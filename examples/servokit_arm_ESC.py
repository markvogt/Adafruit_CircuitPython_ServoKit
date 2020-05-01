# App to ARM the ESC controlling a brushless motor prior to running any other app that will later control the motor...

# IMPORT required python modules (files with python code defining classes, methods and executable code)...
import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit. # 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

# ARM the motor on channel 1...
kit.continuous_servo[1].throttle = 1
time.sleep(3)
kit.continuous_servo[1].throttle = 0
time.sleep(3)
#kit.continuous_servo[1].throttle = 0.1
