from machine import I2C, Pin
from sht30 import SHT30
import utime as time

PIN_CLK = 29   # PD6, get the pin number from get_pin_number.py
PIN_SDA = 30   # PC1

clk = Pin(("clk", PIN_CLK), Pin.OUT_OD)   # Select the PIN_CLK as the clock
sda = Pin(("sda", PIN_SDA), Pin.OUT_OD)   # Select the PIN_SDA as the data line

i2c = I2C(-1, clk, sda, freq=100000)
sensor = SHT30(i2c,0x44)

#print(senser.measure())

#print(senser.measure_int())

while True:
    temperature,xx,humidity,yy = sensor.measure_int()
    print(temperature)
    print(humidity)
    time.sleep_ms(500)
  