# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Special Thanks To @ReshamOwner
# Update Channel @Digital_Botz & @DigitalBotz_Support
"""
Apache License 2.0
Copyright (c) 2022 @Digital_Botz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Telegram Link : https://t.me/Digital_Botz 
Repo Link : https://github.com/DigitalBotz/Digital-Rename-Bot
License Link : https://github.com/DigitalBotz/Digital-Rename-Bot/blob/main/LICENSE
"""

# extra imports
import aiohttp, asyncio, warnings, pytz, datetime
import logging
import logging.config
import glob, sys, pyromod
from pathlib import Path
import importlib.util as import_utils

# pyrogram imports
import pyrogram.utils
from pyrogram import Client, __version__, errors
from pyrogram.raw.all import layer

# bots imports
from config import Config
from plugins.web_support import web_server
from plugins.file_rename import app

pyrogram.utils.MIN_CHANNEL_ID = -1009999999999

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler('BotLog.txt'),
             logging.StreamHandler()]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class DigitalRenameBot(Client):
    def __init__(self):
        super().__init__(
            name="DigitalRenameBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15)

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username
        self.uptime = Config.BOT_UPTIME
        self.premium = Config.PREMIUM_MODE
        self.uploadlimit = Config.UPLOAD_LIMIT_MODE

        app = aiohttp.web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await aiohttp.web.TCPSite(app, bind_address, Config.PORT).start()

        path = "plugins/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as a:
                patt = Path(a.name)
                plugin_name = patt.stem.replace(".py", "")
                plugins_path = Path(f"plugins/{plugin_name}.py")
                import_path = "plugins.{}".format(plugin_name)
                spec = import_utils.spec_from_file_location(import_path, plugins_path)
                load = import_utils.module_from_spec(spec)
                spec.loader.exec_module(load)
                sys.modules["plugins" + plugin_name] = load
                print("Digital Botz Imported " + plugin_name)

        print(f"{me.first_name} Iᵀ Sᴅᵀʀᴛᴇᴅ.....✨️")

        for id in Config.ADMIN:
            try:
                msg = (f"𝟮𝗚𝗕+ ғɪʟᴇ sᴜᴘᴘᴏʀᴛ ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ ᴛᴏ ʏᴏᴜʀ ʙᴏᴛ.\n\nNote: 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐩𝐫𝐞𝐦𝐢𝐮𝐦 𝐚𝐜𝐜𝐨𝐮𝐧𝐭 𝐬𝐭𝐫𝐢𝐧𝐠 𝐬𝐞𝐬𝐬𝐢𝐨𝐧 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝.\n\n**__{me.first_name}  Iᵀ Sᴅᵀʀᴛᴇᴅ.....✨️__**")
                await self.send_message(id, msg)
            except:
                pass

        if Config.LOG_CHANNEL:
            try:
                curr = datetime.datetime.now(pytz.timezone("Africa/Lome"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                log_msg = (f"**__{me.mention} Iᵀ Rᴇsᴛᴀʀᴛᴇᴅ !!**\n\n"
                           f"🗓 Dᴀᴛᴇ : `{date}`\n"
                           f"⏰ Tᴇɪᴍᴇ : `{time}`\n"
                           f"🌐 Tᴇᴛʟᴇᴏᴚᴏɴᴇ : `Asia/Kolkata`\n\n"
                           f"🅐 Vᴇʀsɪᴏɴ : `v{__version__} (Layer {layer})`</b>")
                await self.send_message(Config.LOG_CHANNEL, log_msg)
            except:
                print("Please make sure the bot is admin in the log channel.")

    async def stop(self, *args):
        for id in Config.ADMIN:
            try:
                await self.send_message(id, f"**Bot Stopped....**")
            except:
                pass
        print("Bot Stopped 🙄")
        await super().stop()

bot_instance = DigitalRenameBot()

def main():
    async def start_services():
        if Config.STRING_SESSION:
            await asyncio.gather(
                app.start(),
                bot_instance.start()
            )
        else:
            await asyncio.gather(bot_instance.start())

    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_services())
    loop.run_forever()

if __name__ == "__main__":
    warnings.filterwarnings("ignore", message="There is no current event loop")
    try:
        main()
    except errors.FloodWait as ft:
        print(f"Flood Wait Occurred, Sleeping For {ft}")
        asyncio.sleep(ft.value)
        print("Now Ready For Deploying !")
        main()
