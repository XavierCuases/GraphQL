from ariadne import MutationType
from schema.query import load_users  # Importar load_users
import json

# Escribir datos en JSON
def save_users(users):
    with open("data/users.json", "w") as f:
        json.dump(users, f, indent=2)

mutation = MutationType()

@mutation.field("createUser")
def resolve_create_user(_, info, name, age):
    users = load_users()
    new_id = str(len(users) + 1)
    users[new_id] = {"name": name, "age": age}
    save_users(users)
    return {"id": new_id, "name": name, "age": age}

@mutation.field("deleteUser")
def resolve_delete_user(_, info, id):
    users = load_users()
    if id in users:
        del users[id]
        save_users(users)
        return True
    return False
