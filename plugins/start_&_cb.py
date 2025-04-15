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
import random, asyncio, datetime, pytz, time, psutil, shutil

# pyrogram imports
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.enums import ParseMode

# bots imports
from helper.database import digital_botz
from config import Config, rkn
from helper.utils import humanbytes
from plugins import __version__ as _bot_version_, __developer__, __database__, __library__, __language__, __programer__

upgrade_button = InlineKeyboardMarkup([[        
        InlineKeyboardButton('buy premium ✓', user_id=int(6705898491)),
         ],[
        InlineKeyboardButton("Bᴀᴄᴋ", callback_data = "start")
]])

upgrade_trial_button = InlineKeyboardMarkup([[        
        InlineKeyboardButton('buy premium ✓', user_id=int(6705898491)),
         ],[
        InlineKeyboardButton("ᴛʀɪᴀʟ - 𝟷𝟸 ʜᴏᴜʀs ✓", callback_data = "give_trial"),
        InlineKeyboardButton("Bᴀᴄᴋ", callback_data = "start")
]])


        
@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    start_button = [[        
        InlineKeyboardButton('Mis à jour', url='https://t.me/BotZFlix'),
        InlineKeyboardButton('Support', url='https://t.me/BotZFlixSupport')
        ],[
        InlineKeyboardButton('À propos', callback_data='about'),
        InlineKeyboardButton('Aide', callback_data='help')       
         ]]
        
    if client.premium:
        start_button.append([InlineKeyboardButton('💸 Upgrade to Premium 💸', callback_data='upgrade')])

    # ✅ Affiche tous les stickers l’un après l’autre puis les supprime
    stickers = [
        "CAACAgUAAxkBAAIFOGf7e3t7xbexqML4lUBov33y0fwWAALgCAACW_HQVoT7skQi0IBNHgQ",
        "CAACAgUAAxkBAAIFPGf7e32N9GQtxFUBhRpnBcdq-n2VAAIUCwACrZTRViZ7bFXnR26eHgQ",
        "CAACAgUAAxkBAAIFQGf7e4BWBoddo5yVau4uEnW05RtbAAKLCwACwurRVj5eDbteWRIYHgQ",
        "CAACAgUAAxkBAAIFRGf7e4JmicaVg9hMejExAlZj778PAAITCAACVknZVofykXMFYuv7HgQ",
        "CAACAgUAAxkBAAIFSGf7e4UbEvASETSDmY6k-9iSV1gBAAJFCgACTKLRVklE19TmFp_jHgQ"
    ]

    for sticker_id in stickers:
        try:
            s = await client.send_sticker(chat_id=message.chat.id, sticker=sticker_id)
            await asyncio.sleep(1.1)
            await s.delete()
        except:
            pass

    user = message.from_user
    await digital_botz.add_user(client, message) 
    if Config.RKN_PIC:
        await client.send_photo(
            chat_id=message.chat.id,
            photo=Config.RKN_PIC,
            caption=rkn.START_TXT.format(user.mention),
            reply_markup=InlineKeyboardMarkup(start_button),
            parse_mode=ParseMode.HTML
        )
    else:
        await client.send_message(
            chat_id=message.chat.id,
            text=rkn.START_TXT.format(user.mention),
            reply_markup=InlineKeyboardMarkup(start_button),
            disable_web_page_preview=True,
            parse_mode=ParseMode.HTML
        )


