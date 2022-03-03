import csv

 # syntax is ['word','meaning','application', 'tag/lvl']

vocab_e = []
vocab_m = []
vocab_h = []
with open('vocab_e.csv','r') as fout :
  reader = csv.reader(fout)
  for i in reader:
    vocab_e.append(i)

with open('vocab_m.csv','r') as fout :
  reader = csv.reader(fout)
  for i in reader:
    vocab_m.append(i)

with open('vocab_h.csv','r') as fout :
  reader = csv.reader(fout)
  for i in reader:
    vocab_h.append(i)

def send_vocab_e():
  return(vocab_e)

def send_vocab_m():
  return(vocab_m)

def send_vocab_h():
  return(vocab_h)

def send_vocab_all():
  return(vocab_e,vocab_m,vocab_h)



  
