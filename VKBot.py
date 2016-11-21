# -*- coding: utf-8 -*-

import vk
import time
import datetime


print('VKBot')
session = vk.AuthSession('5690387', '79282165358','Prosoccer2021' )

api = vk.API(session)
print('Authorization complete')

while True:

    messages = api.messages.get()
    commands = ['команды', 'погода', 'обо мне', 'что такое', 'подробнее']
    messages = [(m['uid'], m['mid'], m['body'])
                for m in messages[1:] if m['body'] and m['read_state'] == 0]

    for m in messages:
        user_id = m[0]
        message_id = m[1]
        command = str(m[2])

        date_time_string = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')

        if command == 'команды':
            for command in commands:
                api.messages.send(user_id=user_id, message=command)
                time.sleep(1)

        if command == 'погода':
            api.messages.send(user_id=user_id, message=getWeather())

        if command == 'обо мне':
            api.messages.send(user_id=user_id, message=date_time_string + '\n>VKBot v.0.0.1\n>Разработка asketes' )

    ids = ', '.join([str(m[1]) for m in messages])

    if ids:
        api.messages.markAsRead(message_ids=ids)

    time.sleep(3)