@Client.on_message(filters.private & filters.command("myplan"))
async def myplan(client, message):
    if not client.premium:
        return  # ← suis obligée de mettre de le rtrun ou je ne sais quoi

    user_id = message.from_user.id
    user = message.from_user.mention
    
    if await digital_botz.has_premium_access(user_id):
        data = await digital_botz.get_user(user_id)
        expiry_str_in_ist = data.get("expiry_time")
        time_left_str = expiry_str_in_ist - datetime.datetime.now()

        text = f"ᴜꜱᴇʀ :- {user}\nᴜꜱᴇʀ ɪᴅ :- <code>{user_id}</code>\n"

        if client.uploadlimit:
            await digital_botz.reset_uploadlimit_access(user_id)                
            user_data = await digital_botz.get_user_data(user_id)
            limit = user_data.get('uploadlimit', 0)
            used = user_data.get('used_limit', 0)
            remain = int(limit) - int(used)
            type = user_data.get('usertype', "Free")

            text += f"ᴘʟᴀɴ :- `{type}`\nᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ :- `{humanbytes(limit)}`\nᴛᴏᴅᴀʏ ᴜsᴇᴅ :- `{humanbytes(used)}`\nʀᴇᴍᴀɪɴ :- `{humanbytes(remain)}`\n"

        text += f"ᴛɪᴍᴇ ʟᴇꜰᴛ : {time_left_str}\nᴇxᴘɪʀʏ ᴅᴀᴛᴇ : {expiry_str_in_ist}"

        await message.reply_text(text, quote=True)

    else:
        if client.uploadlimit:
            user_data = await digital_botz.get_user_data(user_id)
            limit = user_data.get('uploadlimit', 0)
            used = user_data.get('used_limit', 0)
            remain = int(limit) - int(used)
            type = user_data.get('usertype', "Free")

            text = f"ᴜꜱᴇʀ :- {user}\nᴜꜱᴇʀ ɪᴅ :- <code>{user_id}</code>\nᴘʟᴀɴ :- `{type}`\nᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ :- `{humanbytes(limit)}`\nᴛᴏᴅᴀʏ ᴜsᴇᴅ :- `{humanbytes(used)}`\nʀᴇᴍᴀɪɴ :- `{humanbytes(remain)}`\nᴇxᴘɪʀᴇᴅ ᴅᴀᴛᴇ :- ʟɪғᴇᴛɪᴍᴇ\n\nɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ 👇"

            await message.reply_text(text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💸 ᴄʜᴇᴄᴋᴏᴜᴛ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴꜱ 💸", callback_data='upgrade')]]), quote=True)

        else:
            m=await message.reply_sticker("CAACAgIAAxkBAAIBTGVjQbHuhOiboQsDm35brLGyLQ28AAJ-GgACglXYSXgCrotQHjibHgQ")
            await message.reply_text(f"ʜᴇʏ {user},\n\nʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴀɴʏ ᴀᴄᴛɪᴠᴇ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴs, ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ 👇",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💸 ᴄʜᴇᴄᴋᴏᴜᴛ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴꜱ 💸", callback_data='upgrade')]]))			 
            await asyncio.sleep(2)
            await m.delete()

@Client.on_message(filters.private & filters.command("plans"))
async def plans(client, message):
    if not client.premium:
        return


    user = message.from_user
    upgrade_msg = rkn.UPGRADE_PLAN.format(user.mention) if client.uploadlimit else rkn.UPGRADE_PREMIUM.format(user.mention)
    
    free_trial_status = await digital_botz.get_free_trial_status(user.id)
    if not await digital_botz.has_premium_access(user.id):
        if not free_trial_status:
            await message.reply_text(text=upgrade_msg, reply_markup=upgrade_trial_button, disable_web_page_preview=True)
        else:
            await message.reply_text(text=upgrade_msg, reply_markup=upgrade_button, disable_web_page_preview=True)
    else:
        await message.reply_text(text=upgrade_msg, reply_markup=upgrade_button, disable_web_page_preview=True)
   
  
@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        start_button = [[        
        InlineKeyboardButton('Mis à jour', url='https://t.me/BotZFlix'),
        InlineKeyboardButton('Support', url='https://t.me/BotZFlixSupport')
        ],[
        InlineKeyboardButton('À propos 🗯', callback_data='about'),
        InlineKeyboardButton('Aide 💬', callback_data='help')       
         ]]
            
        if client.premium:
            start_button.append([InlineKeyboardButton('💸 ᴜᴘɢʀᴀᴅᴇ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ 💸', callback_data='upgrade')])
            
        await query.message.edit_text(
            text=rkn.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(start_button))
        
    elif data == "help":
        await query.message.edit_text(
            text=rkn.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("Miniatures🖼", callback_data = "thumbnail"),
                InlineKeyboardButton("Légende📝", callback_data = "caption")
                ],[          
                InlineKeyboardButton("Personnalisée nom de fichier✏️", callback_data = "custom_file_name")    
                ],[          
                InlineKeyboardButton("À propos 💬", callback_data = "about"),
                InlineKeyboardButton("Méta-Données ♾️", callback_data = "digital_meta_data")
                                     ],[
                InlineKeyboardButton("Retour🔙", callback_data = "start")
                  ]]))         
        
    elif data == "about":
        about_button = [[
         #⚠️ don't change source code & source link ⚠️ #
        InlineKeyboardButton("ZFlixTeam", callback_data = "source_code"), #Whoever is deploying this repo is given a warning ⚠️ not to remove this repo link #first & last warning ⚠️
        InlineKeyboardButton("Statut du bot", callback_data = "bot_status")
        ],[
        InlineKeyboardButton("Statut de Vie", callback_data = "live_status")           
        ]]
        if client.premium:
            about_button[-1].append(InlineKeyboardButton("ᴜᴘɢʀᴀᴅᴇ", callback_data = "upgrade"))
            about_button.append([InlineKeyboardButton("Retour🔙", callback_data = "start")])
        else:
            about_button[-1].append(InlineKeyboardButton("Retour🔙", callback_data = "start"))
            
        await query.message.edit_text(
            text=rkn.ABOUT_TXT.format(client.mention, __developer__, __programer__, __library__, __language__, __database__, _bot_version_),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(about_button))    
        
    elif data == "upgrade":
        if not client.premium:
            return await query.message.delete()
                
        user = query.from_user
        upgrade_msg = rkn.UPGRADE_PLAN.format(user.mention) if client.uploadlimit else rkn.UPGRADE_PREMIUM.format(user.mention)
    
        free_trial_status = await digital_botz.get_free_trial_status(query.from_user.id)
        if not await digital_botz.has_premium_access(query.from_user.id):
            if not free_trial_status:
                await query.message.edit_text(text=upgrade_msg, disable_web_page_preview=True, reply_markup=upgrade_trial_button)   
            else:
                await query.message.edit_text(text=upgrade_msg, disable_web_page_preview=True, reply_markup=upgrade_button)
        else:
            await query.message.edit_text(text=upgrade_msg, disable_web_page_preview=True, reply_markup=upgrade_button)
           
    elif data == "give_trial":
        if not client.premium:
            return await query.message.delete()
                
        await query.message.delete()
        free_trial_status = await digital_botz.get_free_trial_status(query.from_user.id)
        if not free_trial_status:            
            await digital_botz.give_free_trail(query.from_user.id)
            new_text = "**ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴛʀɪᴀʟ ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ ғᴏʀ 𝟷𝟸 ʜᴏᴜʀs.\n\nʏᴏᴜ ᴄᴀɴ ᴜsᴇ ꜰʀᴇᴇ ᴛʀᴀɪʟ ꜰᴏʀ 𝟷𝟸 ʜᴏᴜʀs ꜰʀᴏᴍ ɴᴏᴡ 😀\n\nआप अब से 𝟷𝟸 घण्टा के लिए निःशुल्क ट्रायल का उपयोग कर सकते हैं 😀**"
        else:
            new_text = "**🤣 ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ ᴜsᴇᴅ ғʀᴇᴇ ɴᴏᴡ ɴᴏ ᴍᴏʀᴇ ғʀᴇᴇ ᴛʀᴀɪʟ. ᴘʟᴇᴀsᴇ ʙᴜʏ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ʜᴇʀᴇ ᴀʀᴇ ᴏᴜʀ 👉 /plans**"
        await client.send_message(query.from_user.id, text=new_text)

    elif data == "thumbnail":
        await query.message.edit_text(
            text=rkn.THUMBNAIL,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton(" Retour🔙", callback_data = "help")]])) 
      
    elif data == "caption":
        await query.message.edit_text(
            text=rkn.CAPTION,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton(" Retour🔙", callback_data = "help")]])) 
      
    elif data == "custom_file_name":
        await query.message.edit_text(
            text=rkn.CUSTOM_FILE_NAME,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton(" Retour🔙", callback_data = "help")]])) 
      
    elif data == "digital_meta_data":
        await query.message.edit_text(
            text=rkn.DIGITAL_METADATA,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton(" Retour🔙", callback_data = "help")]])) 
      
    elif data == "bot_status":
        total_users = await digital_botz.total_users_count()
        if client.premium:
            total_premium_users = await digital_botz.total_premium_users_count()
        else:
            total_premium_users = "Disabled ✅"
        
        uptime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - client.uptime))    
        sent = humanbytes(psutil.net_io_counters().bytes_sent)
        recv = humanbytes(psutil.net_io_counters().bytes_recv)
        await query.message.edit_text(
            text=rkn.BOT_STATUS.format(uptime, total_users, total_premium_users, sent, recv),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton(" Bᴀᴄᴋ", callback_data = "about")]])) 
      
    elif data == "live_status":
        currentTime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - client.uptime))    
        total, used, free = shutil.disk_usage(".")
        total = humanbytes(total)
        used = humanbytes(used)
        free = humanbytes(free)
        sent = humanbytes(psutil.net_io_counters().bytes_sent)
        recv = humanbytes(psutil.net_io_counters().bytes_recv)
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        await query.message.edit_text(
            text=rkn.LIVE_STATUS.format(currentTime, cpu_usage, ram_usage, total, used, disk_usage, free, sent, recv),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton(" Retour🔙", callback_data = "about")]])) 
      
    elif data == "source_code":
        await query.message.edit_text(
            text=rkn.DEV_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
           #Whoever is deploying this repo is given a warning ⚠️ not to remove this repo link #first & last warning ⚠️   
                InlineKeyboardButton("💞 ZFlix-Team 💞", url="https://t.me/ZFlixTeam")
            ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
                 ]])          
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()

# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
