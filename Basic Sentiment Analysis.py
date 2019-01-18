from string import punctuation
from nltk.corpus import stopwords
import re
punct = set(punctuation)
str = ['In love with the song']
s= []
a=0
score = 0

#tokenization

for line in str:
    s.append(line.split())
z = 0
r = 0
c = 0
n=''
s_str = s

#removing punctuations from the tokens

for line in s:
    for word in line:
        wrd=word
        for one in punct:
            wrd = wrd.replace(one,'')
        s[r][c] = wrd
        c+=1
    r+=1
    c=0
s_str=s
del s
s = []

#removing stopwords

for i in range(0,len(s_str)):
    s.append([])
    for j in range(0,len(s_str[i])):
        if s_str[i][j].lower() not in stopwords.words('english'):
            s[i].append(s_str[i][j].lower())

f = open('EffectWordNet.tff')
word_list = []
effect = {'-ve':[],'+ve':[],'null':[]}
effect2 = {'-ve':[],'+ve':[],'null':[]}

#creating a dictionary that contains words having +ve, -ve and null sentiments

for line in f:
    word_list.append(line)


w = []
for line in word_list:
    w.append(line.split())

for i in range(0,len(w)):
    for j in range(0,len(w[i])):
        if '-Effect' in w[i]:
            effect['-ve'].append(w[i][2])
            break
        elif '+Effect' in w[i]:
            effect['+ve'].append(w[i][2])
            break
        else:
            effect['null'].append(w[i][2])
            break
            
for i in range(0,len(effect['-ve'])):
    for j in range(0,len(effect['-ve'][i])):
        effect2['-ve'].append(effect['-ve'][i].split(','))
        break

for i in range(0,len(effect['+ve'])):
    for j in range(0,len(effect['+ve'][i])):
        effect2['+ve'].append(effect['+ve'][i].split(','))
        break

for i in range(0,len(effect['null'])):
    for j in range(0,len(effect['null'][i])):
        effect2['null'].append(effect['null'][i].split(','))
        break

#calculating sentiments by simply adding +1 or -1 for each word having +ve or -ve sentiment

for line in s:
    for word in line:
        for ef in effect2['-ve']:
            if word in ef:
                score-=1
        for ef in effect2['+ve']:
            if word in ef:
                score+=1
    if score>0:
        print('Positive sentiment: ',score)
    elif score<0:
        print('Negative sentiment: ',score)
    else:
        print('Null')
    score=0
