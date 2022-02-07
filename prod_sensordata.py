
#!/usr/bin/env python

# coding: utf-8

# In[1]:


#!/usr/bin/python

import spidev
import time
import os

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000


# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts

# Define sensor channels
Fc_1 = 0
Fc_2 = 1
Fc_3 = 2
Fc_4 = 3

# Define delay between readings
delay = 3

def PressureSensors():
    while True:
    # Read the Force sensor data
        Force_level_1 = ReadChannel(Fc_1)
        Force_volts_1 = ConvertVolts(Force_level_1, 2)

        Force_level_2 = ReadChannel(Fc_2)
        Force_volts_2= ConvertVolts(Force_level_2, 2)

        Force_level_3 = ReadChannel(Fc_3)
        Force_volts_3 = ConvertVolts(Force_level_3, 2)

        Force_level_4 = ReadChannel(Fc_4)
        Force_volts_4 = ConvertVolts(Force_level_4, 2)

    # Print out results
        print
        "--------------------------------------------"
        print("Force for Channel 1: {} ({}V)".format(Force_level_1, Force_volts_1))
        print
        "--------------------------------------------"
        print("Force for Channel 2: {} ({}V)".format(Force_level_2, Force_volts_2))
        print
        "--------------------------------------------"  
        print("Force for Channel 3: {} ({}V)".format(Force_level_3, Force_volts_3))
        print
        "--------------------------------------------"
        print("Force for Channel 4: {} ({}V)".format(Force_level_4, Force_volts_4))

        # Wait before repeating loop
        time.sleep(delay)
    
    return Force_level_1,Force_level_2,Force_level_3,Force_level_4, Force_volts_1,Force_volts_2,Force_volts_3,Force_volts_4



