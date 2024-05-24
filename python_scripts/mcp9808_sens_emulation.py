"""
Script Name: mcp9808_sens_emulation.py
Description: Simple script that uses the I2C target to emulate the MCP9808 temperature sensor
Author: Adam Horvath
Company: semify GmbH
Copyright © 2024 semify GmbH. All rights reserved.
"""

import sys
import os
import logging
import time
import threading

from datetime import datetime
from SmartWaveAPI import SmartWave
from fpga_reg import FPGA_Reg


def i2ct_conf(sw):
    """
        This function configures the I2C target for the MCP9808 sensor emulation
    """
    i2ct_addr = 0x18  # I2C address of the MCP9808 Temperature Sensor
    i2ct_devid_addr = 0x07  # Unique device ID register address
    i2ct_devid_val = 0x37  # Arbitrary device ID, set to 55

    # Define the registers of the I2C target modules
    i2ct_env = FPGA_Reg.registers["wfg_drive_i2ct_top_0"]
    i2ct_en = i2ct_env["CTRL"]["addr"]
    i2ct_dev_addr = i2ct_env["CFG"]["addr"]
    i2ct_reg_addr = i2ct_env["REGADDR"]["addr"]
    i2ct_regwdata_addr = i2ct_env["REGWDATA"]["addr"]

    # Setup I2C address within the I2C target
    set_addr = 0
    set_addr |= i2ct_addr << i2ct_env["CFG"]["DEVID"]["LSB"]
    set_addr |= 0b01 << i2ct_env["CFG"]["DATASIZE"]["LSB"]
    sw.writeFPGARegister(i2ct_dev_addr, set_addr)
    read_data = sw.readFPGARegister(i2ct_dev_addr)
    read_data = read_data >> i2ct_env["CFG"]["DEVID"]["LSB"]
    logging.info(f"[I2C_T ADDR] - Data read back: {read_data:#0x} from {i2ct_dev_addr:#0x}")

    # Setup DeviceID within the I2C target
    set_id = 0
    set_id |= i2ct_devid_addr << i2ct_env["REGADDR"]["ADDR"]["LSB"]
    sw.writeFPGARegister(i2ct_reg_addr, set_id)

    # Setup DeviceID register within the I2C target
    set_id = 0
    set_id |= i2ct_devid_val << i2ct_env["REGWDATA"]["DATA"]["LSB"]
    sw.writeFPGARegister(i2ct_regwdata_addr, set_id)
    read_data = sw.readFPGARegister(i2ct_regwdata_addr)
    logging.info(f"[DEV ID WRITE_REG] - Data read back: {read_data:#0x} from address: {i2ct_regwdata_addr:#0x}")

    set_en = 0
    set_en |= 1 << i2ct_env["CTRL"]["EN"]["LSB"]
    sw.writeFPGARegister(i2ct_en, set_en)
    read_data = sw.readFPGARegister(i2ct_en)
    read_data = read_data >> i2ct_env["CTRL"]["EN"]["LSB"]
    logging.info(f"[I2C_T EN] - Data read back: {read_data:#0x} from register: {i2ct_en:#0x}")


def i2ct_amb_temp(sw, ta_data):
    """
        This function configures the I2C target for the MCP9808 sensor emulation
    """
    i2ct_ta_reg = 0x05      # Ambient temperature register address

    # Define the registers of the I2C target modules
    i2ct_env = FPGA_Reg.registers["wfg_drive_i2ct_top_0"]
    i2ct_reg_addr = i2ct_env["REGADDR"]["addr"]
    i2ct_regwdata_addr = i2ct_env["REGWDATA"]["addr"]

    # Setup the ambient temperature  register of the I2C target
    set_amb = 0
    set_amb |= i2ct_ta_reg << i2ct_env["REGADDR"]["ADDR"]["LSB"]
    sw.writeFPGARegister(i2ct_reg_addr, set_amb)

    # Setup the ambient register write data of the I2C target
    set_amb = 0
    set_amb |= ta_data << i2ct_env["REGWDATA"]["DATA"]["LSB"]
    sw.writeFPGARegister(i2ct_regwdata_addr, set_amb)
    read_data = sw.readFPGARegister(i2ct_regwdata_addr)
    logging.info(f"[T_AMB WRITE_REG] - Data read back: {read_data:#0x} // {int(read_data)} "
                 f"from address: {i2ct_regwdata_addr:#0x}")


