import logging
import os
import re
import traceback
from datetime import datetime, timedelta, timezone

import discord
from discord.ext import commands

logging.basicConfig(level=logging.INFO)

utc = timezone.utc
jst = timezone(timedelta(hours=9), "Asia/Tokyo")

token = os.environ["DISCORD_BOT_TOKEN"]

discord.http.API_VERSION = 9


class MyBot(commands.Bot):
    def __init__(self, command_prefix="//", **options):
        super().__init__(command_prefix, **options)
        self.persistent_views_added = False

    async def on_ready(self):
        if self.persistent_views_added is False:
            # self.add_view()
            print("set persistent Views.")
        print("------------------------------------------------------")
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------------------------------------------------------")
        now = datetime.utcnow().astimezone(jst)
        print(
            f"起動完了({now.astimezone(jst).strftime('%m/%d %H:%M:%S')})\nBot ID:{self.user.id}"
        )


bot = MyBot()

if __name__ == "__main__":
    bot.run(token)
