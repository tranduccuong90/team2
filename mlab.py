import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds157742.mlab.com:57742/c4e21-blog

host = "ds157742.mlab.com"
port = 57742
db_name = "c4e21-blog"
user_name = "admin"
password = "a2811994"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
