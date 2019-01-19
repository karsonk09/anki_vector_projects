'''
Author: Karson Richardson
Date: 1/19/2019
Version: 1.0

########################################################################################################################
This program is free for personal use. If you wish to use this program for professional or educational purposes. Please
contact me using any of the following information:
Email: richkar1997@gmail.com
Phone: 309-634-9389 (Text message preferred)

If any issues are found within the program please let me know. It is a work in progress and I would love to know about
the issues.
########################################################################################################################

Description
------------------------------------------------------------------------------------------------------------------------
- This is a program for the Anki Vector Robot. This program uses the HTML from the website "http://nfl.com/schedules".
- Using the HTML from nfl.com, the program pulls specific data from the HTML using XPath.
  See how to find the XPath below. After the data is found, Vector will try to speak what the next NFL game is using the
  robot.saytext() function.
------------------------------------------------------------------------------------------------------------------------
How to Find XPath
------------------------------------------------------------------------------------------------------------------------
- The XPath can be found in multiple ways. The simplest, but most inconsistent way of doing it is the following:
    (Google Chrome)
    1. On the webpage of your choice, right click and select "inspect". This will pull up the HTML for the page.
    2. You can scroll through the HTML to find your information or type in your desired information using CTRL+F.
    3. Once you have found what you are looking for, right click and select Copy->Copy XPath.
    4. The XPath will now be copied to your clipboard.
- The alternative method, which yields better and more consistent results (as I have used below) is the following:
    1. On the webpage of your choice, right click and select "inspect". This will pull up the HTML for the page.
    2. You can scroll through the HTML to find your information or type in your desired information using CTRL+F.
    3. Once you have found the HTML you are looking for, inspect it carefully and write a direct XPath to the HTML.
       The HTML will have an element type and a class. Pay close attention to the class of the element

    EXAMPLE) //span[@class="examplespan"]
             //div[@class="examplediv"]
------------------------------------------------------------------------------------------------------------------------
Known Issues
------------------------------------------------------------------------------------------------------------------------
- Program may fail when the schedule changes, which should be able to be patched quite easily
- Issues with pulling the date from the HTML using XPath.
------------------------------------------------------------------------------------------------------------------------
'''
import anki_vector
from lxml import html
import requests

args = anki_vector.util.parse_command_args()
with anki_vector.Robot(args.serial) as robot:

    # Set up a variable for the link to the page
    page = "http://nfl.com/schedules"
    # Establish connection to page
    html_doc = requests.get(page)
    # Pull HTML from page as a string
    tree = html.fromstring(html_doc.content)

    # Get the raw time value and the time of day and concatonate them
    # These are direct XPaths to specific parts of the HTML
    time_value = tree.xpath('//span[@class="time"]/text()')
    time_of_day = tree.xpath('//span[@class="suff"]/span[1]/text()')
    time = time_value[0] + " " + time_of_day[0]

    # Use Xpath to get team names from page
    home_team_name = tree.xpath('//span[@class="team-name home "]/text()')
    away_team_name = tree.xpath('//span[@class="team-name away "]/text()')

    # Have vector tell you what it has found
    robot.say_text("The next NFL game will be at " + time + " and will feature the " +
                    home_team_name[0] + " and the " + away_team_name[0] + ".")

# END PROGRAM