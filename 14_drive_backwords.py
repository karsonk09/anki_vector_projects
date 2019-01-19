import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps

def main():
    args = anki_vector.util.parse_command_args()

    with anki_vector.Robot(args.serial) as robot:
        robot.behavior.drive_off_charger()

        print("Drive Backwards")
        robot.behavior.drive_straight(distance_mm(-200), speed_mmps(50))

if __name__ == "__main__":
    main()