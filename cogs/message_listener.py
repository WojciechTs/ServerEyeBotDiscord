from datetime import datetime

import discord
from discord.ext import commands, tasks

from database import insert_one


class message_listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,msg):
        channel = msg.channel.id
        guild = msg.author.guild.id
        member = msg.author.id
        date = datetime.now()
        data = {"member":member,"date":date,"tag":"send"}
        insert_one(guild,channel,data)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        channel = before.channel.id
        guild = before.author.guild.id
        member = before.author.id
        date = datetime.now()
        data = {"member":member,"date":date,"tag":"mod"}
        insert_one(guild,channel,data)

    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        channel = msg.channel.id
        guild = msg.author.guild.id
        member = msg.author.id
        date = datetime.now()
        data = {"member":member,"date":date,"tag":"del"}
        insert_one(guild,channel,data)


async def setup(bot):
    await bot.add_cog(message_listener(bot))