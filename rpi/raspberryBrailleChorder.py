#!/usr/bin/env python2

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Examples of using RPi.GPIO: https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/

# Imports
import RPi.GPIO as GPIO

# Definitions
key_ri12 = 2
key_rr12 = 15
key_ir12 = 22

key_ri45 = 3
key_rr45 = 17
key_ir45 = 23

key_ri37 = 4
key_rr37 = 18
key_ir37 = 24

key_ri68 = 14
key_rr68 = 27
key_ir68 = 25

key_num = 10
key_cap = 9
key_macro = 11

all_channels = [

    key_ri12,
    key_rr12,
    key_ir12,

    key_ri45,
    key_rr45,
    key_ir45,

    key_ri37,
    key_rr37,
    key_ir37,

    key_ri68,
    key_rr68,
    key_ir68,

    key_num,
    key_cap,
    key_macro,
]

def setup():
    """ Initial setup. """

    # Use GPIO numbers (not board pin numbers)
    GPIO.setmode(GPIO.BCM)

    # Set the required pins as Inputs with pull-up
    GPIO.setup(all_channels, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def cleanup():
    """ Cleanup at the end of the script. """
    GPIO.cleanup(all_channels)


def main():
    """ Main Subroutine. """
    setup()

    # Test a read
    print("GPIO for RI 12 value: " + str(GPIO.input(key_ri12)))

    # TODO Main loop here

    cleanup()

if __name__ == "__main__":
    main()



