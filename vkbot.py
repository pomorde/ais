import vk
import time
import datetime


print("vkBot")


session = vk.Session('01144ba1ccfac9f1ac3504c1ef21b29b48f6dfda22ba729ae5f7aca810efba63fc54070d178ea22de1c94')

api = vk.API(session)

while(True):
    messages = api.messages.get()

    commands = ['help','weather']

    messages = [(m['uid'],m['mid'],m['body'])
                for m in messages[1:] if m['body'] in commands and m['read_state'] == 0]

    for m in messages:
        user_id = m[0]
        message_id = m[1]
        command = m[2]

        date_time_string = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')

        if command == 'help' :
            api.messages.send(user_id=user_id,message=date_time_string + '\n>VKBOT v0.1\n>Разработал: Fania')

        if command == 'weather' :
            api.messages.send(user_id=user_id,message=date_time_string + '\nПогода отличная!!')
    ids = ', '.join([str(m[1]) for m in messages])

    if ids :
        api.messages.markAsRead(message_id=ids)

    time.sleep(3)