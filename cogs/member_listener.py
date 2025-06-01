from datetime import datetime
from discord.ext import commands, tasks

from database import insert_one, update_one


class member_listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        guild = member.guild.id
        date = datetime.now()
        data = {"member":member.id,"date":date,"tag":"join"}
        insert_one(guild,"members_log",data)
        data = {"name": member.name, "nick": member.nick, "id": member.id, "image": member.guild_avatar.url, "join": member.joined_at, "left": None}
        insert_one(guild, "members", data)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = member.guild.id
        date = datetime.now()
        data = {"member": member.id, "date": date, "tag": "left"}
        insert_one(guild, "members_log", data)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        member = after
        guild = member.guild.id
        filter = {"id": before.id}
        data = {"name": member.name, "nick": member.nick, "id": member.id, "image": member.guild_avatar.url,
                "join": member.joined_at, "left": None}
        update_one(guild, "members", filter,data)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        date = datetime.now()
        data = {"member": user.id, "date": date, "tag": "ban"}
        insert_one(guild.id, "members_log", data)

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        date = datetime.now()
        data = {"member": user.id, "date": date, "tag": "unban"}
        insert_one(guild.id, "members_log", data)

async def setup(bot):
    await bot.add_cog(member_listener(bot))