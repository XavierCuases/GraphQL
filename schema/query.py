import json

def load_users():
    with open("data/users.json", "r") as f:
        return json.load(f)

from ariadne import QueryType

query = QueryType()

@query.field("users")
def resolve_users(_, info):
    users = load_users()
    return [{"id": key, **value} for key, value in users.items()]

@query.field("user")
def resolve_user(_, info, id):
    users = load_users()
    user = users.get(id)
    return {"id": id, **user} if user else None
