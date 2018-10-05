from mongoengine import Document, StringField, IntField, FloatField, ImageField

class Menu(Document):
    code = StringField()
    title = StringField()
    unit = IntField(default=0)
    calori = IntField()
    category = StringField()
    image_link = StringField()




  