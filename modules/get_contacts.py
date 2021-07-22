from pyrogram import Client

api_id = 
api_hash = ""

with Client("minha_conta", api_id,"api_hash") as app:
    
    count = app.get_contacts_count()
print(count)