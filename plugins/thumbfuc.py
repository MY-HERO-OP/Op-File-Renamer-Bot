from pyrogram import Client, filters
from helper.database import db

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client, message):    
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(
	   chat_id=message.chat.id, 
	   photo=thumb)
    else:
        await message.reply_text("✜ __**𝐘𝐨𝐮 𝐃𝐨𝐧𝐭 𝐇𝐚𝐯𝐞 𝐚𝐧𝐲 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐥𝐬**__") 
		
@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client, message):
    await db.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("✘ __**𝐘𝐨𝐮𝐫 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐥𝐬 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐃𝐞𝐥𝐞𝐭𝐞𝐝**__")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    mkn = await message.reply_text("𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭◉◉◉")
    await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await mkn.edit("✔️ __**✜ 𝐘𝐨𝐮𝐫 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐥𝐬 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐒𝐚𝐯𝐞𝐝**__")
	
