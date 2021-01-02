import botFuncs as bf
import discord as d
from discord.ext import commands


client = d.Client()
@client.event
async def on_message(message):
  #message.content = message.content.lower()
  if message.author == client.user:
    return
  if message.content.startswith("/cencrypt "): # /encrypt (cypher letter) (...)
    encrypted_message = bf.caesar_encrypt(message.content[12:], message.content[10]) # Reads the content as well as the cypher
    await message.channel.send(encrypted_message)

  if message.content.startswith("/mencrypt "):
    encrypted_message = bf.morse_encrypt(message.content[10:]) # Reads the content as well as the cypher
    await message.channel.send(encrypted_message)

  if message.content.startswith("/cdecrypt "): # /decrypt (cypher letter) (...)
    decrypted_message = bf.caesar_decrypt(message.content[12:], message.content[10])
    await message.channel.send(decrypted_message)

  if message.content.startswith("/help"): # Gives a list of commands
    definitions = bf.help()
    await message.channel.send(definitions)

client.run('NzUxODM3OTI5MTQzMjcxNDk0.X1O5og.Suh8RT2Mxg-xTCL8USMjWIUKwUI')