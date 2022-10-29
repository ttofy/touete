import asyncio
import random
from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from jepthon import jepiq
from ..helpers.utils import reply_id

# الي يخمط ويكول من كتابتي الا امه انيجه وقد اعذر من انذر
@jepiq.on(admin_cmd(pattern="حالتي ?(.*)"))
async def _(event):
    await event.edit("**- يتم التاكد من حالتك اذا كنت محظور او لا**")
    async with bot.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("** اولا الغي حظر @SpamBot وحاول مجددا**")
            return
        await event.edit(f"- {response.message.message}\n @RICKTHON")

#ها
@jepiq.on(events.NewMessage(outgoing= True,pattern=r'^\.تيك'))
async def e(event):
                chat = event.get_chat()
                h = event.text
                mes = h.replace('.تيك ','')
                await event.edit('انتظر...')
                url = f"https://tiktok-best-experience.p.rapidapi.com/user/{mes}"
                headers = {
		"x-rapidapi-key":"d0cbbe1f79mshe3c74080d9d0da5p1de4ddjsn21db44140e77",
		"x-rapidapi-host":"tiktok-best-experience.p.rapidapi.com",
		"User-Agent":"TikTracker/1.2 (com.markuswu.TikTracker; build:1; iOS 14.4.0) Alamofire/5.4.4"
	}
                r = (requests.get(url,headers=headers).json())
                
                if r['status'] == 'ok':
                 
                  insta = ''
                  uid = ''
                  name=''
                  yc=''
                  bio=''
                  h=''
                  fg=''
                  fs=''
                  p= r['data']['avatar_medium']['url_list'][0]
                  try:
                      uid = r["data"]["uid"]
                  except:
                      uid='not found'
                  try:
                      yc = r["data"]["youtube_channel_id"]
                  except:
                      yc='not found'
                  try:
                      h = r["data"]["total_favorited"]
                  except:
                      h='0'
                  try:
                      fg = r["data"]["following_count"]
                  except:
                      fg='0'
                  try:
                      fs = r["data"]["follower_count"]
                  except:
                      fs='0'
                  try:
                      name = r["data"]["nickname"]
                  except:
                      name='not found'
                  try:
                      bio = r["data"]["signature"]
                  except:
                      bio = 'not found'
    
                  try:
                      insta = r["data"]["ins_id"]
                  except:
                      insta = 'not found'
           
                await event.edit(f'''
• Name : {name}

• Followers : {fs}

• Following : {fg}

• Instagram : {insta}

• Youtube Chanel : {yc}

• Likes : {h}

• Bio : {bio}

• iD : {uid}
= = = = = = = = = = = = = = = = = = = = 
By : @P_J_I To : @RICKTHON''')

@jepiq.on(events.NewMessage(outgoing=True, pattern=r'^\.ذكاء'))
async def hne(event):
    chat = await event.get_chat()
    command = event.raw_text.replace('.ذكاء ','')
    
    await event.edit('انتظر...')

    await jepthon.send_file(event.to_id, AiArt(query=command).Generator(),
                           caption=f'Done Art \nArt name : {command}\n\n•••••••••••••••\nBy : @P_J_I , TO @RICKTHON')
    await jepthon.delete_messages(chat, event.message)
@jepiq.on(events.NewMessage(outgoing=True, pattern=r'^\.غرامات'))
async def bi(event):
    await event.edit('انتظر...')
    k = event.raw_text.replace('.غرامات ', '')
    r = k.split(':')[0]
    t = k.split(':')[1]
    n = k.split(':')[2]
    l = k.split(':')[3]
    headers = {
        'authority': 'itp.gov.iq',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'ar;q=0.5',
        'cache-control': 'max-age=0',
        'origin': 'https://itp.gov.iq',
        'referer': 'https://itp.gov.iq/carSearch.php',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36',
    }
    data = {
        'CarLetter': l,
        'CarNumber': n,
        'CarType': t,
        'CarReg': r,
        'submit': 'بحث',
    }
    r = requests.post('https://itp.gov.iq/carSearch.php', headers=headers, data=data)

    if 'لا توجد غرامات مفروضة على المركبة - شكرا لالتزامكم بقواعد السير الامن ' in r.text:
        await event.edit('لا توجد غرامات مفروضة على المركبة - شكرا لالتزامكم بقواعد السير الامن ')
    else:
        suop = BeautifulSoup(r.text, "html.parser")
        m = suop.find_all("table", {"class": "blueTable"})
        for i in m:
            u = (str(i.text).replace('<td>', ''))
            o = str(u.replace('رقم المخالفة', ''))
            ou = str(o.replace('مبلغ المخالفة', ''))
            oo = str(ou.replace('مكان المخالفة', ''))
            uu = str(oo.replace('الوقت', ''))
            await event.edit(uu)



