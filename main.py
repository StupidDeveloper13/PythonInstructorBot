import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkUpload
from vk_api.utils import get_random_id
import requests
from threading import *
import os
from random import *
from funckey import *
from createkey import *
from message import *
from function import *

def main():
    vk_session = vk_api.VkApi(token = '82e9afd96ab30ccae2c373267e03ded752ac0d84f6438bcaa89faed8fdfef26a82024af471c69579aca30')
    print('Bot started!')

    vk = vk_session.get_api()
    group_id = 182258031

    longpoll = VkBotLongPoll(vk_session, str(group_id))
    upload = vk_api.VkUpload(vk_session)

    def listener(event, vk, vk_session, upload, longpoll, group_id):
        if event.type == VkBotEventType.MESSAGE_NEW and event.object.text.strip()!='':
            uid = event.obj.from_id
            text = event.obj.text
            messages(event, vk_session, vk, longpoll, upload, uid, text, start_keyboard)
        if 'payload' in event.object:
            payload = event.object['payload']
            if payload[:8] == '{"key":"':
                uid = event.obj.from_id
                text = payload[8:][:-2]
                keyfunc(uid, text, vk, vk_session, event)

    for event in longpoll.listen():
        listen = Thread( target = listener, name = str(random()), args = (event, vk, vk_session, upload, longpoll, group_id) )
        listen.start()

if __name__ == "__main__":
    main()