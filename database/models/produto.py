from peewee import Model, CharField, FloatField, BooleanField, TextField, DateTimeField
import datetime
from database.database import db

class Produto(Model):
    nome = CharField()
    descricao = TextField()
    valor = FloatField()
    disp = BooleanField()
    registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db 