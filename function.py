import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkUpload
from vk_api.utils import get_random_id
#from .vk_api import VkApi, VkApiMethod
import requests
import threading
import os
from random import randint
from message import *
from main import *
import json

vk_session = vk_api.VkApi(token = 'token')

vk = vk_session.get_api()
group_id = int(id)

longpoll = VkBotLongPoll(vk_session, str(group_id))
upload = vk_api.VkUpload(vk_session)

