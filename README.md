# Imager
A discord bot that iterates through a specific channel in a discord server and scrapes all the images and videos.

## Installation
Make sure to have the latest version of Python installed and the following dependencies installed in the project folder. Run the specific commands in the terminal for each needed dependency.

Dependencies:
- discord: ``` pip install discord ```
- requests: ``` pip install requests ```

## How to Use
Before cloning this repo, make sure to create a new discord bot in the Discord Developers Portal. This is important for the TOKEN that will be needed to connect the program and the bot together. Next, clone the project folder onto your desktop.
There are two files:
- scrape.py downloads all the images and videos from a specific channel into the project folder
- clean.py deletes all the images and videos that were just downloaded in the project folder

Replace the TOKEN (str) and CHANNEL_ID (int) parameter with your specific parameters in the scrape.py file. The TOKEN is the unique identifier for your bot, which can be found on the Discord Developer Portal under the Bot tab. The CHANNEL_ID can be found by right clicking on a channel (make sure to have Discord Developer activated in settings). To execute the program and run scrape.py, type the following command in the terminal
```
python scrape.py
```

If you want to delete all the images and videos from the current working directory, simply run
```
python clean.py
```