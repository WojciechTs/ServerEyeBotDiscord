from datetime import datetime
from discord.ext import commands
from database import insert_one


class setup_server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="setup")
    @commands.guild_only()
    async def setup(self,ctx: commands.Context):
        guild = ctx.guild
        data = {"name": guild.name, "id": guild.id, "members": [member.id for member in guild.members],
                "text": [text.id for text in guild.text_channels],
                "voice": [voice.id for voice in guild.voice_channels],
                "memeber_count": len(guild.members), "date": datetime.now(), "created": guild.created_at}
        insert_one(guild.id, "info", data)
        for memberi in guild.members:
            member = guild.get_member(memberi.id)
            image = member.display_avatar.url
            data = {"name": member.name, "nick": member.nick, "id": member.id, "image": str(image),
                    "join": member.joined_at}
            insert_one(guild.id, "members", data)
        for text in guild.text_channels:
            data = {"name": text.name, "id": text.id, "created": text.created_at, "image": "text.png"}
            insert_one(guild.id, "texts", data)
        for voice in guild.voice_channels:
            data = {"name": voice.name, "id": voice.id, "created": voice.created_at, "image": "voice.png"}
            insert_one(guild.id, "voices", data)
        await ctx.send(f"Done")

async def setup(bot):
    await bot.add_cog(setup_server(bot))