@jepiq.on(admin_cmd(pattern="الاغنية ?(.*)"))
async def _(event):
    "To reverse search music by bot."
    if not event.reply_to_msg_id:
        return await event.edit("**▾∮ يجب الرد على الاغنيه اولا**")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                await event.edit("**▾∮ يتم التعرف على الاغنية انتظر**")
                start_msg = await conv.send_message("/start")
                response = await conv.get_response()
                send_audio = await conv.send_message(reply_message)
                check = await conv.get_response()
                if not check.text.startswith("Audio received"):
                    return await event.edit(
                        "**▾∮ يجب ان يكون حجم الاغنيه من 5 الى 10 ثواني **."
                    )
                await event.edit("- انتظر قليلا")
                result = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("```Mohon buka blokir (@auddbot) dan coba lagi```")
                return
            namem = f"**الأغنية : **{result.text.splitlines()[0]}\
        \n\n**التفاصيـل : **{result.text.splitlines()[2]}"
            await event.edit(namem)
            await event.client.delete_messages(
                conv.chat_id,
                [start_msg.id, send_audio.id, check.id, result.id, response.id],
            )
    except TimeoutError:
        return await event.edit("***حدث خطا ما حاول مجددا**")


@jepiq.on(admin_cmd(pattern="ايميل وهمي(?: |$)(.*)"))
async def _(event):
    chat = "@TempMailBot"
    geez = await event.edit("**جاري انشاء بريد ...**")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=220112646)
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            response = await response
            jepiq = (response).reply_markup.rows[2].buttons[0].url
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await geez.edit("**الغي حظر @TempMailBot  و حاول مجددا**")
            return
        await event.edit(
            f"الايميل الخاص هو `{response.message.message}`\n[ اضغط هنا لرؤية من رسائل الايميل الواردة]({jepthon})"
        )
@jepiq.on(admin_cmd(outgoing=True, pattern="غنيلي$"))
async def jepvois(vois):
  rl = random.randint(3,267)
  url = f"https://t.me/DwDi1/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="᯽︙ BY : @RICKTHON 🎀",parse_mode="html")
  await vois.delete()

@jepiq.on(admin_cmd(outgoing=True, pattern="شعر$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/L1BBBL/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="᯽︙ BY : @RICKTHON 🎀",parse_mode="html")
  await vois.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="قران$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/QuraanJep/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="᯽︙ BY : @RICKTHON 🤲🏻☪️",parse_mode="html")
  await vois.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="ثيم$"))
async def jepThe(theme):
  rl = random.randint(2,510)
  url = f"https://t.me/GSSSD/{rl}"
  await theme.client.send_file(theme.chat_id,url,caption="᯽︙ THEME BY : @RICKTHON 🎊",parse_mode="html")
  await theme.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="لاتغلط$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/4"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="بجيت$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/5"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="نشاقة$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/3"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="احب الله$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/2"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="روح$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/6"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="انمي1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/7"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="انمي2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/9"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="انمي3$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/11"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="انمي4$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/12"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="انمي5$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/13"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="انمي6$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/14"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="انمي7$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/15"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="انمي8$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/16"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="انمي9$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/17"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="انمي10$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/18"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="زيج2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/19"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@jepiq.on(admin_cmd(outgoing=True, pattern="زيج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/20"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
