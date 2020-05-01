"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

# ARM the motor on channel 1...
kit.continuous_servo[1].throttle = 1
kit.continuous_servo[1].throttle = -1
kit.continuous_servo[1].throttle = 0

# ACTIVATE servo on channel 0 to its 180 deg setting...
kit.servo[0].angle = 180
# ACTIVATE motor on channel 1 to 100% ?...
kit.continuous_servo[1].throttle = 1
# PAUSE 1 second...
time.sleep(1)

# ACTIVATE servo on channel 0 to it 0 deg setting...
kit.servo[0].angle = 0
# ACTIVATE motor on channel 1 to 0%...
kit.continuous_servo[1].throttle = 0
# PAUSE 1 second...
time.sleep(1)



