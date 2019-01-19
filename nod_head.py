import anki_vector
import time

def main():
    args = anki_vector.util.parse_command_args()

    with anki_vector.Robot(args.serial) as robot:
        for i in range(4):
            while robot.head_angle_rad > -0.3:
                robot.motors.set_head_motor(-1.0)
            while robot.head_angle_rad < 0.7:
                robot.motors.set_head_motor(1.0)

        robot.motors.set_head_motor(0)

        anki_vector.Robot.behavior.set_head_angle

if __name__ == "__main__":
    main()