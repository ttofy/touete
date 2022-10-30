from jepthon import jepiq
import telethon
from telethon.tl.functions.messages import ImportChatInviteRequest
from sessoin import *
from telethon import events
import asyncio



@jepiq.on(events.NewMessage(outgoing=True, pattern=r"\.وعد"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit(waad)
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


@jepiq.on(events.NewMessage(outgoing=True, pattern=r"\.كلمات وعد (.*)"))
async def _(event):
    if ispay[0] == "yes":
        for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
            if ispay[0] == 'yes':
                break
            chat = event.chat_id
            await jepiq.send_message(chat, 'كلمات')
            await asyncio.sleep(0.5)
            masg = await jepiq.get_messages(chat, limit=1)
            masg = masg[0].message
            masg = ("".join(masg.split(maxsplit=3)[3:])).split(" ", 2)
            if len(masg) == 2:
                msg = masg[0]
                await jepiq.send_message(chat, msg)
            else:
                msg = masg[0] + " " + masg[1]
                await jepiq.send_message(chat, msg)
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")

# ↢ ()


@jepiq.on(events.NewMessage(outgoing=True, pattern=r"\.استثمار وعد (.*)"))
async def _(event):
    if ispay[0] == "yes":
        for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
            if ispay[0] == 'yes':
                break
            chat = event.chat_id
            await jepiq.send_message(chat, 'فلوسي')
            await asyncio.sleep(0.5)
            masg = await jepiq.get_messages(chat, limit=1)
            masg = masg[0].message
            masg = ("".join(masg.split(maxsplit=2)[2:])).split(" ", 2)
            msg = masg[0]
            if int(msg) > 500000000:
                await jepiq.send_message(chat, f"استثمار {msg}")
                await asyncio.sleep(10)
                mssag2 = await jepiq.get_messages(chat, limit=1)
                await mssag2[0].click(text="اي ✅")
            else:
                await jepiq.send_message(chat, f"استثمار {msg}")
            await asyncio.sleep(1210)

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
