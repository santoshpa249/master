from django.db import connection


def mysql_connection(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        # cursor.callproc(query)
        return cursor.fetchall()
