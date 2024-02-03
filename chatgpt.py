
#-----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
from pyrogram.types import CallbackQuery
from config import *
import yt_dlp
from youtube_search import YoutubeSearch
import os,sys,re,requests
import asyncio,time
from random import choice
from datetime import datetime
import logging

FORMAT = "[LEGEND-MUKESH] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


StartTime = time.time()
Mukesh = Client(
    "chat-gpt" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
START = f"""
ʜᴇʏ 

•  sᴏɴ ᴅᴇʀᴇᴄᴇ ɢᴇʟɪ̇şᴍɪ̇ş, ʙɪ̇ʀ ᴄ̧ᴏᴋ ᴏ̈ᴢᴇʟʟɪ̇ɢ̆ᴇ sᴀʜɪ̇ᴘ ʙɪ̇ʀ ʙᴏᴛᴜᴍ !

•  ᴋᴏᴍᴜᴛʟᴀʀ ᴠᴇ ᴅᴇsᴛᴇᴋ ɪ̇ᴄ̧ɪ̇ɴ ᴀşᴀɢ̆ɪᴅᴀᴋɪ̇ ʙᴜᴛᴏɴʟᴀʀɪ ᴋᴜʟʟᴀɴɪɴ !
"""
xa = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()
SOURCE = xa
SOURCE_TEXT = f"""
๏ ʜᴇʏ,
"""


x=["❤️","🎉","✨","🪸","🎉","🎈","🎯"]
g=choice(x)
MAIN = [
    [
        InlineKeyboardButton(
            text="ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ʏᴀʀᴅıᴍ & ᴋᴏᴍᴜᴛʟᴀʀ ", callback_data="HELP"),
    ],
]
X = [
    [
        InlineKeyboardButton(text=" ᴅᴇsᴛᴇᴋ ", url=f"https://t.me/{SUPPORT_GRP}"),
    ]
    ]
    
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="ᴅᴇsᴛᴇᴋ", 
                              url=f"https://t.me/{SUPPORT_GRP}",
         ),
     ],
]
SOURCE_BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('sᴏᴜʀᴄᴇ', url=f"{SOURCE}")]])
HELP_READ = "**➻ 𝗞𝘂𝗹𝗹𝗮𝗻ı𝗺 :**  \n\n/tag  **Etiketleme** \n\n/bul **Müzik Indirme** \n\n/ping **Sağlık Test** \n\n/admin **Admin Etiketleme** \n\n/durdur **İşlem Durdurma**"
HELP_BACK = [
     [
           InlineKeyboardButton(text="ᴋᴀʏɴᴀᴋ ", url=f"https://github.com/zeedslowy/PlutoTagger"),
           
     ],
    [
           InlineKeyboardButton(text="⬅️ ", callback_data="HELP_BACK"),
    ],
]

  
#         start
@Mukesh.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def start(client, m: Message):
    try:
        accha = await m.reply_text(
                        text = f"{g}")
        await asyncio.sleep(0.2)
        await accha.edit("✦ Yᴜ̈ᴋʟᴇɴɪʏᴏʀ..")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(
                  sticker = STKR,
        )
        await asyncio.sleep(0.3)
        await umm.delete()
        await m.reply_photo(
            photo = START_IMG,
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
    except Exception as y:
        await m.reply(y)
#  callback 
@Mukesh.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
     await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BACK),
     )
    elif query.data == "HELP_BACK":
            await query.message.edit(text = START,
                  reply_markup=InlineKeyboardMarkup(MAIN),
        )
    
@Mukesh.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    hmm = await message.reply_photo(START_IMG,
                        caption=HELP_READ,
                        reply_markup= InlineKeyboardMarkup(HELP_BACK),
       )
