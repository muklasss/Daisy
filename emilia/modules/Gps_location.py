import os
from emilia import client
from geopy.geocoders import Nominatim
from emilia.events import register

from telethon import *
from telethon.tl import *

from emilia import client, dispatcher
from emilia.events import register
from telegram.ext import CommandHandler , run_async
from emilia.modules.helper_funcs.chat_status import user_admin
from emilia.modules.helper_funcs.alternate import send_message
GMAPS_LOC = "https://maps.googleapis.com/maps/api/geocode/json"

@run_async
@user_admin






def gps(update,context):
    args = update.effective_message.text.split(None, 1)
    chat = update.effective_chat

    try:
        geolocator = Nominatim(user_agent="SkittBot")
        location = args
        geoloc = geolocator.geocode(location)
        longitude = geoloc.longitude
        latitude = geoloc.latitude
        gm = "https://www.google.com/maps/search/{},{}".format(
            latitude, longitude)
        send_message(update.effective_message.send_file(chat.id, file=types.InputMediaGeoPoint(types.InputGeoPoint(float(latitude), float(longitude))))
        send_message(update.effective_message,
            "Open with: [Google Maps]({})".format(gm),
            link_preview=False,
        )
    except Exception as e:
        print(e)
        send_message(update.effective_message,"I can't find that")
                     
                     
GPS_HANDLER = CommandHandler('gps', gps)

dispatcher.add_handler(GPS_HANDLER)


__command_list__ = ["gps"]
__handlers__ = [
    
    GPS_HANDLER
]
