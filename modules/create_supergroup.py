from pyrogram import Client

api_id = 
api_hash = ""

with Client("minha_conta", api_id,"api_hash") as app:
    app.create_supergroup("Supergrupo Teste Python", "Teste de criação supergrupo via python")
