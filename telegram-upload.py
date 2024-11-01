import asyncio
import os
import sys

from pyrogram import Client
from pyrogram.types import InputMediaDocument


async def main():
    bot_token = sys.argv[1]
    api_id = 611335
    api_hash = "d524b414d21f4d37f08684c1df41ac9c"
    bot = Client("client", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
    async with bot:
        roaming_ver = os.environ["BiliM_LATEST_TAG"]
        bili_ver = os.environ["Bili_PLAY_VER"]
        msg_p1 = "<b>BiliM-Release</b>"
        msg_p2 = "New release to GitHub!"
        msg_p3 = f"<pre>Bilibili-Play: v{bili_ver}\nBiliRoamingM: v{roaming_ver}</pre>"
        msg_p4 = f'<a href="https://github.com/sakarie9/BiliRoamingM-PreBuilds/releases/tag/v{bili_ver}-{roaming_ver}">Github Releases</a>'
        caption = "{}\n{}\n{}\n\n{}".format(msg_p1, msg_p2, msg_p3, msg_p4)

        dev = InputMediaDocument(
            media=os.environ["BiliM_PLAY_PATCHED_PATH"], caption=caption
        )
        await bot.send_media_group(
            chat_id="@bilim_builds",
            media=[dev],
        )


async def wait():
    try:
        await asyncio.wait_for(main(), timeout=600)
    except asyncio.TimeoutError:
        print("message send timeout!!!")
        exit(1)


asyncio.run(wait())
