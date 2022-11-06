import discord

config = {
    'token': 'MTAzODg0MjY4NTI0ODc3ODI2MA.GwjFha.HfTe8iwXTYCJAVJqkD1yJAQRKyLpzkpFE2YRII',
    'prefix': 'prefix',
}

class Bot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        print(message)

client = Bot(intents=discord.Intents.all())
client.run('MTAzODg0MjY4NTI0ODc3ODI2MA.GJVu2e.DfpDkK9dJzJtniuL1bBSGZAnGBrjJWDBXH3XA8')
