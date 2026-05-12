from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.types import Message

from Pbxbot.functions.utility import Gcast

from . import HelpMenu, handler, Pbxbot, on_message

gcast = Gcast()


@on_message("gcast", allow_stan=True)
async def broadcast(client: Client, message: Message):

    if not message.reply_to_message:
        return await message.reply_text(
            f"Reply to a message with {handler}gcast <all/groups/users>"
        )

    if len(message.command) < 2:
        return await message.reply_text("Specify target!")

    mode = message.command[1].lower()

    if mode not in ["all", "groups", "users"]:
        return await message.reply_text("Invalid target!")

    # False = send as copy (without forward tag)
    tag = False

    Pbx = await message.reply_text("Processing...")

    try:
        msg = await gcast.start(
            message.reply_to_message,
            client,
            mode,
            tag
        )

        if msg:
            await Pbx.edit(msg[1])
        else:
            await Pbx.edit("No chats found.")

    except Exception as e:
        await Pbx.edit(f"Error:\n`{e}`")
        print(e)

HelpMenu("gcast").add(
    "gcast",
    "<target> <copy>",
    "Broadcast the replied message to selected target. If 'copy' is also passed the gcast will be without forward tag. Bydefault gcast is done with a forward tag.",
    "gcast groups copy",
    "Target: all, groups, users",
).info("Broadcast Module").done()
