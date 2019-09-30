from function import *
from createkey import *
from message import *
from main import *


def keyfunc(uid, text, vk, vk_session, event):

    #------------------#
    #Стартовая страница#
    #------------------#

    if text == 'theory':
        theory_list_one(uid, event, vk)

    elif text == 'practice':
        practice_list_one(uid, event, vk)

    elif text == 'help':
        help(uid, event, vk)

    elif text == 'donate':
        vk.messages.send(
                user_id = uid,
                message = 'Пока что, платёжная система не прикреплена к боту. \n Пожертвования принимаются на такие реквизиты: \nQIWI: +79603287087 \nСбербанк: 2202 2001 6235 6354 \nЯндекс Деньги: 410013630987746',
                random_id = get_random_id()
            )

    #----------------------#
    #Первая страница теории#
    #----------------------#

    elif text == 'lesson1':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-vvedenie-v-python \nК первому вводному уроку, практической задачи не будет.',
            random_id = get_random_id()
        )

    elif text == 'lesson2':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-vvod-i-vyvod-dannyh \nНе забудьте заглянуть в раздел Практики, чтобы закрепить изученное задачками 😉',
            random_id = get_random_id()
        )

    elif text == 'lesson3':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-usloviya \nНе забудьте заглянуть в раздел Практики, чтобы закрепить изученное задачками 😉',
            random_id = get_random_id()
        )

    elif text == 'lesson4':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-vychisleniya \nНе забудьте заглянуть в раздел Практики, чтобы закрепить изученное задачками 😉',
            random_id = get_random_id()
        )

    elif text == 'lesson5':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-cikl-for \nНе забудьте заглянуть в раздел Практики, чтобы закрепить изученное задачками 😉',
            random_id = get_random_id()
        )

    elif text == 'lesson6':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-stroki \nНе забудьте заглянуть в раздел Практики, чтобы закрепить изученное задачками 😉',
            random_id = get_random_id()
        )

    elif text == 'lesson7':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-cikl-while \nНе забудьте заглянуть в раздел Практики, чтобы закрепить изученное задачками 😉',
            random_id = get_random_id()
        )

    elif text == 'lesson8':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-spiski \nНе забудьте заглянуть в раздел Практики, чтобы закрепить изученное задачками 😉',
            random_id = get_random_id()
        )

    elif text == 'lesson9':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-funkcii-i-rekursiya \nНе забудьте заглянуть в раздел Практики, чтобы закрепить изученное задачками 😉',
            random_id = get_random_id()
        )

    elif text == 'lesson10':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-dvumernye-massivy \nНе забудьте заглянуть в раздел Практики, чтобы закрепить изученное задачками 😉',
            random_id = get_random_id()
        )

    elif text == 'lesson11':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-mnozhestva \nНе забудьте заглянуть в раздел Практики, чтобы закрепить изученное задачками 😉',
            random_id = get_random_id()
        )

    elif text == 'lesson12':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-slovari \nНе забудьте заглянуть в раздел Практики, чтобы закрепить изученно задачками 😉',
            random_id = get_random_id()
        )

    elif text == 'lesson_back1':
        start_keyboard(uid, event, vk)

    elif text == 'lesson_next1':
        theory_list_two(uid, event, vk)

    elif text == 'lesson_back2':
        theory_list_one(uid, event, vk)

    elif text == 'start':
        start_keyboard(uid, event, vk)

    #------------------------#
    #Первая страница практики#
    #------------------------#

    elif text == 'task1':
        vk.messages.send(
            user_id = uid,
            message = 'Первый урок, был вводным. Задачи не будет.',
            random_id = get_random_id()
        )

    elif text == 'task2':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-zadanie-k-uroku-2',
            random_id = get_random_id()
        )

    elif text == 'task3':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-zadanie-k-uroku-3',
            random_id = get_random_id()
        )

    elif text == 'task4':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-zadanie-k-uroku-4',
            random_id = get_random_id()
        )

    elif text == 'task5':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-zadanie-k-uroku-5',
            random_id = get_random_id()
        )

    elif text == 'task6':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-zadanie-k-uroku-6',
            random_id = get_random_id()
        )

    elif text == 'task7':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-zadanie-k-uroku-7',
            random_id = get_random_id()
        )

    elif text == 'task8':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-zadanie-k-uroku-8',
            random_id = get_random_id()
        )

    elif text == 'task9':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-zadanie-k-uroku-9',
            random_id = get_random_id()
        )

    elif text == 'task10':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-zadanie-k-uroku-10',
            random_id = get_random_id()
        )

    elif text == 'task11':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-zadanie-k-uroku-11',
            random_id = get_random_id()
        )

    elif text == 'task12':
        vk.messages.send(
            user_id = uid,
            message = 'https://vk.com/@pythoninstructor-zadanie-k-uroku-12',
            random_id = get_random_id()
        )

    elif text == 'task_back1':
        start_keyboard(uid, event, vk)

    elif text == 'task_next1':
        practice_list_two(uid, event, vk)

    elif text == 'task_back2':
        practice_list_one(uid, event, vk)

    #-------------------------#
    #Первая страница подсказок#
    #-------------------------#

    elif text == 'help_web':
        vk.messages.send(
            user_id = uid,
            message = 'Подсказка не добавлена',
            random_id = get_random_id()
        )

    elif text == 'help_desktop':
        vk.messages.send(
            user_id = uid,
            message = 'Подсказка не добавлена',
            random_id = get_random_id()
        )

    elif text == 'help_ml':
        vk.messages.send(
            user_id = uid,
            message = 'Подсказка не добавлена',
            random_id = get_random_id()
        )

    elif text == 'help_back1':
        start_keyboard(uid, event, vk)

    elif text == 'help_next1':
        vk.messages.send(
            user_id = uid,
            message = 'Страница не готова',
            random_id = get_random_id()
        )

    elif text == 'push':
        vk.messages.send(
            user_id = 127949564,
            message = ('Вас вызвал юзер: https://vk.com/id' + str(uid)),
            random_id = get_random_id()
        )
        vk.messages.send(
            user_id = uid,
            message = 'Ожидайте, скоро админ выйдет с вами на связь.',
            random_id = get_random_id()
        )