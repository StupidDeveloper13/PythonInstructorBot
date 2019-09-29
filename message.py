from function import *
from message import *
#from main import *
from createkey import *

def messages(event, vk_session, vk, longpoll, upload, uid, text, new_keyboard):
    if event.obj.peer_id < 2000000000:
        if uid > 0:
            if text == '!help':
                vk.messages.send(
                    user_id = uid,
                    message = 'Для вывода клавиатуры введите !key',
                    random_id = get_random_id()
                )
            elif text == '!key':
                start_keyboard(uid, event, vk)