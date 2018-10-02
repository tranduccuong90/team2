from mongoengine import Document, StringField, IntField, FloatField

class Post(Document):
    sex = StringField()
    weight = FloatField()
    height = FloatField()
    age = IntField()
    