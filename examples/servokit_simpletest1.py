"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

# SEND MAX THROTTLE (1) command to motor...
kit.continuous_servo[1].throttle = 1
time.sleep(2)
# SET motor to 50% with a (.5) command...
kit.continuous_servo[1].throttle = .5
time.sleep(2)
# STOP motor with a STOP THROTTLE (-1) command...
kit.continuous_servo[1].throttle = -1
time.sleep(3)

# ACTIVATE servo on channel 0 to its 180 deg setting...
kit.servo[0].angle = 180
# PAUSE 1 second...
time.sleep(1)
# ACTIVATE servo on channel 0 to it 0 deg setting...
kit.servo[0].angle = 0
time.sleep(2)

