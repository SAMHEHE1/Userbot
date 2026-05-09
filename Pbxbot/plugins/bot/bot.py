import heroku3

from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    Message,
)

from Pbxbot import HEROKU_APP
from Pbxbot.core import LOGS
from Pbxbot.functions.tools import restart

from ..btnsG import (
    gen_bot_help_buttons,
    start_button,
)

from . import (
    HELP_MSG,
    START_MSG,
    BotHelp,
    Config,
    Pbxbot,
)


# ─────────────────────────────────────────────
# Start Image
# ─────────────────────────────────────────────

START_IMAGE = "https://files.tgvibes.online/cTfLdOhe.jpg"


# ─────────────────────────────────────────────
# /start
# ─────────────────────────────────────────────

@Pbxbot.bot.on_message(filters.command("start"))
async def start_pm(_, message: Message):

    btns = start_button()

    text = START_MSG.format(
        message.from_user.mention
    )

    try:

        await message.reply_photo(
            photo=START_IMAGE,

            caption=text,

            disable_web_page_preview=True,

            reply_markup=InlineKeyboardMarkup(btns),
        )

    except Exception:

        await message.reply_text(
            text,

            disable_web_page_preview=True,

            reply_markup=InlineKeyboardMarkup(btns),
        )


# ─────────────────────────────────────────────
# /help
# ─────────────────────────────────────────────

@Pbxbot.bot.on_message(filters.command("help"))
async def help_pm(_, message: Message):

    btns = gen_bot_help_buttons()

    await message.reply_text(
        HELP_MSG,

        disable_web_page_preview=True,

        reply_markup=InlineKeyboardMarkup(btns),
    )


# ─────────────────────────────────────────────
# /restart
# ─────────────────────────────────────────────

@Pbxbot.bot.on_message(
    filters.command("restart")
    & Config.AUTH_USERS
)
async def restart_clients(_, message: Message):

    await message.reply_text(
        "🔄 Restarting Bot..."
    )

    try:

        if HEROKU_APP:

            try:

                heroku = heroku3.from_key(
                    Config.HEROKU_APIKEY
                )

                app = heroku.apps()[
                    Config.HEROKU_APPNAME
                ]

                app.restart()

            except Exception:

                await restart()

        else:

            await restart()

    except Exception as e:

        LOGS.error(e)

        await message.reply_text(
            f"❌ Restart failed:\n<code>{e}</code>"
        )


# ─────────────────────────────────────────────
# Help Menu
# ─────────────────────────────────────────────

BotHelp("Others").add(
    "start",
    "To start the bot and get the main menu."
).add(
    "help",
    "To get the help menu with all commands."
).add(
    "restart",
    "To restart the bot."
).info(
    "Basic commands of the bot."
).done()
