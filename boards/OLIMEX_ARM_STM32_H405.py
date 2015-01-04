#!/bin/false
# This file is part of Espruino, a JavaScript interpreter for Microcontrollers
#
# Copyright (C) 2013 Gordon Williams <gw@pur3.co.uk>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# ----------------------------------------------------------------------------------------
# This file contains information for a specific board - the available pins, and where LEDs,
# Buttons, and other in-built peripherals are. It is used to build documentation as well
# as various source and header files for Espruino.
# ----------------------------------------------------------------------------------------

import pinutils;
import json;
info = {
 'name' : "Olimex ARM STM32-H405",
 'link' :  [ "https://www.olimex.com/Products/ARM/ST/STM32-H405/",
            "https://www.olimex.com/Products/ARM/ST/STM32-H405/resources/STM32-H405_sch.pdf",
            # same board as H103, see rev. C notes on last page
            "https://www.olimex.com/Products/ARM/ST/STM32-H103/resources/STM32-H103.pdf"
            ],
 'variables' : 5450,
 'binary_name' : 'espruino_%v_olimex_stm32_h405.bin'
};
chip = {
  'part' : "STM32F405RGT6", #T6
  'family' : "STM32F4",
  'package' : "LQFP64",
  'ram' : 192,
  'flash' : 1024,
  'speed' : 168,
  'usart' : 3,
  'spi' : 2,
  'i2c' : 2,
  'adc' : 3,
  'dac' : 0,
};

# left-right, or top-bottom order
board = {
# Ext2 PIN 2-26
  'top' : [ 'VDDA','GNDA','3V3','A2','C3','A4','C5','B11','B12','B15','C7','5VUSB','GND'],
# Ext2 PIN 1-25
  'top2' : [ 'C2','A0','GND','A1','A3','C4','B10','B13','B14','C6','C8','C9','VIN'],
# Ext1 pin 1-25
    'bottom2' : ['A11','A12','3V3','A10','C11','D2','B6','B7','B9','C0','B0','VBAT','NRST'],
# Ext1 pin 2-26
    'bottom' : ['A8','A9','GND','C10','C12','B5','A6','B8','A5','C1','A7','C13','B1'],
#JTAG PIN 1-19
  'jtag1' : ['3V3','B4','A15','A13','A14','NC','B3','NRST','NC','NC'],
  'jtag2' : ['3V3','GND','GND','GND','GND','GND','GND','GND','GND','GND'],
# BOOT0/BOO4
  'right' : ['BOOT0','B2']
};
board["bottom"].reverse()
board["bottom2"].reverse()
board["jtag1"].reverse()
board["jtag2"].reverse()

devices = {
  'LED1' : { 'pin' : 'C12' },
  'BTN1' : { 'pin' : 'A0' },
  'USB' : { 'pin_disc' :  'C11',
            'pin_dm' : 'A11',
            'pin_dp' : 'A12'
          }
};

board_css = """
#board {
    width: 742px;
    height: 742px;
    top: 0px;
    left: 100px;
    background-image: url(img/OLIMEX_SMT32_H405.jpg);
}

#boardcontainer {
  height: 1024px;
}

#top {
    top: 372px;
    right: 262px;
}
#top2  {
    top: 450px;
    left: 135px;
}

#bottom {
    top: 708px;
    left: 143px;
}
#bottom2  {
    top: 630px;
    left: 157px;
}

#right {
    top: 66px;
    left: 565px;
}

#jtag1 {
    left: 110px;
    top: 70px;
}
#jtag2 {
    left: -20px;
    top: 70px;
}

.jtag1pin, .jtag2pin {
    height: 24px;
}

.pin {
    font-size: .5em;
}

""";

def get_pins():
    pins = pinutils.scan_pin_file([], 'stm32f40x.csv', 6, 9, 10)
    return pinutils.only_from_package(pinutils.fill_gaps_in_pin_list(pins), chip["package"])
