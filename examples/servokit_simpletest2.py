# SIMPLETEST2
# MARK VOGT 2020 05 01 
# Simple test for a standard servo on channel 0 and an ESC-controlled brushless motor on channel 1 using Adafruit ServoKit python module...

# IMPORT python modules required by code...
import time
from adafruit_servokit import ServoKit

# SET channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

# while True:
#     # SEND a FULL THROTTLE command...
#     kit.continuous_servo[1].throttle = 1
#     # CONTINUE at this speed by using SLEEP for 5 secs...
#     time.sleep(5)

#     # SEND a HALF THROTTLE command (NOT actually "zero")...
#     kit.continuous_servo[1].throttle = .5
#     time.sleep(5)

#     # SEND a SLOWEST THROTTLE command (NOT actually "zero")...
#     kit.continuous_servo[1].throttle = 0
#     time.sleep(5)

#     # SEND STOP MOTOR command...
#     kit.continuous_servo[1].throttle = -1
#     time.sleep(5)

while True: 
    for i in range(0, 10,1):
        # SEND a FULL THROTTLE command...
        kit.continuous_servo[1].throttle = i/10
        # CONTINUE at this speed by using SLEEP for 5 secs...
        time.sleep(1)

    for i in range(10, 0,-1):
        # SEND a FULL THROTTLE command...
        kit.continuous_servo[1].throttle = i/10
        # CONTINUE at this speed by using SLEEP for 5 secs...
        time.sleep(1)



# ACTIVATE servo on channel 0 to its 180 deg setting...
# kit.servo[0].angle = 180
# ACTIVATE motor on channel 1 to 100% ?...
# kit.continuous_servo[1].throttle = .1
# PAUSE 1 second...
# time.sleep(1)

# ACTIVATE servo on channel 0 to it 0 deg setting...
#kit.servo[0].angle = 0
# ACTIVATE motor on channel 1 to 0%...
# kit.continuous_servo[1].throttle = 0