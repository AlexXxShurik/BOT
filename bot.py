import asyncio
import re
from datetime import timedelta

import discord

from DataBase import *
from config import *

caps_list = []
bad_nick = []


class Bot(discord.Client):

    abusive_language = []

    caps_list = []

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        self.abusive_language = getMats()
        self.caps_list = getCapser()
        print(self.caps_list)

    async def on_message(self, ctx):

        abusive_language = getMats()

        # Проверка капса
        if ctx.author == self.user:
            return
        stmbol_caps = 0

        message_lower = re.sub(r'[^\w\s]+|[\d]+', r'', ctx.content).strip().split("http")[0]

        for caps in message_lower:
            if caps.isupper():
                stmbol_caps += 1

        if stmbol_caps/len(message_lower) > 0.4 or ctx.content.upper() == ctx.content and len(message_lower)>3:
            if self.caps_list.count(ctx.author) == 1:
                await ctx.channel.send(f' { ctx.author.mention } { message["kaps2"] }')
                await ctx.author.timeout(timedelta(seconds=60), reason='Забанен за капс')
                print('Писал капсом, чат на минуту: ', ctx.author, ' Ник:', ctx.author.nick, ' Сообщение:', ctx.content)
            elif self.caps_list.count(ctx.author) == 2:
                await ctx.channel.send(f' { ctx.author.mention } { message["kaps3"] }')
                await ctx.author.timeout(timedelta(seconds=300), reason='Забанен за капс')
                print('Писал капсом, чат на 5 мин: ', ctx.author, ' Ник:', ctx.author.nick, ' Сообщение:', ctx.content)
            elif self.caps_list.count(ctx.author) == 3:
                await ctx.channel.send(f' { ctx.author.mention } { message["kaps4"] }')
                await ctx.author.timeout(timedelta(days=1), reason='Забанен за капс')
                print('Писал капсом, чат на день: ', ctx.author, ' Ник:', ctx.author.nick, ' Сообщение:', ctx.content)
            elif self.caps_list.count(ctx.author) > 3:
                await ctx.channel.send(f' { ctx.author.mention } { message["kaps5"] }')
                await asyncio.sleep(5)
                await ctx.author.ban(delete_message_days=1, reason='Забанен за капс')
                print('Писал капсом, забанен: ', ctx.author, ' Ник:', ctx.author.nick, ' Сообщение:', ctx.content)
            else:
                await ctx.channel.send(f' { ctx.author.mention } { message["kaps1"] }')
                print('Писал капсом: ', ctx.author, ' Ник:', ctx.author.nick, ' Сообщение:', ctx.content)
            self.caps_list.append(ctx.author)
            insertCaps(str(ctx.author))
        # Проверка ника на маты
        for mat in abusive_language:
            if mat in str(ctx.author.nick).lower() or ctx.author.nick == None and mat in str(ctx.author).lower():
                await ctx.channel.send(f' { ctx.author.mention } { message["mat_nick"] }')
                print('Мат в нике: ', ctx.author, ' Ник:', ctx.author.nick, ' Мат:', mat)
                await ctx.author.add_roles(discord.utils.get(self.get_guild(230416224629161985).roles, id=893606025264001094))
                await ctx.author.edit(nick='Пища Для Орка')
                break
        # Проверка сообщения на маты
        for mes in re.sub(r'[^\w\s]+|[\d]+', r' ', ctx.content).strip().split():
            if mes.lower() in abusive_language:
                await ctx.channel.send(f' { ctx.author.mention } { message["mat1"] }')
                await ctx.author.timeout(timedelta(minutes=10), reason='Забанен за мат')
                await ctx.delete()
                print('Мат написал: ', ctx.author, ' Ник:', ctx.author.nick, ' Сообщение:', ctx.content)

    async def on_member_update(self, before, after):

        if before.nick != after.nick and after.nick != 'Пища Для Орка':
            for mat in self.abusive_language:
                if mat in str(after.nick).lower() or after.nick == None and mat in str(after).lower():
                    if before.nick == 'Пища Для Орка':
                        await after.send(f' { after.mention } { message["mat_nick_rename"] }')
                    else:
                        await after.send(f' { after.mention } { message["mat_nick"] }')
                    print('Мат в нике: ', after, ' Ник:', after.nick, ' Мат:', mat)
                    await after.add_roles(discord.utils.get(self.get_guild(230416224629161985).roles, id=893606025264001094))
                    await after.edit(nick='Пища Для Орка')
                    break
            if before.nick == 'Пища Для Орка':
                await after.remove_roles(discord.utils.get(self.get_guild(230416224629161985).roles, id=893606025264001094))

client = Bot(intents=discord.Intents.all())
client.run(token)
