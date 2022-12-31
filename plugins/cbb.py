# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de
# Recode now By @thisrama
# t.me/ramsupportt & t.me/userbotch
# t.me/HyperSupportQ & t.me/storyQi

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>Informasi.\n\n • OWNER REPO : @excute7\n • CHANNEL : <a href='https://t.me/storyQi'>JOIN</a>\n • GROUP : <a href='https://t.me/HyperSupportQ'>JOIN</a>\n\n Support @ProjectHyper</b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴜᴛᴜᴘ •", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
