import os

import wikipedia

import math

def log(value , base = 'e'):
  if base < 0 or base == 1 or base == 0 or value < 0:
    return 'domain error'
  elif base == 'e':
    return math.log(value)
  elif base == 10:
    return math.log10(value)
  elif base == 2:
    return math.log2(value)
  else :
    return math.log(value,base)








def prob50():
  num = [0,1]
  choice = random.choice()
  return choice

my_secret = os.environ['bot_token']
from nerdy_forever import bot_forever

import datetime

from datetime import datetime

import discord
import random
from discord.ext import commands
import time

import requests

client = commands.Bot(command_prefix='~')


def get_random_vocab_lvl():
  l=['e','m','h']
  vocab_lvl = random.choice(l)
  if vocab_lvl == 'e':
    return 'vocab_e.txt'
  if vocab_lvl == 'm':
    return 'vocab_m.txt'
  else :
    return 'vocab_h.txt'



def get_random_vocab(file_name):
  fout = open(file_name,'r')
  vocab_list = fout.readlines()
  fout.close()
  length_list = len(vocab_list)
  index_random = random.randint(0,length_list -1)
  return vocab_list[index_random]
  
def read_full(exam_level):
  with open(exam_level,'r') as fout:
    exams_list = fout.readlines()
  return exams_list

def get_vocab_send(vocab_str):
  vocab__list = vocab_str.split(',')
  return vocab__list


def get_name(full_list):
    name = ''
    for m in range(len(full_list)):
        if m == 0:
            pass
        else:
            name += full_list[m] + ' '
    return name

def get_google_search(term):
  term_list=term.split()
  x = len(term_list)
  for m in range(x):
    if m == (x - 1):
      pass
    else:
      term_list[m] = term_list[m] + '%20'
      search_term = ''
  for k in term_list:
    search_term = search_term + k
  return search_term  


def get_search(term_p):
  term_list=term_p.split()
  x = len(term_list)
  for m in range(x):
    if m == (x - 1):
      pass
    else:
      term_list[m] = term_list[m] + '_'
      search_term = ''
  for k in term_list:
    search_term = search_term + k
  return search_term  


@client.event
async def on_ready():
    print("Bot is online")


