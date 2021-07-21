from pyrogram import Client

api_id = 6766845
api_hash = "25db9298b5add501ced445e6328ab7e0"

with Client("minha_conta", 6766845,"25db9298b5add501ced445e6328ab7e0") as app:
    me = app.get_me()
print(me)