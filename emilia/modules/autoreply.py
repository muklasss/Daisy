from telegram import ParseMode, Update, Bot, Chat
from telegram.ext import CommandHandler, MessageHandler, BaseFilter, run_async

from emilia import dispatcher
from emilia.modules.helper_funcs.alternate import send_message
from emilia.modules.disable import DisableAbleCommandHandler, DisableAbleMessageHandler

import time

from telethon import TelegramClient, events

# sample API_ID from https://github.com/telegramdesktop/tdesktop/blob/f98fdeab3fb2ba6f55daf8481595f879729d1b84/Telegram/SourceFiles/config.h#L220
# or use your own
api_id = 2993816
api_hash = '7fb36e8000845a3834d852f1bd717469'
session_file = '@InukaASiTH'
# fill in your own details here

x=False
A=False
B=False
C=False
D=False
client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)


@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
    
        
    if event.is_private:  # only auto-reply to private chats
        
            
       from_ = await event.client.get_entity(event.from_id)  # this lookup will be cached by telethon
       if not from_.bot:  # don't auto-reply to bots
            
                
            print(time.asctime(), '-', event.message)  # optionally log time and message
            time.sleep(1)  # pause for 1 second to rate-limit automatic replies
            await event.respond(message)

    
                # Create the client and connect
                # use sequential_updates=True to respond to messages one at a time



                
def auto(update,context):
    global x
    global A
    global B
    global C
    global D

    global client
    
        
    if (A==True and C== True and D==True):
        
            
        print(time.asctime(), '-', 'Auto-replying...')
        client.start(phone, password)
        send_message(update.effective_message, "Service Started!")
            
        
            


            




    else:
        
        
        send_message(update.effective_message, "Enter all other commands before you go!")

            
def phne(update,context):
    global phone
    global A
    args = update.effective_message.text.split(None, 1)
    phone = args[1]
    send_message(update.effective_message, "Remember to add other things also.. Successful")
    A=True
    
def session(update,context):
    global session_file
    global B
    args = update.effective_message.text.split(None, 1)
    session_file = args[1]
    send_message(update.effective_message, "Remember to add other things also.. successful")
    B=True
    
def passwrd(update,context):
    global password
    global C
    args = update.effective_message.text.split(None, 1)
    password = args[1]
    send_message(update.effective_message, "Remember to add other things also.. Successful")
    C=True
    
def messag(update,context):
    global message
    global D
    args = update.effective_message.text.split(None, 1)
    message = args[1]
    send_message(update.effective_message, "Remember to add other things also.. Successful")
    D=True
    
def end(update,context):
    global x
    global client
    x=True
    client.stop
    print(time.asctime(), '-', 'Stopped!')
    send_message(update.effective_message, "Service Stopped")
        
__help__ = """ #FUCK_YOU
autoreply,phoneno,session,password,message,end"""

__mod_name__ = "SUDO ACCESS"


AUTO_HANDLER = DisableAbleCommandHandler("autoreply", auto)
PHNE_HANDLER = DisableAbleCommandHandler("phoneno", phne)
session_HANDLER = DisableAbleCommandHandler("session", session)
passwrd_HANDLER = DisableAbleCommandHandler("password", passwrd)
messag_HANDLER = DisableAbleCommandHandler("message", messag)
end_HANDLER = DisableAbleCommandHandler("end", end)
dispatcher.add_handler(AUTO_HANDLER)
dispatcher.add_handler(PHNE_HANDLER)
dispatcher.add_handler(session_HANDLER)
dispatcher.add_handler(passwrd_HANDLER)
dispatcher.add_handler(messag_HANDLER)
dispatcher.add_handler(end_HANDLER)
__command_list__ = ["autoreply","phoneno","session","password","message","end"]
__handlers__ = [
    AUTO_HANDLER, PHNE_HANDLER, session_HANDLER, passwrd_HANDLER, messag_HANDLER, end_HANDLER, 
]
    
