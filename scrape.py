import os
import discord
import requests

# Required parameters, input your own TOKEN and CHANNEL_ID here
TOKEN = None
CHANNEL_ID = None

# Define the intents for the bot
intents = discord.Intents.default()
intents.message_content = True

# Initialize the Discord client with the specified intents
client = discord.Client(intents=intents)

# Function to download all time images and videos from a Discord channel
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

    # Fetch the channel
    channel = client.get_channel(CHANNEL_ID)

    # Collect the images
    image_urls = []
    async for message in channel.history(limit=None):
        for attachment in message.attachments:
            if attachment.url.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".mov", ".mp4")):
                image_urls.append(attachment.url)

    # Print and download the collected image URLs
    idxImg, idxVid = 1, 1
    for url in image_urls:
        print(url)
        
        img_data = requests.get(url).content
        if url.endswith('.mov') or url.endswith('.mp4'):
            with open(f'video{idxVid}.mov', 'wb') as handler:
                handler.write(img_data)
                idxVid += 1
        else:
            with open(f'image{idxImg}.jpg', 'wb') as handler:
                handler.write(img_data)
                idxImg += 1

    print("Finished downloading all the images")
    
    # Stop the client and exit the program
    await client.close()

# Run the bot
client.run(TOKEN)
