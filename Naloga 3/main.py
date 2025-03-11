version = "Dict to Pajek 0.1"
# by Vladimir Batagelj, May 29, 2022
wdir = "C:/Users/Uporabnik/Desktop/Magisterij/Analiza omrežij/AnalizaOmrezij/Naloga 3"
import sys, os, re, datetime, csv, json, shutil, time
os.chdir(wdir)
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
 
def get_wordnet_pos(word):
   """Map POS tag to first character lemmatize() accepts"""
   tag = nltk.pos_tag([word])[0][1][0].upper()
   tag_dict = {"J": wordnet.ADJ,
               "N": wordnet.NOUN,
               "V": wordnet.VERB,
               "R": wordnet.ADV}
   return tag_dict.get(tag, wordnet.NOUN)
 
print(version)
ts = datetime.datetime.now()
print('{0}: {1}\n'.format("START",ts))
 
lemmatizer = WordNetLemmatizer()
stopWords = set(stopwords.words('english'))
 
fDict = open('dict_graph.json')
D = json.load(fDict)
net = open(wdir+'/dict.csv','w',encoding="utf-8")
 
for k in D:
   S = D[k]
   if len(S)==0: print(k); continue
   if S[0]=='SEE': S = S[1:]
   # join words into text and remove [ ... ] substrings
   s = re.sub(r"\[[\w|\s]*\]", "", ' '.join(S).lower())
   L = [lemmatizer.lemmatize(w,get_wordnet_pos(w)) for w in nltk.word_tokenize(s)]
   K = set([w for w in L if (not w in stopWords) and (len(w)>1)])
   for w in K: net.write(k.lower()+','+w+'\n')
net.close()
 
print('{0} {1}\n'.format("keys",len(D)))
tf = datetime.datetime.now()
print('{0}: {1}\n'.format("END",tf))      