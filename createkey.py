from message import *
from function import *
from main import *
from funckey import *
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

#------------------#
#Стартовая страница#
#------------------#

def start_keyboard(uid, event, vk):

        keyboard = VkKeyboard(one_time=False)

        keyboard.add_button(
            'Теория',
            color=VkKeyboardColor.POSITIVE,
            payload = {'key': 'theory'}
        )
        keyboard.add_button(
            'Практика',
            color = VkKeyboardColor.NEGATIVE,
            payload = {'key': 'practice'}
        )
        keyboard.add_button(
            'Подсказки',
            color=VkKeyboardColor.PRIMARY,
            payload={'key': 'help'}
        )

        keyboard.add_line()

        keyboard.add_vkpay_button(hash = 'action=transfer-to-user&user_id=127949564', payload={'key': 'donate'})

        keyboard.add_line()

        keyboard.add_button(
            'Вызов админа',
            color=VkKeyboardColor.NEGATIVE,
            payload={'key': 'push'}
        )

        vk.messages.send(
            user_id = uid,
            message = 'Управляйте ботом с помощью кнопок',
            keyboard = keyboard.get_keyboard(),
            random_id = get_random_id()
)

#----------------------#
#Первая страница теории#
#----------------------#

def theory_list_one(uid, event, vk):
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        'Урок №1',
        color=VkKeyboardColor.PRIMARY,
        payload= {'key': 'lesson1'}
    )

    keyboard.add_button(
        'Урок №2',
        color=VkKeyboardColor.PRIMARY,
        payload={'key': 'lesson2'}
    )

    keyboard.add_button(
        'Урок №3',
        color=VkKeyboardColor.PRIMARY,
        payload={'key': 'lesson3'}
    )

    keyboard.add_button(
        'Урок №4',
        color=VkKeyboardColor.PRIMARY,
        payload={'key': 'lesson4'}
    )

    keyboard.add_line()

    keyboard.add_button(
        'Урок №5',
        color=VkKeyboardColor.POSITIVE,
        payload={'key': 'lesson5'}
    )

    keyboard.add_button(
        'Урок №6',
        color=VkKeyboardColor.POSITIVE,
        payload={'key': 'lesson6'}
    )

    keyboard.add_button(
        'Урок №7',
        color=VkKeyboardColor.POSITIVE,
        payload={'key': 'lesson7'}
    )

    keyboard.add_button(
        'Урок №8',
        color=VkKeyboardColor.POSITIVE,
        payload={'key': 'lesson8'}
    )

    keyboard.add_line()

    keyboard.add_button(
        'Назад',
        color=VkKeyboardColor.NEGATIVE,
        payload={'key': 'lesson_back1'}
    )

    keyboard.add_button(
        'Далее',
        color=VkKeyboardColor.NEGATIVE,
        payload={'key': 'lesson_next1'}
    )

    vk.messages.send(
            user_id = uid,
            message = 'Вы перешли в раздел теории',
            keyboard = keyboard.get_keyboard(),
            random_id = get_random_id()
    )

#----------------------#
#Вторая страница теории#
#----------------------#
def theory_list_two(uid, event, vk):
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        'Урок №9',
        color=VkKeyboardColor.PRIMARY,
        payload= {'key': 'lesson9'}
    )

    keyboard.add_button(
        'Урок №10',
        color=VkKeyboardColor.PRIMARY,
        payload={'key': 'lesson10'}
    )

    keyboard.add_button(
        'Урок №11',
        color=VkKeyboardColor.PRIMARY,
        payload={'key': 'lesson11'}
    )

    keyboard.add_button(
        'Урок №12',
        color=VkKeyboardColor.PRIMARY,
        payload={'key': 'lesson12'}
    )

    keyboard.add_line()

    keyboard.add_button(
        'Назад',
        color=VkKeyboardColor.NEGATIVE,
        payload={'key': 'lesson_back2'}
    )

    keyboard.add_button(
        'Главная',
        color=VkKeyboardColor.NEGATIVE,
        payload={'key': 'start'}
    )

    vk.messages.send(
            user_id = uid,
            message = 'Вы перешли на вторую страницу Теории',
            keyboard = keyboard.get_keyboard(),
            random_id = get_random_id()
    )

