from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.utils import not_subscribed 

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="✜ 𝐉𝐨𝐢𝐧 𝐔𝐩𝐃𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ✜", url=client.invitelink) ]]
    text = "**𝐒𝐨𝐫𝐫𝐲 𝐃𝐮𝐝𝐞 𝐲𝐨𝐮𝐫 𝐍𝐨𝐭 𝐉𝐨𝐢𝐧𝐝 𝐌𝐲 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 🦋 𝐏𝐥𝐞𝐚𝐬𝐞 𝐉𝐨𝐢𝐧 𝐌𝐲 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐓𝐨 𝐔𝐬𝐞 𝐁𝐨𝐭 𝐓𝐡𝐚𝐧𝐤 𝐘𝐨𝐮..**"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          



