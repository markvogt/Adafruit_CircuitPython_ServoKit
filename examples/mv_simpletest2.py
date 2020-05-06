# SIMPLETEST2
# MARK VOGT 2020 05 01 
# Simple test for a standard servo on channel 0 and an ESC-controlled brushless motor on channel 1 using Adafruit ServoKit python module...
# It also loops both a motor or "continously-rotating servo" AND a position-holding servo over a range of motion a few times...

# IMPORT python modules required by code...
import time
from adafruit_servokit import ServoKit

# SET channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

# INITIALIZE the ESC...
print("INITIALIZING motor...")
kit.continuous_servo[1].throttle = 1
time.sleep(2)
kit.continuous_servo[1].throttle = -1
time.sleep(2)

print("STEPPING MOTOR SPEED and a SERVO ANGLE up & down a few times...   ")
for i in  range(0,2,1):
    print("i = " + str(i))
    #while True: 
    for j in range(0, 10,1):
        # SEND an incremental THROTTLE CHANGE command...
        print("  j = " + str(j))
        kit.continuous_servo[1].throttle = j/10
        # SEND an incremental SERVO CHANGE command...
        kit.servo[0].angle = j*9
        # CONTINUE at this speed by using SLEEP for 5 secs...
        time.sleep(1)

    for j in range(10, 0,-1):
        # SEND a THROTTLE command...
        print("  j = " + str(j))
        kit.continuous_servo[1].throttle = j/10
        # SEND an incremental SERVO CHANGE command...
        kit.servo[0].angle = j*9
        # CONTINUE at this speed by using SLEEP for 5 secs...
        time.sleep(1)

    i = i + 1
    print("")

print("STOPPING motor...")
kit.continuous_servo[1].throttle = -1