#------------------------#
#Первая страница практики#
#------------------------#

def practice_list_one(uid, event, vk):
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        'Задача к уроку №1',
        color=VkKeyboardColor.PRIMARY,
        payload={'key': 'task1'}
    )

    keyboard.add_button(
        'Задача к уроку №2',
        color=VkKeyboardColor.PRIMARY,
        payload={'key': 'task2'}
    )

    keyboard.add_button(
        'Задача к уроку №3',
        color=VkKeyboardColor.PRIMARY,
        payload={'key': 'task3'}
    )

    keyboard.add_button(
        'Задача к уроку №4',
        color=VkKeyboardColor.PRIMARY,
        payload={'key': 'task4'}
    )

    keyboard.add_line()

    keyboard.add_button(
        'Задача к уроку №5',
        color=VkKeyboardColor.POSITIVE,
        payload={'key': 'task5'}
    )

    keyboard.add_button(
        'Задача к уроку №6',
        color=VkKeyboardColor.POSITIVE,
        payload={'key': 'task6'}
    )
    keyboard.add_button(
        'Задача к уроку №7',
        color=VkKeyboardColor.POSITIVE,
        payload={'key': 'task7'}
    )

    keyboard.add_button(
        'Задача к уроку №8',
        color=VkKeyboardColor.POSITIVE,
        payload={'key': 'task8'}
    )

    keyboard.add_line()

    keyboard.add_button(
        'Назад',
        color=VkKeyboardColor.NEGATIVE,
        payload={'key': 'task_back1'}
    )

    keyboard.add_button(
        'Далее',
        color=VkKeyboardColor.NEGATIVE,
        payload={'key': 'task_next1'}
    )

    vk.messages.send(
            user_id = uid,
            message = 'Вы перешли в раздел практики',
            keyboard = keyboard.get_keyboard(),
            random_id = get_random_id()
    )

#------------------------#
#Вторая страница практики#
#------------------------#
def practice_list_two(uid, event, vk):
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        'Задача к уроку №9',
        color=VkKeyboardColor.PRIMARY,
        payload={'key': 'task9'}
    )

    keyboard.add_button(
        'Задача к уроку №10',
        color=VkKeyboardColor.PRIMARY,
        payload={'key': 'task10'}
    )

    keyboard.add_button(
        'Задача к уроку №11',
        color=VkKeyboardColor.PRIMARY,
        payload={'key': 'task11'}
    )

    keyboard.add_button(
        'Задача к уроку №12',
        color=VkKeyboardColor.PRIMARY,
        payload={'key': 'task12'}
    )

    keyboard.add_line()

    keyboard.add_button(
        'Назад',
        color=VkKeyboardColor.NEGATIVE,
        payload={'key': 'task_back2'}
    )

    keyboard.add_button(
        'Главная',
        color=VkKeyboardColor.NEGATIVE,
        payload={'key': 'start'}
    )

    vk.messages.send(
            user_id = uid,
            message = 'Вы перешли на вторую страницу практики',
            keyboard = keyboard.get_keyboard(),
            random_id = get_random_id()
    )

#-------------------------#
#Первая страница подсказок#
#-------------------------#

def help(uid, event, vk):
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        'Web',
        color=VkKeyboardColor.PRIMARY,
        payload={'key': 'help_web'}
    )

    keyboard.add_button(
        'GUI',
        color=VkKeyboardColor.POSITIVE,
        payload={'key': 'help_desktop'}
    )

    keyboard.add_button(
        'Neural Networks',
        color=VkKeyboardColor.NEGATIVE,
        payload={'key': 'help_nn'}
    )

    keyboard.add_line()

    keyboard.add_button(
        'Назад',
        color=VkKeyboardColor.NEGATIVE,
        payload={'key': 'help_back1'}
    )

    keyboard.add_button(
        'Далее',
        color=VkKeyboardColor.NEGATIVE,
        payload={'key': 'help_next1'}
    )

    vk.messages.send(
            user_id = uid,
            message = 'Вы перешли в раздел подсказок',
            keyboard = keyboard.get_keyboard(),
            random_id = get_random_id()
    )