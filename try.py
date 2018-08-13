from peewee import *
from datetime import date

db = PostgresqlDatabase('try',host = 'localhost', user = 'postgres', password='dssadmin')


class tryy (Model):
    name = CharField()
    type = CharField()
    start_date= DateField()
    end_date=DateField()
    amount=IntegerField()
    description= TextField()
    user_id= CharField()
    class Meta:
        database= db
        # table='projects'
        db.connect()
tryy.create_table()

print("table created")


obj = tryy.create(name="Grandma",type ="internal project",start_date= date(2018,8,10),end_date= date(2018,5,5),amount= 12000, description= "this is my first project", user_id = "1")
obj.name= 'Aunt'
obj.delete()
# for x in tryy.select():
#     print(x)