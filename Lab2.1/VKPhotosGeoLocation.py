import vk
import time
print('VK Photos geo location')
#авторизируем сессию
session = vk.AuthSession('5690387', '79282165358','Prosoccer20188' )

#cоздаем обьект API
api = vk.API(session)

#запрашиваем список всех друзей
friends = api.friends.get()

#получаем информацию о всех друзьях
friends_info = api.users.get(user_ids=friends)

#выведем список друзей в удобном виде
for friend in friends_info:
    print('ID: %s Имя: %s %s' % (friend['uid'], friend['last_name'], friend['first_name']))
#здесь будут храниться геоданные
geolocation = []

#получим геоданные всех фотографий каждого друга
#цикл перебирающий всех друзей
for id in friends:
    print('Получаем данные пользователя: %s' % id)
    #получаем все альбомы пользователя, кроме служебных
    albums = api.photos.getAlbums(owner_id=id)
    print('\t...альбомов %s...' % len(albums))
    #цикл перебирающий все альбомы пользователя
    for album in albums:
        try:
            photos = api.photos.get(owner_id=id, album_id=album['aid'])
            print('\t\t...обрабатываем фотографии альбома...')
            for photo in photos:
                if  'lat' in photo and 'long' in photo:
                    geolocation.append((photo['lat'], photo['long']))
            print('\t\t...найдено %s фото...' % len(photos))
        except:
            pass
        time.sleep(0.5)
    time.sleep(0.5)

#Здесь будет храниться сгенерированный JavaScript код
js_code = " "

for loc in geolocation:
    js_code += 'new google.maps.Marker({ position: {lat: %s, lng: %s}, map: map});\n' % (loc[0], loc[1])
#считываем из файла-шаблона html данные
html = open('map.html').read()
#заменяем placeholder на сгенерированый код
html = html.replace('/* PLACEHOLDER */', js_code)

#записываем данные в новый файл
f = open('VKPhotosGeoLocation.html', 'w')
f.write(html)
f.close()