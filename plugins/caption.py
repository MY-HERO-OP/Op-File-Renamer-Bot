from pyrogram import Client, filters 
from helper.database import db

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**__𝐆𝐢𝐯𝐞 𝐦𝐞 𝐚 𝐂𝐚𝐩𝐭𝐢𝐨𝐧 𝐭𝐨 𝐒𝐞𝐭.__\n\n𝐄𝐱𝐚𝐦𝐩𝐥𝐞:- `/set_caption {filename}\n\n💾 Size: {filesize}\n\n⏰ Duration: {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("__**✔️ 𝐘𝐨𝐮𝐫 𝐂𝐚𝐩𝐭𝐢𝐨𝐧 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐒𝐚𝐯𝐞𝐝**__")

    
@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("__**✜ 𝐘𝐨𝐮 𝐃𝐨𝐧𝐭 𝐇𝐚𝐯𝐞 𝐚𝐧𝐲 𝐂𝐚𝐩𝐭𝐢𝐨𝐧**__")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("__**✘ 𝐘𝐨𝐮𝐫 𝐂𝐚𝐩𝐭𝐢𝐨𝐧 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐃𝐞𝐥𝐞𝐭𝐞𝐝**__")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**✜ 𝐘𝐨𝐮𝐫 𝐂𝐚𝐩𝐭𝐢𝐨𝐧:-**\n\n`{caption}`")
    else:
       await message.reply_text("__**✜ 𝐘𝐨𝐮 𝐃𝐨𝐧𝐭 𝐇𝐚𝐯𝐞 𝐚𝐧𝐲 𝐂𝐚𝐩𝐭𝐢𝐨𝐧**__")
