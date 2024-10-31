import discord
from discord.ext import commands
import requests
import os

token = os.environ.get("BOT_TOKEN")
prefix = os.environ.get("BOT_PREFIX")

@client.event
async def on_ready():
    print("Logged in as {0.user} ".format(client)) 
                      
client.run(token)    
                            
                            
                            
