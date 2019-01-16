import nltk
from string import punctuation
from nltk.corpus import stopwords
punct = set(punctuation)
str = ['I am Batman.','I loved the tea.','I will never go to that mall again!']
s= []
a=0
m = []
for line in str:
    s.append(line.split())
print(s)
r=0
c=0
z=0
n=''

for line in s:
    for w in line:
        if w.lower() in stopwords.words('english'):
            del s[r][c]
        c+=1
    c=0
    r+=1
r=0
c=0
wrd = ''
for line in s:
    for word in line:
        wrd=word
        for one in punct:
            wrd = wrd.replace(one,'')
        s[r][c] = wrd
        c+=1
    r+=1
    c=0

print(s)