@Mukesh.on_message(filters.command(['source', 'repo'], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def source(bot, m):
    
    await m.reply_photo(START_IMG, caption=SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
#  alive
@Mukesh.on_message(filters.command(["ping","alive"], prefixes=["+", "/", "-", "?", "$", "&","."]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "Bekleyiniz.."
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("✦ Yᴜ̈ᴋʟᴇɴɪʏᴏʀ..")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(
                             photo=START_IMG,
                             caption=f"ʜᴇʏ !!\n**[{BOT_NAME}](t.me/{BOT_USERNAME}) ɪ̇ʟᴇᴛɪşɪᴍ ᴠᴇ öɴᴇʀɪ \n➥ `{ms}` ms\n\n**🌹 || [sᴀʜɪᴘ](https://t.me/{OWNER_USERNAME})||",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )

#  main   

chatQueue = []

stopProcess = False

@Mukesh.on_message(filters.command(["tag","all"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"] ))
async def everyone(client, message):
  global stopProcess
  try: 
    try:
      sender = await teletips.get_chat_member(message.chat.id, message.from_user.id)
      has_permissions = sender.privileges
    except:
      has_permissions = message.sender_chat  
    if has_permissions:
      if len(chatQueue) > 50:
        await message.reply("⛔️ | Şuan 50 Sohbet Üzerinde Çalışıyorum")
      else:  
        if message.chat.id in chatQueue:
          await message.reply("🚫 | Lütfen İşlemin Bitmesini Bekleyiniz.")
        else:  
          chatQueue.append(message.chat.id)
          if len(message.command) > 1:
            inputText = message.command[1]
          elif len(message.command) == 1:
            inputText = ""    
          membersList = []
          async for member in teletips.get_chat_members(message.chat.id):
            if member.user.is_bot == True:
              pass
            elif member.user.is_deleted == True:
              pass
            else:
              membersList.append(member.user)
          i = 0
          lenMembersList = len(membersList)
          if stopProcess: stopProcess = False
          while len(membersList) > 0 and not stopProcess :
            j = 0
            text1 = f"{inputText}\n\n"
            try:    
              while j < 10:
                user = membersList.pop(0)
                if user.username == None:
                  text1 += f"{user.mention} "
                  j+=1
                else:
                  text1 += f"@{user.username} "
                  j+=1
              try:     
                await teletips.send_message(message.chat.id, text1)
              except Exception:
                pass  
              await asyncio.sleep(10) 
              i+=10
            except IndexError:
              try:
                await teletips.send_message(message.chat.id, text1)  
              except Exception:
                pass  
              i = i+j
          if i == lenMembersList:    
            await message.reply(f"✅ | Etiketleme Başarılı.") 
          else:
            await message.reply(f"✅ | İşlem Başarılı.")    
          chatQueue.remove(message.chat.id)
    else:
      await message.reply("👮🏻 | Üzgünüm, **Sadece Adminler**")  
  except FloodWait as e:
    await asyncio.sleep(e.value)
      

@Mukesh.on_message(filters.command(["bul", "song"]))
def song(client, message):

    message.delete()
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chutiya = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    query = ""
    for i in message.command[1:]:
        query += " " + str(i)
    print(query)
    m = message.reply("» İndiriliyor.")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        # print(results)
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)

        duration = results[0]["duration"]
        results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "Sonuç Bulunamadı"
        )
        print(str(e))
        return
    m.edit("» Bekleyiniz..")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"**Başlık :** {title[:25]}\n**Süre :** `{duration}`\n**İzlenme :** `{views}`\n**Talep​ »** {chutiya}"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
        message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            title=title,
            duration=dur,
        )
        m.delete()
    except Exception as e:
        m.edit(
            f"» Başarısız"
        )
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
        
        
@Mukesh.on_message(filters.command(["durdur","cancel"]))
async def stop(client, message):
  global stopProcess
  try:
    try:
      sender = await teletips.get_chat_member(message.chat.id, message.from_user.id)
      has_permissions = sender.privileges
    except:
      has_permissions = message.sender_chat  
    if has_permissions:
      if not message.chat.id in chatQueue:
        await message.reply("🤷🏻‍♀️ | Maleaef Şuan Etiketleme İşlemindeyim.")
      else:
        stopProcess = True
        await message.reply("🛑 | Durdurldu.")
    else:
      await message.reply("👮🏻 | Üzgünüm, **Sadece Adminler**")
  except FloodWait as e:
    await asyncio.sleep(e.value)

@Mukesh.on_message(filters.command(["admins","staff"]))
async def admins(client, message):
  try: 
    adminList = []
    ownerList = []
    async for admin in teletips.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
      if admin.privileges.is_anonymous == False:
        if admin.user.is_bot == True:
          pass
        elif admin.status == ChatMemberStatus.OWNER:
          ownerList.append(admin.user)
        else:  
          adminList.append(admin.user)
      else:
        pass   
    lenAdminList= len(ownerList) + len(adminList)  
    text2 = f"**Grup Yönetici Listesi - {message.chat.title}**\n\n"
    try:
      owner = ownerList[0]
      if owner.username == None:
        text2 += f"👑 Sahip\n└ {owner.mention}\n\n👮🏻 Admin 1\n"
      else:
        text2 += f"👑 Sahip\n└ @{owner.username}\n\n👮🏻 Admin 2\n"
    except:
      text2 += f"👑 Sahip\n└ <i>Gizemli</i>\n\n👮🏻 Admin 3\n"
    if len(adminList) == 0:
      text2 += "└ <i>Gizli Yöneticiler</i>"  
      await teletips.send_message(message.chat.id, text2)   
    else:  
      while len(adminList) > 1:
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"├ {admin.mention}\n"
        else:
          text2 += f"├ @{admin.username}\n"    
      else:    
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"└ {admin.mention}\n\n"
        else:
          text2 += f"└ @{admin.username}\n\n"
      text2 += f"✅ | **Toplam Yöneticiler Listesi**"  
      await teletips.send_message(message.chat.id, text2)           
  except FloodWait as e:
    await asyncio.sleep(e.value)       

@Mukesh.on_message(filters.command("bot"))
async def bots(client, message):  
  try:    
    botList = []
    async for bot in teletips.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BOTS):
      botList.append(bot.user)
    lenBotList = len(botList) 
    text3  = f"**BOT LISTESİ - {message.chat.title}**\n\n🤖 | Mevcut Botlarınız\n"
    while len(botList) > 1:
      bot = botList.pop(0)
      text3 += f"├ @{bot.username}\n"    
    else:    
      bot = botList.pop(0)
      text3 += f"└ @{bot.username}\n\n"
      text3 += f"✅ | **Toplam Bot Listesi**: {lenBotList}"  
      await teletips.send_message(message.chat.id, text3)
  except FloodWait as e:
    await asyncio.sleep(e.value)
 

s = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()

if SOURCE != s:
    print("So sad, you have changed source, change it back to ` https://github.com/Noob-mukesh/Chatgpt-bot `  else I won't work")
    sys.exit(1)  


if __name__ == "__main__":
    print(f""" {BOT_NAME} ɪs ᴀʟɪᴠᴇ!
    """)
    try:
        Mukesh.start()
        
        
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    print(f"""JOIN  @MR_SUKKUN
GIVE STAR TO THE REPO 
 {BOT_NAME} ɪs ᴀʟɪᴠᴇ!  
    """)
    idle()
    Mukesh.stop()
    print("Bot stopped. Bye !")
#-----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
