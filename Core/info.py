import json
import os

import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        path = os.path.join(os.path.dirname(__file__), r"../ext.json")
        with open(path, mode="r") as f:
            d = json.load(f)
        self.guilds = [v for k, v in d["guild"].items()]
        # print(self.guilds)

    @commands.slash_command(guild_ids=[self.guilds], name="user")
    @commands.has_role()
    async def _user(self):
        pass


def setup(bot):
    return bot.add_cog(Info(bot))
