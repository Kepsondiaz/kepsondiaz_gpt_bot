from dotenv import load_dotenv
import discord
import os 


load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client):
    async def on_ready(self):
        print("Connecter avec succée", self.user)
    async def on_message(self, message): 
        print(message.content)
        if message.author == self.user:
            return
        command, user_message = None, None
    
        for text in ['/ai', '/bot', '/chatgpt']:
            if message.content.startswith(text):
                command=message.content.split(' ')[0]
                user_message=message.content.replace(text, '')
                print(command, user_message) 
        if command == '/ai' or command == '/bot' or command 