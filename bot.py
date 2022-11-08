import asyncio
import re
from datetime import timedelta

import discord
from config import *

caps_list = []


class Bot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, ctx):
        if ctx.author == self.user:
            return
        if ctx.content.upper() == ctx.content and len(re.sub(r'[^\w\s]+|[\d]+', r'', ctx.content).strip())>2:
            if caps_list.count(ctx.author) == 1:
                await ctx.channel.send(f' { ctx.author.mention } { message["kaps2"] }')
                await ctx.author.timeout(timedelta(seconds=60), reason='Забанен за капс')
            elif caps_list.count(ctx.author) == 2:
                await ctx.channel.send(f' { ctx.author.mention } { message["kaps3"] }')
                await ctx.author.timeout(timedelta(seconds=300), reason='Забанен за капс')
            elif caps_list.count(ctx.author) == 3:
                await ctx.channel.send(f' { ctx.author.mention } { message["kaps4"] }')
                await ctx.author.timeout(timedelta(days=1), reason='Забанен за капс')
            elif caps_list.count(ctx.author) > 3:
                await ctx.channel.send(f' { ctx.author.mention } { message["kaps5"] }')
                await asyncio.sleep(5)
                await ctx.author.ban(delete_message_days=1, reason='Забанен за капс')
            else:
                await ctx.channel.send(f' { ctx.author.mention } { message["kaps1"] }')
            caps_list.append(ctx.author)
        for mat in abusive_language:
            if mat in str(ctx.author.nick).lower():
                await ctx.channel.send(f' { ctx.author.mention } { message["mat_nick"] } "{ mat }"')
                break

client = Bot(intents=discord.Intents.all())
client.run(token)

# await ctx.author.ban(delete_message_days=1, reason='Забанен за капс')
# await asyncio.sleep(5)
# await ctx.author.unban()
