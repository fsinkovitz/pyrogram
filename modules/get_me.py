from pyrogram import Client

api_id = 
api_hash = ""

with Client("minha_conta", api_id,"api_hash") as app:
    me = app.get_me()
print(me)