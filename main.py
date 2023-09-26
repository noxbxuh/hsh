import telethon
from telethon import events
from telethon.sync import functions
from telethon import TelegramClient
import telethon
import random
from random import choices
import time ;import os
from telethon.tl.functions.messages import GetPeerDialogsRequest


StrPython.start()
band = []

ban = open("band.txt","r").read().split()
band.append(ban)
abcd = "qwertyuiopassdfghjklzxcvbnm"
number = "1234567890"

@StrPython.on(
events.NewMessage(
outgoing=True, pattern=r"تشغيل الحجز"))
async def StrPychecker(event):
        clicks = 1
       
        await StrPython.send_message("botfather","/newbot")
        await StrPython.send_message("botfather","king 🍋")
        
        

        await event.reply(f"تم البدأ بنجاح 🐊")
        while True:
            q = random.choices(abcd)
            w = random.choices(abcd)
            b = random.choices(abcd)
            user = [q[0],w[0],b[0]]
            username = "".join(user)
            username = username+"bot"
		
            if username in band[0]:
            	pass
            else:
                pass
                clicks += 1
                try:
                	os.remove("clicks.txt")
                except :
                	open("clicks.txt","a").write(str(clicks)+"\n")
                else:
                	open("clicks.txt","a").write(str(clicks)+"\n")
                try:
             	   await StrPython(GetPeerDialogsRequest(peers=[username]))
             	   
                except Exception as err:
                    if "No user has" in str(err):
                        
                        	await StrPython.send_message("botfather",str(username))
                        
                        	await StrPython.send_file(event.chat_id, "https://t.me/xx3bD/203",caption=f'''
Good evening 🪶
⌯ User ⤷ @{username}
⌯ Save ⤷ bot
⌯ Clicks ⤷ {clicks}
⌯ Program the bot ⤷ @xx_YaBh''')
                        	os.remove("clicks.txt")
                        	break
                                 
                        
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    	band.append(username)
                except telethon.errors.rpcerrorlist.UsernameOccupiedError:
                    	time.sleep(1);continue
                except telethon.errors.rpcerrorlist.FloodWaitError as ses:
                    	await StrPython.send_message(event.chat.id,f"Flood & {ses.seconds}")
                    	
                    	break
             
       


@StrPython.on(events.NewMessage(outgoing=True, pattern=r"الضغطات"))
async def Shhtah(event):
	try:
		n = open("clicks.txt","r").read()
		
	except:
		await event.reply("طافي يابه؟ 💀")
	else:
		
		await event.reply(f"عدد الضغطات حاليا : {n}")
	
	
	
	
	

for x in StrPython.iter_dialogs():
		if x.is_user and not x.entity.bot:
			
				too = x.id
				msg = """

Programmer : @xx_YaBh
المطور : @xx_YaBh"""
				try:
					StrPython.send_message(too, msg)
				except BaseException:continue
StrPython.send_file("me","https://t.me/xx3bD/178",caption=f"""**مرحبا بك في سورس تشيكر  (t.me/xx_YaBh) .
اليك الاوامر ادناة .
الأمر الاول : `ايقاف الحجز`
الأمر الثاني : `تشغيل الحجز`
الأمر الثالث : `الضغطات`**
""")
@StrPython.on(events.NewMessage(outgoing=True, pattern=r"ايقاف الحجز"))
async def Shhtah(event):
	await StrPython.send_message(event.chat_id,"جارِ ...")

	await StrPython.disconnect()
	
print("Run")
StrPython.run_until_disconnected()
