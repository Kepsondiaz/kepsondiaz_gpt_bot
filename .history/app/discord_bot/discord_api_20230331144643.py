from dotenv import load_dotenv
import discord
import os 


load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")

def MyClient(discord.Client)