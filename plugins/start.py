from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
import random
from helper.txt import mr
from helper.database import db
from config import START_PIC, FLOOD, ADMIN 


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id)             
    txt=f"HEY 🦋 {user.mention} \n I Am Simply File Rename+File To Video Converter Bot With Permanent Thumbnail & Custom Caption Support!"
    button=InlineKeyboardMarkup([[
        InlineKeyboardButton("𝐂𝐨𝐧𝐭𝐚𝐜𝐭", callback_data='dev')
        ],[
        InlineKeyboardButton('✜ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬', url='https://t.me/Opleech'),
        InlineKeyboardButton('✜ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭', url='https://t.me/WD_Topic_Group')
        ],[
        InlineKeyboardButton('✜ 𝐀𝐛𝐨𝐮𝐭', callback_data='about'),
        InlineKeyboardButton('✜ 𝐇𝐞𝐥𝐩', callback_data='help')
        ]])
    if START_PIC:
        await message.reply_photo(START_PIC, caption=txt, reply_markup=button)       
    else:
        await message.reply_text(text=txt, reply_markup=button, disable_web_page_preview=True)
    

@Client.on_message(filters.command('logs') & filters.user(ADMIN))
async def log_file(client, message):
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply_text(f"Error:\n`{e}`")

@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 𝐒𝐭𝐚𝐫𝐭 𝐑𝐞𝐧𝐚𝐦𝐞 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✘ 𝐂𝐚𝐧𝐜𝐞𝐥 ✘", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 𝐒𝐭𝐚𝐫𝐭 𝐑𝐞𝐧𝐚𝐦𝐞 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✘ 𝐂𝐚𝐧𝐜𝐞𝐥 ✘", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""HEY 🦋 {query.from_user.mention} \nI Am Simply File Rename+File To Video Converter Bot With Permanent Thumbnail & Custom Caption Support! """,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("𝐂𝐨𝐧𝐭𝐚𝐜𝐭", callback_data='dev')                
                ],[
                InlineKeyboardButton('✜ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬', url='https://t.me/Opleech'),
                InlineKeyboardButton('✜ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭', url='https://t.me/WD_Topic_Group')
                ],[
                InlineKeyboardButton('✜ 𝐀𝐛𝐨𝐮𝐭', callback_data='about'),
                InlineKeyboardButton('✜ 𝐇𝐞𝐥𝐩', callback_data='help')
                ]]
                )
            )
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change Contact code & Contact link ⚠️ #
               InlineKeyboardButton("⫷◆𝐁𝐚𝐜𝐤", callback_data = "start"),
               InlineKeyboardButton("✘ 𝐂𝐥𝐨𝐬𝐞", callback_data = "close")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change Contact & Contact link ⚠️ #
               InlineKeyboardButton("⫷◆𝐁𝐚𝐜𝐤", callback_data = "start"),
               InlineKeyboardButton("✘ 𝐂𝐥𝐨𝐬𝐞", callback_data = "close")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change Contact & Contact link ⚠️ #
               InlineKeyboardButton("🦋 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 🦋", url="https://t.me/WD_Contact_Bot")
               ],[
               InlineKeyboardButton("⫷◆𝐁𝐚𝐜𝐤", callback_data = "start"),
               InlineKeyboardButton("✘ 𝐂𝐥𝐨𝐬𝐞", callback_data = "close")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()





