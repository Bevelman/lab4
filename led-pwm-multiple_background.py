#!/usr/bin/python3

import RPi.GPIO as gpio
import json
import time

ledPins = [18,19,21]
pwms = []

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

for i in range(3):
  gpio.setup(ledPins[i], gpio.OUT)
  pwm[i] = gpio.PWM(ledPins[i], 100)
  pwm[i].start(0)

while True:
  # The next 3 lines are just in case file is empty or can't be opened:
  led_num = '1'
  slider_val = '0'
  data = json.loads("'led':led_num, 'slider':slider_val")  

  # Get data from the file:
  with open("led-pwm-multiple.txt", 'r') as f:
    data = json.load(f)

  # Change the DC for the given LED:
  led_num = int(data['led'])
  slider_val = int(data['slider'])
  pwm[led_num-1].ChangeDutyCycle(slider_val)

  time.sleep(0.1)  # small sleep step to avoid re-opening the file too often
