from mysql.connector import connect, Error
from config import *

def getMats():
    try:
        with connect(
            host=data_base['server'],
            user=data_base['login'],
            password=data_base['password'],
        ) as connection:
            select_query = "SELECT word FROM apwebd10_django.Mats"
            with connection.cursor() as cursor:
                cursor.execute(select_query)
                abusive_language = [row[0] for row in cursor.fetchall()]
        return abusive_language

    except Error as e:
        print("Ошибка при получении матерных слов: ", e)
        return []

def getCapser():
    try:
        with connect(
            host=data_base['server'],
            user=data_base['login'],
            password=data_base['password'],
        ) as connection:
            select_query = "SELECT nick FROM apwebd10_django.capsers"
            with connection.cursor() as cursor:
                cursor.execute(select_query)
                caps_list = [row[0] for row in cursor.fetchall()]
        return caps_list

    except Error as e:
        print("Ошибка при получении списка капсеров: ", e)
        return []

def insertCaps(nick):
    try:
        with connect(
            host=data_base['server'],
            user=data_base['login'],
            password=data_base['password'],
        ) as connection:
            insert_query = "INSERT INTO apwebd10_django.capsers (`nick`) VALUES (%s)"
            with connection.cursor() as cursor:
                cursor.execute(insert_query, (nick,))
                connection.commit()
            print("Добавлен капсер: ", nick)

    except Error as e:
        print("Ошибка при добавлении капсера: ", e)
