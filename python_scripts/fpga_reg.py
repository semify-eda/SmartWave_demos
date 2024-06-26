#marker_template_start
#multidata: globaldata:../../pkg/global_templating_data.json
#multidata: wfg_core_top:../../wfg/wfg_core/data/wfg_core_reg.json
#multidata: wfg_drive_i2c_top:../../wfg/wfg_drive_i2c/data/wfg_drive_i2c_reg.json
#multidata: wfg_drive_i2ct_top:../../wfg/wfg_drive_i2ct/data/wfg_drive_i2ct_reg.json
#multidata: wfg_drive_pat_top:../../wfg/wfg_drive_pat/data/wfg_drive_pat_reg.json
#multidata: wfg_drive_spi_top:../../wfg/wfg_drive_spi/data/wfg_drive_spi_reg.json
#multidata: wfg_drive_uart_top:../../wfg/wfg_drive_uart/data/wfg_drive_uart_reg.json
#multidata: wfg_stim_mem_top:../../wfg/wfg_stim_mem/data/wfg_stim_mem_reg.json
#multidata: wfg_record_mem_top:../../wfg/wfg_record_mem/data/wfg_record_mem_reg.json
#multidata: wfg_pin_mux_top:../../wfg/wfg_pin_mux/data/wfg_pin_mux_reg.json
#multidata: wfg_sysctrl_reg:../../wfg/wfg_top/data/wfg_sysctrl_reg.json
#template: python_registers/registers.template
#marker_template_code

