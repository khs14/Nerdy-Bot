
from flask import Flask
from threading import Thread
app=Flask('')

@app.route('/')

def confirmation():
  return "Senpai I'm here"
def run():
  app.run(host='0.0.0.0',port=8080)

def bot_forever():
  forver=Thread(target=run)
  forver.start()