def pin_mux_conf(sw):
    """
        This function routs out the I2C target's SCL and SDA lines onto Pin A1 and Pin A2 of SmartWave
    """
    # Configure the desired pins by writing to the FPGA's register
    i2ct_scl_i = 3  # I2C target SCL input
    i2ct_sda_i = 2  # I2C target SDA input
    i2ct_scl_o = 6  # I2C target SCL output
    i2ct_sda_o = 5  # I2C target SDA output

    # Set I2C target environment for pin muxing
    localenv = FPGA_Reg.registers["wfg_pin_mux_top"]

    # I2CT_SCL and I2CT_SDA input enable
    addr = localenv["INPUT_SEL_0"]["addr"]
    pingroup = 0
    pingroup |= i2ct_scl_i << localenv["INPUT_SEL_0"]["0"]["LSB"]  # SCL on pin A1
    pingroup |= i2ct_sda_i << localenv["INPUT_SEL_0"]["1"]["LSB"]  # SDA on pin A2
    sw.writeFPGARegister(addr, pingroup)

    # I2CT_SCL and I2CT_SDA output enable
    addr = localenv["OUTPUT_SEL_0"]["addr"]
    pingroup = 0
    pingroup |= i2ct_scl_o << localenv["OUTPUT_SEL_0"]["0"]["LSB"]  # SCL on pin A1
    pingroup |= i2ct_sda_o << localenv["OUTPUT_SEL_0"]["1"]["LSB"]  # SDA on pin A2
    sw.writeFPGARegister(addr, pingroup)

    # I2CT_SCL and I2CT_SDA pulled-up enable
    addr = localenv["PULLUP_SEL_0"]["addr"]
    pingroup = 0
    pingroup |= 1 << localenv["PULLUP_SEL_0"]["0"]["LSB"]
    pingroup |= 1 << localenv["PULLUP_SEL_0"]["1"]["LSB"]
    sw.writeFPGARegister(addr, pingroup)


def main():
    """
        Main function for the sensor emulation
    """
    # Basic configuration for logging

    # Create directory to save the log files
    directory = "./mcp9808_emulation.logs"
    if not os.path.exists(directory):
        os.mkdir(directory)

    date_time = datetime.now().strftime("%Y.%m.%d_%H.%M.%S")
    file_name = f'Sensor_emulation_{date_time}.log'
    fq_fn = os.path.join(directory, file_name)
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt="%Y-%m-%d %H:%M:%S",
                        encoding='utf-8', level=logging.DEBUG,
                        handlers=[
                            logging.StreamHandler(sys.stdout),
                            logging.FileHandler(filename=fq_fn)
                        ]
                        )

    ta_data = 30

    def update_ta_data(sw):
        """
            This function takes a new user input to update the ambient temperature value
        """
        nonlocal ta_data
        while True:
            try:
                new_value = input("Enter new ambient temperature: ")
                if new_value.lower() == 'exit':
                    print("Exiting input thread.")
                    break
                ta_data = int(new_value)
                i2ct_amb_temp(sw, ta_data)
                logging.info(f"Updated ambient temperature to: {ta_data}")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # Setup connection to SmartWave
    with SmartWave().connect() as sw:
        logging.info("Successfully connected to SmartWave")
        logging.info("Configure the I2C target for the MCP9808 temperature sensor emulation")
        i2ct_conf(sw)
        logging.info("Rout out the I2C target SCL and SDA lines to the physical pins")
        pin_mux_conf(sw)
        input_thread = threading.Thread(target=update_ta_data(sw), daemon=True)
        input_thread.start()

        while input_thread.is_alive():
            time.sleep(1)


if __name__ == "__main__":
    main()
