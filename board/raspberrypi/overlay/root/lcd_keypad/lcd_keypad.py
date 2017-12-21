#!/usr/bin/python
#
# Use LCD Keypad HAT for web radio
#
# Author: Johannes Schmitz
#
# Date: 18/12/2017

import time
import os
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

# Make list of button value, text, and backlight color.
buttons = ( (LCD.SELECT, 'Select', (1,1,1)),
            (LCD.LEFT,   'Left'  , (1,0,0)),
            (LCD.UP,     'Up'    , (0,0,1)),
            (LCD.DOWN,   'Down'  , (0,1,0)),
            (LCD.RIGHT,  'Right' , (1,0,1)) )

def update_station_info():
    f = os.popen("mpc current -f [%name%]")
    station = ""
    for i in f.readlines():
        station = station + i
    lcd.clear()
    lcd.message(station[:16]+'\n'+station[16:32])

# Initial text
lcd.set_color(0,0,0)
lcd.clear()
lcd.message('Quick Pi \nWeb Radio')
time.sleep(2.5)
update_station_info()

while True:
    # Loop through each button and check if it is pressed.
    if lcd.is_pressed(LCD.LEFT):
        os.system('mpc prev')
        time.sleep(0.2)
        os.system('mpc play')
        update_station_info()
    if lcd.is_pressed(LCD.RIGHT):
        os.system('mpc next')
        time.sleep(0.2)
        os.system('mpc play')
        update_station_info()
    if lcd.is_pressed(LCD.UP):
        os.system('mpc volume +10')
        lcd.clear()
        lcd.message('Volume UP')
        time.sleep(0.5)
        update_station_info()
    if lcd.is_pressed(LCD.DOWN):
        os.system('mpc volume -10')
        lcd.clear()
        lcd.message('Volume DOWN')
        time.sleep(0.5)
        update_station_info()
    if lcd.is_pressed(LCD.SELECT):
        update_station_info()
        time.sleep(0.5)
    time.sleep(0.1)
