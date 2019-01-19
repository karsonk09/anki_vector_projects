#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Hello World - Text Version

Make Vector say 'Hello World' in text via ImageDraw.
"""
import anki_vector
import sys
import time

from anki_vector.util import degrees

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Cannot import from PIL. Do `pip3 install --user Pillow` to install")


def make_text_image(text_to_draw, x, y, font=None):
    '''Make a PIL.Image with the given text printed on it

   Args:
       text_to_draw (string): the text to draw to the image
       x (int): x pixel location
       y (int): y pixel location
       font (PIL.ImageFont): the font to use

   Returns:
       :class:(`PIL.Image.Image`): a PIL image with the text drawn on it
   '''
    dimensions = (184, 96)

    # make a blank image for the text, initialized to opaque black
    text_image = Image.new(
        'RGBA', dimensions, (0, 0, 0, 255))

    # get a drawing context
    dc = ImageDraw.Draw(text_image)

    # draw the text
    dc.text((x, y), text_to_draw, fill=(255, 255, 255, 255), font=font)

    return text_image


# Get font file from computer (change directory as needed)
try:
    font_file = ImageFont.truetype("arial.ttf", 20)
except IOError:
    try:
        font_file = ImageFont.truetype(
            "/usr/share/fonts/noto/NotoSans-Medium.ttf", 20)
    except IOError:
        pass

args = anki_vector.util.parse_command_args()

with anki_vector.Robot(args.serial) as robot:
    # Set text to create image from here
    text_to_draw = str(robot.touch.last_sensor_reading.raw_touch_value)
    face_image = make_text_image(text_to_draw, 0, 0, font_file)

    # If necessary, Move Vector's Head and Lift to make it easy to see his face
    robot.behavior.set_head_angle(degrees(45.0))
    robot.behavior.set_lift_height(0.0)

    # Convert the image to the format used by the Screen
    print("Display image on Vector's face...")
    screen_data = anki_vector.screen.convert_image_to_screen_data(
        face_image)
    robot.screen.set_screen_with_image_data(
        screen_data, 5.0, interrupt_running=True)
    time.sleep(5)