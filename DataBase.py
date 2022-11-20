from mysql.connector import connect, Error
from config import *

def getMats():
    try:
        with connect(
            host=data_base['server'],
            user=data_base['login'],
            password=data_base['password'],
        ) as connection:
            abusive_language = []
            select_movies_query = "SELECT * FROM apwebd10_django.Mats"
            with connection.cursor() as cursor:
                cursor.execute(select_movies_query)
                result = cursor.fetchall()
                for row in result:
                    abusive_language.append(row[1])
        return abusive_language

    except Error as e:
        print("Ошибка: ", e)
        abusive_language = []
        return abusive_language

def getCapser():
    try:
        with connect(
            host=data_base['server'],
            user=data_base['login'],
            password=data_base['password'],
        ) as connection:
            caps_list = []
            select_movies_query = "SELECT * FROM apwebd10_django.capsers"
            with connection.cursor() as cursor:
                cursor.execute(select_movies_query)
                result = cursor.fetchall()
                for row in result:
                    caps_list.append(row[1])
        return caps_list

    except Error as e:
        print("Ошибка: ", e)
        caps_list = []
        return caps_list

def insertCaps(nick):
    try:
        with connect(
            host=data_base['server'],
            user=data_base['login'],
            password=data_base['password'],
        ) as connection:
            insert_movies_query = """INSERT INTO apwebd10_django.capsers(`nick`) VALUES ('""" + nick + """')"""
            with connection.cursor() as cursor:
                cursor.execute(insert_movies_query)
                connection.commit()
            print("Внесен капсер: ", nick)

    except Error as e:
        print("Ошибка: ", e)
