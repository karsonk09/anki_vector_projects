'''
Author: Karson Richardson

**** This program is free for personal use, it would be much appreciated if permission was requested from the author
before using this program for professional or educational purposes. Contact the author using the following email:
richkar1997@gmail.com ****

Program Description
------------------------------------------------------------------------------------------------------------------------
This program is intended to allow the user to be able to use the touch sensor on Vector's back to
move the lift up and down. If the user applies pressure to Vector's touch sensor with three fingers, the lift will move
upwards. If the user applies pressure to Vector's touch sensor with two fingers, the lift will maintain its height. If
the user applies pressure to Vector's touch sensor with one finger, the lift will move downwards. If the user has not
touched Vector's back for ten seconds, the program will end.
------------------------------------------------------------------------------------------------------------------------

Raw integer values for the range of the touch sensors
------------------------------------------------------------------------------------------------------------------------
Minimum touch sensor value ~ 4720
Maximum touch sensor value ~ 5000
One finger sensor range: 4780-4850
Two finger sensor range: 4851-4900
Three finger sensor range: 4900+
------------------------------------------------------------------------------------------------------------------------

'''

import anki_vector
import time

args = anki_vector.util.parse_command_args()

with anki_vector.Robot(args.serial) as robot:
    # Reset lift height so that we start at the ground
    robot.behavior.set_lift_height(0.0)

    # Vector introduces the program
    '''robot.say_text("Use my touch sensor to control the height of my lift. Place one finger on my touch sensor to "
                   "lower my lift. Place two fingers on my touch sensor to raise my lift.")'''

    done = False
    while not done:

        while not robot.touch.last_sensor_reading.is_being_touched:
            print("Robot not being touched")
            robot.motors.set_lift_motor(0)

        while robot.touch.last_sensor_reading.is_being_touched:
            # Retrieve the integer value of Vector's last touch reading
            print("Robot being touched")
            touch_value = robot.touch.last_sensor_reading.raw_touch_value
            print("Touch sensor reading: " + str(touch_value))

            # Using the raw sensor values from our data, we set the motor speed to the corresponding values based on
            # how many fingers Vector can feel using his sensors
            if touch_value > 4755 and touch_value <= 4840:
                print("Lowering lift")
                robot.motors.set_lift_motor(-1.0)
            elif touch_value > 4840:
                print("Raising lift")
                robot.motors.set_lift_motor(1.0)