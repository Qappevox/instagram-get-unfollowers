# instagram-get-unfollowers
# "You can run this code after copying the div tag included in the _aano class and pasting it into the html body."

This Python script allows you to find your Instagram unfollowers by comparing your followers list with your following list.

Requirements:

Python 3.x
An active Instagram account
Chrome or Firefox browser
Internet connection
Instructions:

Open your Instagram profile in a browser and navigate to the "Followers" and "Following" pages.
Scroll down the page until all followers/following users are loaded.
Right-click on the page and select "Save Page As" to save the HTML file for each page to your local directory.
Run the Python script in the same directory where the HTML files were saved.
The script will automatically parse the HTML files and create two separate text files for your followers and following users.
The script will then compare the two files and create a third text file containing the list of unfollowers.
Note: It is recommended to run this script after a few days of following new users, as the list of unfollowers may not be accurate immediately after following new users.

Usage:

Open the terminal/command prompt in the directory where the script is located.
Type "python InstagramUnfollowersFinder.py" and hit Enter.
Wait for the script to finish running.
Open the "unfollowers.txt" file to see the list of users who unfollowed you.
