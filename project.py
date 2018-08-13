from peewee import *
from datetime import date

db = PostgresqlDatabase('project',host = 'localhost', user = 'postgres', password='dssadmin')


class Project (Model):
    name = CharField()
    type = CharField()
    start_date= DateField()
    end_date=DateField()
    amount=IntegerField()
    description= TextField()

    class Meta:
        database= db
        # table='projects'
        table_name='project'
db.connect()
Project.create_table(fail_silently='true')

# print("table created")


# obj = Project.create(name="Grandma",type ="internal project",start_date= date(2018,8,10),end_date= date(2018,5,5),amount= 12000, description= "this is my first project", user_id = "1")