@client.event
async def on_message(message):
  s = message.content
  f = s.lower()
  l = f.split()
  study_gif = ['https://media.giphy.com/media/LkN7pIx62IaKm5DMOm/giphy.gif?cid=790b7611e264d7c7aa0cd73ee1dd94b8e7a8c04f8a3e68c8&rid=giphy.gif&ct=g', 'https://media.giphy.com/media/fhAwk4DnqNgw8/giphy.gif?cid=790b761186f3ade36e79017f737a177ee7f586f8f263b352&rid=giphy.gif&ct=g', 'https://media.giphy.com/media/1WbJnEhCpZTThmzFTz/giphy-downsized.gif?cid=790b7611aac69583b42c42c39d83fa8439c0181df841134d&rid=giphy-downsized.gif&ct=g','https://media.giphy.com/media/1WbJnEhCpZTThmzFTz/giphy-downsized.gif?cid=790b7611aac69583b42c42c39d83fa8439c0181df841134d&rid=giphy-downsized.gif&ct=g','https://media.giphy.com/media/YFFGUPTPTRqIhwepA4/giphy.gif?cid=790b7611c1d6a91b05b672f4ba6f916b32637809fd473a37&rid=giphy.gif&ct=g','https://media.giphy.com/media/WRRL1EKo9rNe12S4zh/giphy.gif?cid=790b7611cd29875793ccf706c3492994008a06ef6247510d&rid=giphy.gif&ct=g','https://media.giphy.com/media/10I54Pr7nbGrAs/giphy.gif?cid=790b761137867af700b3e1cb5ba253eebba703c5ef510c76&rid=giphy.gif&ct=g','https://media.giphy.com/media/vnAeqoVlbnqfuTtLt8/giphy-downsized.gif?cid=790b7611329a75c94bb22764bce3b0ce975bcef4c14bc52c&rid=giphy-downsized.gif&ct=g','https://media.giphy.com/media/RiPB21AVCQbMYI0dwm/giphy.gif?cid=790b7611ff4c00d23104f781ea4c926fe7144181d86c4ed3&rid=giphy.gif&ct=g','https://media.giphy.com/media/3o6nUMMgbMRhs9dUvS/giphy-downsized.gif?cid=790b76114e0c9c9b5d7f9a27731d952139f08eadccc0dd20&rid=giphy-downsized.gif&ct=g','https://media.giphy.com/media/VIKOfvqJHcVDrdVivT/giphy.gif?cid=790b7611fa0757ee501ac0b35649917dfac79ceb04c3bf59&rid=giphy.gif&ct=g','https://media.giphy.com/media/jBzO4OBN8oIms/giphy.gif?cid=790b76115a2a5b8d404cd4cd1573450da1c56f202c2f9dc9&rid=giphy.gif&ct=g','https://media.giphy.com/media/BXgfFotA3amW6GjJPj/giphy.gif?cid=790b7611e79ed646cebc9725797d4d78b21e506a985a1699&rid=giphy.gif&ct=g','https://media.giphy.com/media/8dYmJ6Buo3lYY/giphy.gif?cid=790b7611145b3d910b05182715f783604bf9ba9ebd32201a&rid=giphy.gif&ct=g','https://media.giphy.com/media/3owyp2SViuDIGh8YoM/giphy.gif?cid=790b76111efee936e974b32e41dc4c98096e79fe1485e8f1&rid=giphy.gif&ct=g','https://media.giphy.com/media/MEySLGjxQak0w/giphy.gif?cid=790b7611e59e2e0511b58960ed18e026a6ba450445d10b57&rid=giphy.gif&ct=g','https://media.giphy.com/media/g2lH60ZcvUGL6/giphy.gif?cid=790b7611b5d698a046bb853cabeba27d07d7713803259ba4&rid=giphy.gif&ct=g','https://media.giphy.com/media/DwrnYsZCXspu8/giphy.gif?cid=790b7611a3ddd1284272ee9166a4eb1fbc88643b65484ce5&rid=giphy.gif&ct=g','https://media.giphy.com/media/ql6hxonaYC6EE/giphy.gif?cid=790b761181de927ce1d68b12025f8ef2aaf14f9e64ad0ff1&rid=giphy.gif&ct=g','https://media.giphy.com/media/cuD1nbjhru7O5Ly0eI/giphy.gif?cid=790b7611caf60d841c941072036b554acb09c053969168a2&rid=giphy.gif&ct=g']
  if f == '~bye':
    await message.channel.send("BYE TTYL")
    await message.channel.send("Best of luck Senpai, Study hard")
    await message.channel.send(random.choice(study_gif))
    
  if f in ['~hi', '~hello', '~hey']:
    await message.channel.send("Ya Ya Hi, Now Please Study Senpai !")
    await message.channel.send(random.choice(study_gif))
  
  if f[:11:]=='~motivation':
    motivation_q = ['"The beautiful thing about learning is that no one can take it away from you". — B.B. King','“Learning is never done without errors and defeat.” – Vladimir Lenin','“A person who never made a mistake never tried anything new." — Albert Einstein','“The expert in anything was once a beginner." — Helen Hayes','“You don’t have to be great to start, but you have to start to be great.” – Zig Ziglar','“There are no shortcuts to any place worth going.” — Beverly Stills','“Motivation is what gets you started. Habit is what keeps you going.” – Jim Ryun','“Success is the sum of small efforts, repeated.” — R Collier','THE MIND IS NOT A VESSEL TO BE FILLED BUT A FIRE TO BE IGNITED','It’s not about how bad you want it. It’s about how hard you’re willing to work for it.','It’s not going to be easy, but it’s going to be worth','Strive for progress, not perfection.','The secret of success is to do the common things uncommonly well. – John D. Rockefeller']
    
    
    motivation_gif = ['https://media.giphy.com/media/3o85xtLX7zCyeeWGLC/giphy.gif?cid=790b7611b87eb5048e319ab034da8a7d6e5159fec56719ba&rid=giphy.gif&ct=g','https://media.giphy.com/media/4GXUa4U05Q0JAM972c/giphy-downsized.gif?cid=790b761119fdd9b907dccd31a4d48757a04fa11516920845&rid=giphy-downsized.gif&ct=g','https://media.giphy.com/media/l41Yh1olOKd1Tgbw4/giphy.gif?cid=790b76113be0c4db3e23250837b026ac2e114072ebf99af4&rid=giphy.gif&ct=g','https://media.giphy.com/media/dKs4KUXhoEYGupeI7L/giphy.gif?cid=790b76118d43b218e8d4b19f06faa53a64970ece74c22e5c&rid=giphy.gif&ct=g','https://media.giphy.com/media/bg58m10HpbljgFVXxY/giphy-downsized.gif?cid=790b7611de0f9286b21e3d1a087027cc6804af8514c7be72&rid=giphy-downsized.gif&ct=g','https://media.giphy.com/media/bpr2oLSUYUUcjq91zU/giphy-downsized.gif?cid=790b7611ed7fa751c134f8d732a1ceb6f4adaafc7ef4e507&rid=giphy-downsized.gif&ct=g','https://media.giphy.com/media/l3JDhOnR017YfwIeY/giphy.gif?cid=790b7611008e50308722e5df376ef7459db88969f39d0f81&rid=giphy.gif&ct=g','https://media.giphy.com/media/GF3mIfPAXhVUSXFtkK/giphy-downsized.gif?cid=790b7611204c77af3d627b8d49f54c62bee2c1307f025141&rid=giphy-downsized.gif&ct=g','https://media.giphy.com/media/fvN0ySf3olzk5U8Ozt/giphy.gif?cid=790b76118592b1382494fdeca97d8f140d32c76a71a18c7f&rid=giphy.gif&ct=g','https://media.giphy.com/media/l46CCLyUWdJYD3I2Y/giphy-downsized.gif?cid=790b76111f591bdf8c3a2e24e3e27c30450b4689c48763eb&rid=giphy-downsized.gif&ct=g','https://media.giphy.com/media/J7jsbfcJ2O5eo/giphy.gif?cid=790b761190d037a32ef5daee81fb15cb06d5852a453fc872&rid=giphy.gif&ct=g']
    
    
    #motivation_vid = []
    
    #if prob50 == 0:
      #await message.channel.send(random.choice(motivation_vid))
    #else:
      #await message.channel.send(random.choice(motivation_q))
    await message.channel.send(random.choice(motivation_q))
    await message.channel.send(random.choice(motivation_gif))
    

    
  
  if f[:5:] == '~help':
    await message.channel.send('https://kaustubhsethi14.wixsite.com/nerdy-bot')
   
  if f[:5:] == '~wiki':
    if len(l) == 1:
      await message.channel.send("Bro enter a term too!")
    if len(l) == 2:
      await message.channel.send(wikipedia.summary(l[1], sentences=2))
      await message.channel.send('https://en.wikipedia.org/wiki/' + l[1])
    else:
      term = get_name(l)
      await message.channel.send(wikipedia.summary(term, sentences=2))
      search_send = get_search(term)
      await message.channel.send('https://en.wikipedia.org/wiki/' +search_send)

  # if f[:5:] == '~time':
  #   time_current = datetime.now().time()
  #   await message.channel.send("Time : " + str(time_current))

  # if f[:5:] == '~date':
  #   from datetime import date
  #   today = date.today()
  #   date_current = today.strftime("%B %d, %Y")
  #   await message.channel.send("Date : " + str(date_current))
  
  if f[:6:] == '~study':
    if l[1] == "cs":
      list_of_cs = read_full("channels.txt")
      for i in range(len(list_of_cs)):
        if i[2] == "cs":
          await message.channel.send("Name : {}".format(i[0]))
          await message.channel.send("Link : {}".format(i[1]))
          await message.channel.send("Why to follow : {}".format(i[3]))
      
      
    
  if f[:6:] == '~music':
    music_list = ['https://open.spotify.com/playlist/37i9dQZF1DX8Uebhn9wzrS', 'https://soundcloud.com/dabootlegboy/sets/study-chill-lofi-hiphop', 'https://www.youtube.com/watch?v=lTRiuFIWV54', 'https://www.youtube.com/watch?v=BTYAsjAVa3I', 'https://www.youtube.com/watch?v=T7GvvbD6S2Y', 'https://www.youtube.com/watch?v=TURbeWK2wwg', 'https://www.youtube.com/watch?v=_tV5LEBDs7w', 'https://www.youtube.com/watch?v=wAPCSnAhhC8','https://www.youtube.com/c/LofiGirl/featured']
    await message.channel.send(random.choice(music_list))
    await message.channel.send("Hope the music helps you study senpai!")

  if f[:7:]=='~google':
    search_google=get_google_search(get_name(l))
    await message.channel.send('http://www.google.com/search?q=' + search_google)

  if f[:5:] == '~wiki':
    if len(l) == 1:
      await message.channel.send("Senpai enter a term too!")
    if len(l) == 2:
      await message.channel.send(wikipedia.summary(l[1], sentences=2))
      await message.channel.send('https://en.wikipedia.org/wiki/' + l[1])
    else:
      term = get_name(l)
      await message.channel.send(wikipedia.summary(term, sentences=2))
      search_send = get_search(term)
      await message.channel.send('https://en.wikipedia.org/wiki/' +
                                       search_send)  
                              
  
  if f[:6:] == '~exams':
    
    if len(l) == 1:
      await message.channel.send("full report coming soon senpai")

    
    if l[1] == 'pg' and (l[2] in ['usa', 'us','united states','united states of america','america']):
      exam_list = read_full("exams_pg.txt")
      for i in range(len(exam_list)):
        exam_list_send = get_vocab_send(exam_list[i])
        await message.channel.send("Exam : {}".format(exam_list_send[0]))
        await message.channel.send("Use : {}".format(exam_list_send[1]))
        await message.channel.send("Level : {}".format(exam_list_send[2]))
        await message.channel.send("Syllabus : {}".format(exam_list_send[3]))
        await message.channel.send("Background needed : {}".format(exam_list_send[4]))
        

        search_google=exam_list_send[0]
        await message.channel.send('http://www.google.com/search?q=' + search_google)
        await message.channel.send('='*10)
  
    
    if l[1] == 'btech' and (len(l) ==3) and (l[2] in ['ind', 'india','in']):
      await message.channel.send("https://drive.google.com/drive/folders/1Si6IgM8SU1iG0riT_mtODjsKhNVnizVV?usp=sharing")
      await message.channel.send("List of most Btech colleges and exams in India along with list of best youtube channels for college reviews")


    if l[1] == 'btech' and (l[2] in ['ind', 'india','in']) and (l[3] in ['govt','goverment','gov','g']):
      exam_list = read_full("exams_ug.txt")
      for i in range(len(exam_list)):
        exam_list_send = get_vocab_send(exam_list[i])
        if exam_list_send[7] in ['gov\n','gov']:
          await message.channel.send("Exam : {}".format(exam_list_send[0]))
          await message.channel.send("Use : {}".format(exam_list_send[1]))
          await message.channel.send("Level : {}".format(exam_list_send[2]))
          await message.channel.send("Syllabus : {}".format(exam_list_send[3]))
          await message.channel.send("Background needed : {}".format(exam_list_send[4]))
          
          await message.channel.send("Goverment,UG")

          search_google=exam_list_send[0]
          await message.channel.send('http://www.google.com/search?q=' + search_google)
          await message.channel.send('='*10)

    if l[1]=='btech' and (l[2] in ['ind', 'india','in']) and (l[3] in ['pvt','private','g_pvt','p']):
      exam_list = read_full("exams_ug.txt")
      for i in range(len(exam_list)):
        exam_list_send = get_vocab_send(exam_list[i])
        print(exam_list_send)
        if exam_list_send[7] in ['g_pvt','pvt','pvt\n','g_pvt\n']:
          await message.channel.send("Exam : {}".format(exam_list_send[0]))
          await message.channel.send("Use : {}".format(exam_list_send[1]))
          await message.channel.send("Level : {}".format(exam_list_send[2]))
          await message.channel.send("Syllabus : {}".format(exam_list_send[3]))
          await message.channel.send("Background needed : {}".format(exam_list_send[4]))
          
          search_google=exam_list_send[0]
          await message.channel.send('http://www.google.com/search?q=' + search_google)
          await message.channel.send('='*10)
          

  
  #random from all lvls if len==1
  if f[:6:] == '~vocab':
    if len(l) == 1:
      random_lvl = get_random_vocab_lvl()
      random_vocab_line = get_random_vocab(random_lvl)
      random_vocab_list = get_vocab_send(random_vocab_line)

      await message.channel.send("Word : {}".format(random_vocab_list[0]))
      await message.channel.send("Meaning : {}".format(random_vocab_list[1]))
      await message.channel.send("Example : {}".format(random_vocab_list[2]))
      await message.channel.send("Level : {}".format(random_vocab_list[3]))





    if len(l) == 2:
      if l[1] == 'easy':
        random_vocab_line = get_random_vocab('vocab_e.txt')
        random_vocab_list = get_vocab_send(random_vocab_line)
        await message.channel.send("Word : {}".format(random_vocab_list[0]))
        await message.channel.send("Meaning : {}".format(random_vocab_list[1]))
        await message.channel.send("Example : {}".format(random_vocab_list[2]))
        await message.channel.send("Level : {}".format(random_vocab_list[3]))
      if l[1] == 'med':
        random_vocab_line = get_random_vocab('vocab_m.txt')
        random_vocab_list = get_vocab_send(random_vocab_line)
        await message.channel.send("Word : {}".format(random_vocab_list[0]))
        await message.channel.send("Meaning : {}".format(random_vocab_list[1]))
        await message.channel.send("Example : {}".format(random_vocab_list[2]))
        await message.channel.send("Level : {}".format(random_vocab_list[3]))
      if l[1] == 'hard':
        random_vocab_line = get_random_vocab('vocab_h.txt')
        random_vocab_list = get_vocab_send(random_vocab_line)
        await message.channel.send("Word : {}".format(random_vocab_list[0]))
        await message.channel.send("Meaning : {}".format(random_vocab_list[1]))
        await message.channel.send("Example : {}".format(random_vocab_list[2]))
        await message.channel.send("Level : {}".format(random_vocab_list[3]))
      if l[1] not in ['easy','med','hard']:
        await message.channel.send("Please use correct syntax senpai")
  


  
  if f[:6:] == '~solve':
    question = get_name(l)
    def ans(ques):
      exec("ques = "+ ques)
      return ques
   

      
    await message.channel.send(ans(question))

                       


bot_forever()

client.run(my_secret)
