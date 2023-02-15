from peewee import *

db = PostgresqlDatabase('testtwo', host='localhost', user='postgres', password='pytpyt')

class Data(Model):
    id = BigAutoField(unique=True)
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db
        order_by = 'id'
        db_table = 'data'





