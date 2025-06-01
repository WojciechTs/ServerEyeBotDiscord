from datetime import datetime
from discord.ext import commands
from database import insert_one

class voice_listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        before = before.channel
        guild = None
        if before is not None:
            guild = before.guild.id
            before = before.id

        after = after.channel
        if after is not None:
            guild = after.guild.id
            after = after.id
        date = datetime.now()

        if before is None:
            data = {"member": member, "date": date, "tag": "join"}
            insert_one(guild,after,data)
        elif after is None:
            data = {"member": member, "date": date, "tag": "exit"}
            insert_one(guild, before, data)
        elif before is not None and after is not None:
            data = {"member": member, "date": date, "tag": "exit"}
            insert_one(guild, before, data)
            data = {"member": member, "date": date, "tag": "join"}
            insert_one(guild, after, data)



async def setup(bot):
    await bot.add_cog(voice_listener(bot))