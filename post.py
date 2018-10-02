from mongoengine import Document, StringField, IntField, FloatField

class Post(Document):
    sex = StringField()
    weight = FloatField(default=None)
    height = FloatField(default=None)
    age = IntField(default=None)
    exercise = StringField()