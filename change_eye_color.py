import anki_vector
import time

def main():
    args = anki_vector.util.parse_command_args()

    with anki_vector.Robot(args.serial) as robot:
        for i in range(10):
            for j in range(100):
                robot.behavior.set_eye_color(hue = j/100.0, saturation = 0.99)
                time.sleep(0.01)

if __name__ == "__main__":
    main()