from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI_MUSIC import app
from config import BOT_USERNAME
from SONALI_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
<u>❃ ᴡєʟᴄσϻє ᴛᴏ ⎯⁠⁠⁠⁠‌⎯⁠⁠⁠‌ 𝚂꯭‌𝚙꯭‌𝚊꯭‌𝚛꯭‌𝚜꯭‌𝚑꯭‌𝅃⁠⁠⁠ꀭ꯭‧₊꯭♡゙꯭꯬ #Destiny ʀєᴘσs ❃</u>
 
✼ ʀєᴘᴏ ɪs ηᴏᴡ ᴘʀɪᴠᴧᴛє ᴅᴜᴅє 😌
 
❉  ʏᴏᴜ ᴄᴧη мʏ ᴜsє ᴘᴜʙʟɪᴄ ʀєᴘσs !!  

✼ || [⎯⁠⁠⁠⁠‌⎯⁠⁠⁠‌ 𝚂꯭‌𝚙꯭‌𝚊꯭‌𝚛꯭‌𝚜꯭‌𝚑꯭‌𝅃⁠⁠⁠ꀭ꯭‧₊꯭♡゙꯭꯬ #Destiny](https://t.me/oye_sparsh_baby) ||
 
❊ ʀᴜη 24x7 ʟᴧɢ ϝʀєє ᴡɪᴛʜσᴜᴛ sᴛσᴘ**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴧᴅᴅ ϻє вᴧʙʏ ✙", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜєʟᴘ •", url="https://t.me/oye_Sparsh_baby"),
          InlineKeyboardButton("• 𝛅ᴜᴘᴘσʀᴛ •", url="https://t.me/+Y8qbKGRU2Dg1MzU0"),
          ],
[
InlineKeyboardButton("• ϻᴧɪη ʙσᴛ •", url=f"https://t.me/auramusicprobot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/adh8ul.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
