# K: Keyboard Buttons

from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup


def gen_keyboard(collection: list, row: int = 2) -> list[list[KeyboardButton]]:
    keyboard = []
    for i in range(0, len(collection), row):
        kyb = []
        for x in collection[i : i + row]:
            kyb.append(KeyboardButton(x))
        keyboard.append(kyb)
    return keyboard


def session_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [
                KeyboardButton("ᴀᴅᴅ ɴᴇᴡ sᴇssɪᴏɴ 📟")
            ],
            [
                KeyboardButton("ᴍᴀɴᴜᴀʟ sᴇssɪᴏɴ 📰"),
                KeyboardButton("ᴅᴇʟᴇᴛᴇ 🚫"),
            ],
            [
                KeyboardButton("ʟɪsᴛ 🪧"),
                KeyboardButton("ʜᴏᴍᴇ 📲"),
            ]
        ],
        resize_keyboard=True,
    )


def start_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [
                KeyboardButton("📳 sᴇssɪᴏɴ"),
                KeyboardButton(" ғᴏʀᴄᴇ sᴜʙ✨"),
            ],
            [
                KeyboardButton("🧑‍🤝‍🧑 ᴜsᴇʀs"),
                KeyboardButton("ᴏᴛʜᴇʀs 🛒"),
            ],
        ],
        resize_keyboard=True,
    )