class FPGA_Reg:
  def __init__(self):
    return



  output_pins  = {

    "wfg_drive_spi_top_0_sclk" : 32,
    "wfg_drive_spi_top_0_cs" : 31,
    "wfg_drive_spi_top_0_dout" : 30,
    "wfg_drive_spi_top_1_sclk" : 29,
    "wfg_drive_spi_top_1_cs" : 28,
    "wfg_drive_spi_top_1_dout" : 27,
    "wfg_drive_pat_top_0_output_0" : 26,
    "wfg_drive_pat_top_0_output_1" : 25,
    "wfg_drive_pat_top_0_output_2" : 24,
    "wfg_drive_pat_top_0_output_3" : 23,
    "wfg_drive_pat_top_0_output_4" : 22,
    "wfg_drive_pat_top_0_output_5" : 21,
    "wfg_drive_pat_top_0_output_6" : 20,
    "wfg_drive_pat_top_0_output_7" : 19,
    "wfg_drive_pat_top_0_output_8" : 18,
    "wfg_drive_pat_top_0_output_9" : 17,
    "wfg_drive_pat_top_0_output_10" : 16,
    "wfg_drive_pat_top_0_output_11" : 15,
    "wfg_drive_pat_top_0_output_12" : 14,
    "wfg_drive_pat_top_0_output_13" : 13,
    "wfg_drive_pat_top_0_output_14" : 12,
    "wfg_drive_pat_top_0_output_15" : 11,
    "wfg_drive_i2c_top_0_scl" : 10,
    "wfg_drive_i2c_top_0_sda" : 9,
    "wfg_drive_i2c_top_1_scl" : 8,
    "wfg_drive_i2c_top_1_sda" : 7,
    "wfg_drive_i2ct_top_0_scl" : 6,
    "wfg_drive_i2ct_top_0_sda" : 5,
    "wfg_drive_uart_top_0_tx" : 4,
    "wfg_drive_uart_top_1_tx" : 3
  };


  input_pins  = {

    "wfg_drive_spi_top_0_din" : 9,
    "wfg_drive_spi_top_1_din" : 8,
    "wfg_drive_i2c_top_0_scl" : 7,
    "wfg_drive_i2c_top_0_sda" : 6,
    "wfg_drive_i2c_top_1_scl" : 5,
    "wfg_drive_i2c_top_1_sda" : 4,
    "wfg_drive_i2ct_top_0_scl" : 3,
    "wfg_drive_i2ct_top_0_sda" : 2,
    "wfg_drive_uart_top_0_rx" : 1,
    "wfg_drive_uart_top_1_rx" : 0
  };


  memory = 0x20000


  registers = {
    "wfg_interconnect_top" : {
      "wfg_drive_spi_top_0_select_0" : {
        "addr" : 0x44000,
        "disconnect" : 0x00,
        "wfg_stim_mem_top_0" : 0x01,
        "wfg_stim_mem_top_1" : 0x02,
        "wfg_stim_mem_top_2" : 0x03,
        "wfg_stim_mem_top_3" : 0x04,
        "MSB" : 7,
        "LSB" : 0
      },
      "wfg_drive_spi_top_1_select_0" : {
        "addr" : 0x44001,
        "disconnect" : 0x00,
        "wfg_stim_mem_top_0" : 0x01,
        "wfg_stim_mem_top_1" : 0x02,
        "wfg_stim_mem_top_2" : 0x03,
        "wfg_stim_mem_top_3" : 0x04,
        "MSB" : 7,
        "LSB" : 0
      },
      "wfg_drive_pat_top_0_select_0" : {
        "addr" : 0x44010,
        "disconnect" : 0x00,
        "wfg_stim_mem_top_0" : 0x01,
        "wfg_stim_mem_top_1" : 0x02,
        "wfg_stim_mem_top_2" : 0x03,
        "wfg_stim_mem_top_3" : 0x04,
        "MSB" : 7,
        "LSB" : 0
      },
      "wfg_drive_i2c_top_0_select_0" : {
        "addr" : 0x44020,
        "disconnect" : 0x00,
        "wfg_stim_mem_top_0" : 0x01,
        "wfg_stim_mem_top_1" : 0x02,
        "wfg_stim_mem_top_2" : 0x03,
        "wfg_stim_mem_top_3" : 0x04,
        "MSB" : 7,
        "LSB" : 0
      },
      "wfg_drive_i2c_top_1_select_0" : {
        "addr" : 0x44021,
        "disconnect" : 0x00,
        "wfg_stim_mem_top_0" : 0x01,
        "wfg_stim_mem_top_1" : 0x02,
        "wfg_stim_mem_top_2" : 0x03,
        "wfg_stim_mem_top_3" : 0x04,
        "MSB" : 7,
        "LSB" : 0
      },

      "wfg_drive_uart_top_0_select_0" : {
        "addr" : 0x44030,
        "disconnect" : 0x00,
        "wfg_stim_mem_top_0" : 0x01,
        "wfg_stim_mem_top_1" : 0x02,
        "wfg_stim_mem_top_2" : 0x03,
        "wfg_stim_mem_top_3" : 0x04,
        "MSB" : 7,
        "LSB" : 0
      },
      "wfg_drive_uart_top_1_select_0" : {
        "addr" : 0x44031,
        "disconnect" : 0x00,
        "wfg_stim_mem_top_0" : 0x01,
        "wfg_stim_mem_top_1" : 0x02,
        "wfg_stim_mem_top_2" : 0x03,
        "wfg_stim_mem_top_3" : 0x04,
        "MSB" : 7,
        "LSB" : 0
      },
      "wfg_record_mem_top_0_select_0" : {
        "addr" : 0x440f0,
        "disconnect" : 0x00,
        "wfg_drive_spi_top_0" : 0x01,
        "wfg_drive_spi_top_1" : 0x02,
        "wfg_drive_pat_top_0" : 0x11,
        "wfg_drive_i2c_top_0" : 0x21,
        "wfg_drive_i2c_top_1" : 0x22,
        "wfg_drive_i2ct_top_0" : 0x21,
        "wfg_drive_uart_top_0" : 0x31,
        "wfg_drive_uart_top_1" : 0x32,
        "MSB" : 7,
        "LSB" : 0
      },
      "wfg_record_mem_top_1_select_0" : {
        "addr" : 0x440f1,
        "disconnect" : 0x00,
        "wfg_drive_spi_top_0" : 0x01,
        "wfg_drive_spi_top_1" : 0x02,
        "wfg_drive_pat_top_0" : 0x11,
        "wfg_drive_i2c_top_0" : 0x21,
        "wfg_drive_i2c_top_1" : 0x22,
        "wfg_drive_i2ct_top_0" : 0x21,
        "wfg_drive_uart_top_0" : 0x31,
        "wfg_drive_uart_top_1" : 0x32,
        "MSB" : 7,
        "LSB" : 0
      },
      "wfg_record_mem_top_2_select_0" : {
        "addr" : 0x440f2,
        "disconnect" : 0x00,
        "wfg_drive_spi_top_0" : 0x01,
        "wfg_drive_spi_top_1" : 0x02,
        "wfg_drive_pat_top_0" : 0x11,
        "wfg_drive_i2c_top_0" : 0x21,
        "wfg_drive_i2c_top_1" : 0x22,
        "wfg_drive_i2ct_top_0" : 0x21,
        "wfg_drive_uart_top_0" : 0x31,
        "wfg_drive_uart_top_1" : 0x32,
        "MSB" : 7,
        "LSB" : 0
      },
      "wfg_record_mem_top_3_select_0" : {
        "addr" : 0x440f3,
        "disconnect" : 0x00,
        "wfg_drive_spi_top_0" : 0x01,
        "wfg_drive_spi_top_1" : 0x02,
        "wfg_drive_pat_top_0" : 0x11,
        "wfg_drive_i2c_top_0" : 0x21,
        "wfg_drive_i2c_top_1" : 0x22,
        "wfg_drive_i2ct_top_0" : 0x21,
        "wfg_drive_uart_top_0" : 0x31,
        "wfg_drive_uart_top_1" : 0x32,
        "MSB" : 7,
        "LSB" : 0
      }

    },


      "wfg_core_top" : {
        "CTRL" : {
          "addr" : 0x40000,
          "EN" : {
            "MSB" : 0,
            "LSB" : 0
          }
        },
        "CFG" : {
          "addr" : 0x40004,
          "SYNC" : {
            "MSB" : 15,
            "LSB" : 0
          },
          "SUBCYCLE" : {
            "MSB" : 31,
            "LSB" : 16
          }
        },
        "MODULE_INFO" : {
          "addr" : 0x400fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }
        }
      },
      "wfg_pin_mux_top" : {
        "OUTPUT_SEL_0" : {
          "addr" : 0x46000,
          "0" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "1" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "2" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "3" : {
            "MSB" : 31,
            "LSB" : 24
          }
        },
        "OUTPUT_SEL_1" : {
          "addr" : 0x46004,
          "4" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "5" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "6" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "7" : {
            "MSB" : 31,
            "LSB" : 24
          }
        },
        "OUTPUT_SEL_2" : {
          "addr" : 0x46008,
          "8" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "9" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "10" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "11" : {
            "MSB" : 31,
            "LSB" : 24
          }
        },
        "OUTPUT_SEL_3" : {
          "addr" : 0x4600c,
          "12" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "13" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "14" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "15" : {
            "MSB" : 31,
            "LSB" : 24
          }
        },
        "PULLUP_SEL_0" : {
          "addr" : 0x46010,
          "0" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "1" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "2" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "3" : {
            "MSB" : 31,
            "LSB" : 24
          }
        },
        "PULLUP_SEL_1" : {
          "addr" : 0x46014,
          "4" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "5" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "6" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "7" : {
            "MSB" : 31,
            "LSB" : 24
          }
        },
        "PULLUP_SEL_2" : {
          "addr" : 0x46018,
          "8" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "9" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "10" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "11" : {
            "MSB" : 31,
            "LSB" : 24
          }
        },
        "PULLUP_SEL_3" : {
          "addr" : 0x4601c,
          "12" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "13" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "14" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "15" : {
            "MSB" : 31,
            "LSB" : 24
          }
        },
        "INPUT_SEL_0" : {
          "addr" : 0x46020,
          "0" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "1" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "2" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "3" : {
            "MSB" : 31,
            "LSB" : 24
          }
        },
        "INPUT_SEL_1" : {
          "addr" : 0x46024,
          "4" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "5" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "6" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "7" : {
            "MSB" : 31,
            "LSB" : 24
          }
        },
        "INPUT_SEL_2" : {
          "addr" : 0x46028,
          "8" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "9" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "10" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "11" : {
            "MSB" : 31,
            "LSB" : 24
          }
        },
        "INPUT_SEL_3" : {
          "addr" : 0x4602c,
          "12" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "13" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "14" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "15" : {
            "MSB" : 31,
            "LSB" : 24
          }
        },
        "MIRROR_OUTPUT" : {
          "addr" : 0x46030,
          "VAL" : {
            "MSB" : 15,
            "LSB" : 0
          }
        },
        "MIRROR_PULLUP" : {
          "addr" : 0x46034,
          "VAL" : {
            "MSB" : 15,
            "LSB" : 0
          }
        },
        "MIRROR_INPUT" : {
          "addr" : 0x46038,
          "VAL" : {
            "MSB" : 15,
            "LSB" : 0
          }
        },
        "PIN_IR_RISING" : {
          "addr" : 0x46090,
          "VAL" : {
            "MSB" : 15,
            "LSB" : 0
          }
        },
        "PIN_IR_FALLING" : {
          "addr" : 0x46094,
          "VAL" : {
            "MSB" : 15,
            "LSB" : 0
          }
        },
        "ISR" : {
          "addr" : 0x460a0,
          "PIN" : {
            "MSB" : 15,
            "LSB" : 0
          }
        },
        "IER" : {
          "addr" : 0x460a4,
          "PIN" : {
            "MSB" : 15,
            "LSB" : 0
          }
        },
        "ICR" : {
          "addr" : 0x460a8,
          "PIN" : {
            "MSB" : 15,
            "LSB" : 0
          }
        },
        "MODULE_INFO" : {
          "addr" : 0x460fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }
        }
      },
      "wfg_sysctrl_reg" : {
        "PRODUCT" : {
          "addr" : 0x48000,
          "ID" : {
            "MSB" : 31,
            "LSB" : 0
          }
        },
        "FPGA_VERSION" : {
          "addr" : 0x48004,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "DEV" : {
            "MSB" : 24,
            "LSB" : 24
          }
        },
        "GENDATE" : {
          "addr" : 0x48008,
          "YEAR" : {
            "MSB" : 10,
            "LSB" : 0
          },
          "MONTH" : {
            "MSB" : 14,
            "LSB" : 11
          },
          "DAY" : {
            "MSB" : 19,
            "LSB" : 15
          },
          "HOUR" : {
            "MSB" : 23,
            "LSB" : 20
          },
          "MINUTE" : {
            "MSB" : 29,
            "LSB" : 24
          }
        },
        "CLK_SPEED" : {
          "addr" : 0x4800c,
          "VAL" : {
            "MSB" : 7,
            "LSB" : 0
          }
        },
        "SOC_CTRL" : {
          "addr" : 0x48010,
          "FETCH_ENABLE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "CORE_RESET_N" : {
            "MSB" : 1,
            "LSB" : 1
          }
        },
        "SOC_STATUS" : {
          "addr" : 0x48014,
          "CORE_SLEEP" : {
            "MSB" : 0,
            "LSB" : 0
          }
        },
        "RESET_FLAGS" : {
          "addr" : 0x48020,
          "WFG" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "SOC" : {
            "MSB" : 1,
            "LSB" : 1
          }
        },
        "RESET_CLEARS" : {
          "addr" : 0x48024,
          "WFG" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "SOC" : {
            "MSB" : 1,
            "LSB" : 1
          }
        },
        "ISR" : {
          "addr" : 0x480a0,
          "WISHBONE_INVALID_ADDRESS" : {
            "MSB" : 0,
            "LSB" : 0
          }
        },
        "IER" : {
          "addr" : 0x480a4,
          "WISHBONE_INVALID_ADDRESS" : {
            "MSB" : 0,
            "LSB" : 0
          }
        },
        "ICR" : {
          "addr" : 0x480a8,
          "WISHBONE_INVALID_ADDRESS" : {
            "MSB" : 0,
            "LSB" : 0
          }
        },
        "INTERRUPT_MIRROR" : {
          "addr" : 0x480b0,
          "VECTOR" : {
            "MSB" : 31,
            "LSB" : 0
          }
        },
        "MODULE_INFO" : {
          "addr" : 0x480fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }
        }
      }
      ,

      "wfg_stim_mem_top_0" : {
        "CTRL" : {
          "addr" : 0x60000,
          "EN" : {
            "MSB" : 0,
            "LSB" : 0
          }

        },
        "CFG" : {
          "addr" : 0x60004,
          "CNT" : {
            "MSB" : 7,
            "LSB" : 0
          }

        },
        "START" : {
          "addr" : 0x60008,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "STOP" : {
          "addr" : 0x6000c,
          "VAL" : {
            "MSB" : 13,
            "LSB" : 0
          }

        },
        "STEP" : {
          "addr" : 0x60010,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "ADDR" : {
          "addr" : 0x60014,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "GAIN" : {
          "addr" : 0x60018,
          "VAL" : {
            "MSB" : 15,
            "LSB" : 0
          }

        },
        "OFFSET" : {
          "addr" : 0x6001c,
          "VAL" : {
            "MSB" : 31,
            "LSB" : 0
          }

        },
        "ISR" : {
          "addr" : 0x600a0,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "IER" : {
          "addr" : 0x600a4,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "ICR" : {
          "addr" : 0x600a8,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "MODULE_INFO" : {
          "addr" : 0x600fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }

        }
      },
      "wfg_stim_mem_top_1" : {
        "CTRL" : {
          "addr" : 0x60100,
          "EN" : {
            "MSB" : 0,
            "LSB" : 0
          }

        },
        "CFG" : {
          "addr" : 0x60104,
          "CNT" : {
            "MSB" : 7,
            "LSB" : 0
          }

        },
        "START" : {
          "addr" : 0x60108,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "STOP" : {
          "addr" : 0x6010c,
          "VAL" : {
            "MSB" : 13,
            "LSB" : 0
          }

        },
        "STEP" : {
          "addr" : 0x60110,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "ADDR" : {
          "addr" : 0x60114,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "GAIN" : {
          "addr" : 0x60118,
          "VAL" : {
            "MSB" : 15,
            "LSB" : 0
          }

        },
        "OFFSET" : {
          "addr" : 0x6011c,
          "VAL" : {
            "MSB" : 31,
            "LSB" : 0
          }

        },
        "ISR" : {
          "addr" : 0x601a0,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "IER" : {
          "addr" : 0x601a4,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "ICR" : {
          "addr" : 0x601a8,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "MODULE_INFO" : {
          "addr" : 0x601fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }

        }
      },
      "wfg_stim_mem_top_2" : {
        "CTRL" : {
          "addr" : 0x60200,
          "EN" : {
            "MSB" : 0,
            "LSB" : 0
          }

        },
        "CFG" : {
          "addr" : 0x60204,
          "CNT" : {
            "MSB" : 7,
            "LSB" : 0
          }

        },
        "START" : {
          "addr" : 0x60208,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "STOP" : {
          "addr" : 0x6020c,
          "VAL" : {
            "MSB" : 13,
            "LSB" : 0
          }

        },
        "STEP" : {
          "addr" : 0x60210,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "ADDR" : {
          "addr" : 0x60214,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "GAIN" : {
          "addr" : 0x60218,
          "VAL" : {
            "MSB" : 15,
            "LSB" : 0
          }

        },
        "OFFSET" : {
          "addr" : 0x6021c,
          "VAL" : {
            "MSB" : 31,
            "LSB" : 0
          }

        },
        "ISR" : {
          "addr" : 0x602a0,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "IER" : {
          "addr" : 0x602a4,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "ICR" : {
          "addr" : 0x602a8,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "MODULE_INFO" : {
          "addr" : 0x602fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }

        }
      },
      "wfg_stim_mem_top_3" : {
        "CTRL" : {
          "addr" : 0x60300,
          "EN" : {
            "MSB" : 0,
            "LSB" : 0
          }

        },
        "CFG" : {
          "addr" : 0x60304,
          "CNT" : {
            "MSB" : 7,
            "LSB" : 0
          }

        },
        "START" : {
          "addr" : 0x60308,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "STOP" : {
          "addr" : 0x6030c,
          "VAL" : {
            "MSB" : 13,
            "LSB" : 0
          }

        },
        "STEP" : {
          "addr" : 0x60310,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "ADDR" : {
          "addr" : 0x60314,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "GAIN" : {
          "addr" : 0x60318,
          "VAL" : {
            "MSB" : 15,
            "LSB" : 0
          }

        },
        "OFFSET" : {
          "addr" : 0x6031c,
          "VAL" : {
            "MSB" : 31,
            "LSB" : 0
          }

        },
        "ISR" : {
          "addr" : 0x603a0,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "IER" : {
          "addr" : 0x603a4,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "ICR" : {
          "addr" : 0x603a8,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "MODULE_INFO" : {
          "addr" : 0x603fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }

        }
      },
      "wfg_drive_spi_top_0" : {
        "CTRL" : {
          "addr" : 0x80000,
          "EN" : {
            "MSB" : 0,
            "LSB" : 0
          }

        },
        "CFG" : {
          "addr" : 0x80004,
          "CPOL" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "CPHA" : {
            "MSB" : 1,
            "LSB" : 1
          },
          "LSBFIRST" : {
            "MSB" : 2,
            "LSB" : 2
          },
          "SSPOL" : {
            "MSB" : 3,
            "LSB" : 3
          },
          "CORE_SEL" : {
            "MSB" : 4,
            "LSB" : 4
          },
          "CORE_DEPENDENT" : {
            "MSB" : 5,
            "LSB" : 5
          },
          "IO_DELAY_COMPENSATION" : {
            "MSB" : 8,
            "LSB" : 6
          }

        },
        "CLKCFG" : {
          "addr" : 0x80008,
          "DIV" : {
            "MSB" : 31,
            "LSB" : 0
          }

        },
        "SPI_LEN" : {
          "addr" : 0x8000c,
          "VAL" : {
            "MSB" : 5,
            "LSB" : 0
          }

        },
        "CS_HIGH_TIME" : {
          "addr" : 0x80010,
          "VAL" : {
            "MSB" : 31,
            "LSB" : 0
          }

        },
        "CS_ACTIVE_DELAY_TIME" : {
          "addr" : 0x80014,
          "VAL" : {
            "MSB" : 31,
            "LSB" : 0
          }

        },
        "MODULE_INFO" : {
          "addr" : 0x800fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }

        }
      },
      "wfg_drive_spi_top_1" : {
        "CTRL" : {
          "addr" : 0x80100,
          "EN" : {
            "MSB" : 0,
            "LSB" : 0
          }

        },
        "CFG" : {
          "addr" : 0x80104,
          "CPOL" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "CPHA" : {
            "MSB" : 1,
            "LSB" : 1
          },
          "LSBFIRST" : {
            "MSB" : 2,
            "LSB" : 2
          },
          "SSPOL" : {
            "MSB" : 3,
            "LSB" : 3
          },
          "CORE_SEL" : {
            "MSB" : 4,
            "LSB" : 4
          },
          "CORE_DEPENDENT" : {
            "MSB" : 5,
            "LSB" : 5
          },
          "IO_DELAY_COMPENSATION" : {
            "MSB" : 8,
            "LSB" : 6
          }

        },
        "CLKCFG" : {
          "addr" : 0x80108,
          "DIV" : {
            "MSB" : 31,
            "LSB" : 0
          }

        },
        "SPI_LEN" : {
          "addr" : 0x8010c,
          "VAL" : {
            "MSB" : 5,
            "LSB" : 0
          }

        },
        "CS_HIGH_TIME" : {
          "addr" : 0x80110,
          "VAL" : {
            "MSB" : 31,
            "LSB" : 0
          }

        },
        "CS_ACTIVE_DELAY_TIME" : {
          "addr" : 0x80114,
          "VAL" : {
            "MSB" : 31,
            "LSB" : 0
          }

        },
        "MODULE_INFO" : {
          "addr" : 0x801fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }

        }
      },
      "wfg_drive_pat_top_0" : {
        "CTRL" : {
          "addr" : 0x82000,
          "EN" : {
            "MSB" : 15,
            "LSB" : 0
          }

        },
        "CFG" : {
          "addr" : 0x82004,
          "BEGIN" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "CORE_SEL" : {
            "MSB" : 16,
            "LSB" : 16
          }

        },
        "PATSEL0" : {
          "addr" : 0x82008,
          "LOW" : {
            "MSB" : 15,
            "LSB" : 0
          }

        },
        "PATSEL1" : {
          "addr" : 0x8200c,
          "HIGH" : {
            "MSB" : 15,
            "LSB" : 0
          }

        },
        "MODULE_INFO" : {
          "addr" : 0x820fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }

        }
      },
      "wfg_drive_i2c_top_0" : {
        "CTRL" : {
          "addr" : 0x84000,
          "EN" : {
            "MSB" : 0,
            "LSB" : 0
          }

        },
        "CFG" : {
          "addr" : 0x84004,
          "DEV_ID" : {
            "MSB" : 6,
            "LSB" : 0
          },
          "WAIT_STATE_ENABLED" : {
            "MSB" : 8,
            "LSB" : 8
          },
          "CORE_SEL" : {
            "MSB" : 16,
            "LSB" : 16
          },
          "CORE_DEPENDENT" : {
            "MSB" : 17,
            "LSB" : 17
          }

        },
        "CLKCFG" : {
          "addr" : 0x84008,
          "DIV" : {
            "MSB" : 31,
            "LSB" : 0
          }

        },
        "ISR" : {
          "addr" : 0x840a0,
          "COMMAND_FRAME_ERROR" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "DATA_FRAME_ERROR" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "IER" : {
          "addr" : 0x840a4,
          "COMMAND_FRAME_ERROR" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "DATA_FRAME_ERROR" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "ICR" : {
          "addr" : 0x840a8,
          "COMMAND_FRAME_ERROR" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "DATA_FRAME_ERROR" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "MODULE_INFO" : {
          "addr" : 0x840fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }

        }
      },
      "wfg_drive_i2c_top_1" : {
        "CTRL" : {
          "addr" : 0x84100,
          "EN" : {
            "MSB" : 0,
            "LSB" : 0
          }

        },
        "CFG" : {
          "addr" : 0x84104,
          "DEV_ID" : {
            "MSB" : 6,
            "LSB" : 0
          },
          "WAIT_STATE_ENABLED" : {
            "MSB" : 8,
            "LSB" : 8
          },
          "CORE_SEL" : {
            "MSB" : 16,
            "LSB" : 16
          },
          "CORE_DEPENDENT" : {
            "MSB" : 17,
            "LSB" : 17
          }

        },
        "CLKCFG" : {
          "addr" : 0x84108,
          "DIV" : {
            "MSB" : 31,
            "LSB" : 0
          }

        },
        "ISR" : {
          "addr" : 0x841a0,
          "COMMAND_FRAME_ERROR" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "DATA_FRAME_ERROR" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "IER" : {
          "addr" : 0x841a4,
          "COMMAND_FRAME_ERROR" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "DATA_FRAME_ERROR" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "ICR" : {
          "addr" : 0x841a8,
          "COMMAND_FRAME_ERROR" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "DATA_FRAME_ERROR" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "MODULE_INFO" : {
          "addr" : 0x841fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }

        }
      },
      "wfg_drive_i2ct_top_0" : {
        "CTRL" : {
          "addr" : 0x88000,
          "EN" : {
            "MSB" : 0,
            "LSB" : 0
          }

        },
        "CFG" : {
          "addr" : 0x88004,
          "DEVID" : {
            "MSB" : 7,
            "LSB" : 1
          },
          "ADDRSIZE" : {
            "MSB" : 8,
            "LSB" : 8
          },
          "DATASIZE" : {
            "MSB" : 17,
            "LSB" : 16
          }

        },
        "REGCFG" : {
          "addr" : 0x88010,
          "AUTOINC" : {
            "MSB" : 0,
            "LSB" : 0
          }

        },
        "REGADDR" : {
          "addr" : 0x88014,
          "ADDR" : {
            "MSB" : 15,
            "LSB" : 0
          }

        },
        "REGWDATA" : {
          "addr" : 0x88018,
          "DATA" : {
            "MSB" : 31,
            "LSB" : 0
          }

        },
        "REGWMASK" : {
          "addr" : 0x8801c,
          "MASK" : {
            "MSB" : 31,
            "LSB" : 0
          }

        },
        "REGRDATA" : {
          "addr" : 0x88020,
          "DATA" : {
            "MSB" : 31,
            "LSB" : 0
          }

        },
        "REGRMASK" : {
          "addr" : 0x88024,
          "MASK" : {
            "MSB" : 31,
            "LSB" : 0
          }

        }
      },
      "wfg_drive_uart_top_0" : {
        "CTRL" : {
          "addr" : 0x86000,
          "EN" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "" : {
            "MSB" : 31,
            "LSB" : 31
          }

        },
        "CFG" : {
          "addr" : 0x86004,
          "CORE_SEL" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "TXSIZE" : {
            "MSB" : 4,
            "LSB" : 1
          },
          "CORE_DEPENDENT" : {
            "MSB" : 7,
            "LSB" : 7
          },
          "CDIV" : {
            "MSB" : 31,
            "LSB" : 8
          }

        },
        "CFG2" : {
          "addr" : 0x86008,
          "PARITY_SEL" : {
            "MSB" : 1,
            "LSB" : 0
          },
          "STOP_SEL" : {
            "MSB" : 3,
            "LSB" : 2
          },
          "TX_DELAY" : {
            "MSB" : 19,
            "LSB" : 4
          },
          "SHIFT_DIR" : {
            "MSB" : 20,
            "LSB" : 20
          }

        },
        "RX_CFG" : {
          "addr" : 0x8600c,
          "TIMEOUT" : {
            "MSB" : 9,
            "LSB" : 0
          }

        },
        "ISR" : {
          "addr" : 0x860a0,
          "TIMEOUT_REACHED" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "FRAME_ERROR" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "IER" : {
          "addr" : 0x860a4,
          "TIMEOUT_REACHED" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "FRAME_ERROR" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "ICR" : {
          "addr" : 0x860a8,
          "TIMEOUT_REACHED" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "FRAME_ERROR" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "MODULE_INFO" : {
          "addr" : 0x860fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }

        }
      },
      "wfg_drive_uart_top_1" : {
        "CTRL" : {
          "addr" : 0x86100,
          "EN" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "" : {
            "MSB" : 31,
            "LSB" : 31
          }

        },
        "CFG" : {
          "addr" : 0x86104,
          "CORE_SEL" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "TXSIZE" : {
            "MSB" : 4,
            "LSB" : 1
          },
          "CORE_DEPENDENT" : {
            "MSB" : 7,
            "LSB" : 7
          },
          "CDIV" : {
            "MSB" : 31,
            "LSB" : 8
          }

        },
        "CFG2" : {
          "addr" : 0x86108,
          "PARITY_SEL" : {
            "MSB" : 1,
            "LSB" : 0
          },
          "STOP_SEL" : {
            "MSB" : 3,
            "LSB" : 2
          },
          "TX_DELAY" : {
            "MSB" : 19,
            "LSB" : 4
          },
          "SHIFT_DIR" : {
            "MSB" : 20,
            "LSB" : 20
          }

        },
        "RX_CFG" : {
          "addr" : 0x8610c,
          "TIMEOUT" : {
            "MSB" : 9,
            "LSB" : 0
          }

        },
        "ISR" : {
          "addr" : 0x861a0,
          "TIMEOUT_REACHED" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "FRAME_ERROR" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "IER" : {
          "addr" : 0x861a4,
          "TIMEOUT_REACHED" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "FRAME_ERROR" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "ICR" : {
          "addr" : 0x861a8,
          "TIMEOUT_REACHED" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "FRAME_ERROR" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "MODULE_INFO" : {
          "addr" : 0x861fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }

        }
      },
      "wfg_record_mem_top_0" : {
        "CTRL" : {
          "addr" : 0xa0000,
          "EN" : {
            "MSB" : 0,
            "LSB" : 0
          }

        },
        "CFG" : {
          "addr" : 0xa0004,
          "CNT" : {
            "MSB" : 7,
            "LSB" : 0
          }

        },
        "START" : {
          "addr" : 0xa0008,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "STOP" : {
          "addr" : 0xa000c,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "STEP" : {
          "addr" : 0xa0010,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "ADDR" : {
          "addr" : 0xa0014,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "ISR" : {
          "addr" : 0xa00a0,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "IER" : {
          "addr" : 0xa00a4,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "ICR" : {
          "addr" : 0xa00a8,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "MODULE_INFO" : {
          "addr" : 0xa00fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }

        }
      },
      "wfg_record_mem_top_1" : {
        "CTRL" : {
          "addr" : 0xa0100,
          "EN" : {
            "MSB" : 0,
            "LSB" : 0
          }

        },
        "CFG" : {
          "addr" : 0xa0104,
          "CNT" : {
            "MSB" : 7,
            "LSB" : 0
          }

        },
        "START" : {
          "addr" : 0xa0108,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "STOP" : {
          "addr" : 0xa010c,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "STEP" : {
          "addr" : 0xa0110,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "ADDR" : {
          "addr" : 0xa0114,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "ISR" : {
          "addr" : 0xa01a0,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "IER" : {
          "addr" : 0xa01a4,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "ICR" : {
          "addr" : 0xa01a8,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "MODULE_INFO" : {
          "addr" : 0xa01fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }

        }
      },
      "wfg_record_mem_top_2" : {
        "CTRL" : {
          "addr" : 0xa0200,
          "EN" : {
            "MSB" : 0,
            "LSB" : 0
          }

        },
        "CFG" : {
          "addr" : 0xa0204,
          "CNT" : {
            "MSB" : 7,
            "LSB" : 0
          }

        },
        "START" : {
          "addr" : 0xa0208,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "STOP" : {
          "addr" : 0xa020c,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "STEP" : {
          "addr" : 0xa0210,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "ADDR" : {
          "addr" : 0xa0214,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "ISR" : {
          "addr" : 0xa02a0,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "IER" : {
          "addr" : 0xa02a4,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "ICR" : {
          "addr" : 0xa02a8,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "MODULE_INFO" : {
          "addr" : 0xa02fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }

        }
      },
      "wfg_record_mem_top_3" : {
        "CTRL" : {
          "addr" : 0xa0300,
          "EN" : {
            "MSB" : 0,
            "LSB" : 0
          }

        },
        "CFG" : {
          "addr" : 0xa0304,
          "CNT" : {
            "MSB" : 7,
            "LSB" : 0
          }

        },
        "START" : {
          "addr" : 0xa0308,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "STOP" : {
          "addr" : 0xa030c,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "STEP" : {
          "addr" : 0xa0310,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "ADDR" : {
          "addr" : 0xa0314,
          "VAL" : {
            "MSB" : 12,
            "LSB" : 0
          }

        },
        "ISR" : {
          "addr" : 0xa03a0,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "IER" : {
          "addr" : 0xa03a4,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "ICR" : {
          "addr" : 0xa03a8,
          "DONE" : {
            "MSB" : 0,
            "LSB" : 0
          },
          "END" : {
            "MSB" : 1,
            "LSB" : 1
          }

        },
        "MODULE_INFO" : {
          "addr" : 0xa03fc,
          "PATCH" : {
            "MSB" : 7,
            "LSB" : 0
          },
          "MINOR" : {
            "MSB" : 15,
            "LSB" : 8
          },
          "MAJOR" : {
            "MSB" : 23,
            "LSB" : 16
          },
          "TYPE" : {
            "MSB" : 27,
            "LSB" : 27
          },
          "BLOCK" : {
            "MSB" : 31,
            "LSB" : 28
          }

        }
      }

  }


#marker_template_end
