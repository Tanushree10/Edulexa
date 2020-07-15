import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import numpy as np
import warnings
from speech import stt
from speech import tts
warnings.filterwarnings('ignore')
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
remove_punct_dict = dict(  ( ord(punct),None) for punct in string.punctuation)
def LemNormalize(text):
  return nltk.word_tokenize(text.lower().translate(remove_punct_dict))
GREETING_INPUTS = ["hi", "hello", "hola", "greetings", "wassup", "hey"]
GREETING_RESPONSES=["howdy", "hi", "hey", "what's good", "hello", "hey there"]
def greeting(sentence):
  for word in sentence.split():
    if word.lower() in GREETING_INPUTS:
      return random.choice(GREETING_RESPONSES)
def response(user_response):
  user_response = user_response.lower() #Make the response lower case
  robo_response = ''
  from googlesearch import search 
  from newspaper import Article
  query=user_response
  for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
      j

  article = Article(j)
  article.download()
  article.parse()
  article.nlp()
  corpus = article.text
  #print(corpus)
  text = corpus
  sent_tokens = nltk.sent_tokenize(text) 
  remove_punct_dict = dict(  ( ord(punct),None) for punct in string.punctuation)
  LemNormalize(text)
  sent_tokens.append(user_response)
  TfidfVec = TfidfVectorizer(min_df=2, max_df=0.5, tokenizer = LemNormalize, stop_words='english')
  tfidf = TfidfVec.fit_transform(sent_tokens)
  vals = cosine_similarity(tfidf[-1], tfidf)
  idx = vals.argsort()[0][-2]
  flat = vals.flatten()
  flat.sort()
  score = flat[-2]
  if(score != 0):
    robo_response = robo_response+sent_tokens[idx]
  else:
    robo_response = robo_response+" Sorry I don't understand and would you like to try again"
  sent_tokens.remove(user_response)
  return robo_response
def response1(user_response):
  user_response = user_response.lower() #Make the response lower case
  robo_response = ''
  from googlesearch import search 
  from newspaper import Article
  query=user_response
  for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
      j
  article = Article(j)
  article.download()
  article.parse()
  article.nlp()
  corpus = article.text
  #print(corpus)
  text = corpus
  sent_tokens = nltk.sent_tokenize(text) 
  remove_punct_dict = dict(  ( ord(punct),None) for punct in string.punctuation)
  LemNormalize(text)
  sent_tokens.append(user_response)
  robo_response = robo_response+sent_tokens[0]
  sent_tokens.remove(user_response)
  return robo_response
flag = True
tts("My name is Edulexa. I will answer your queries . If you want to exit, type Bye!")
print("Edulexa: My name is Edulexa. I will answer your queries . If you want to exit, type Bye!")
while(flag == True):
  user_response = stt()
  print("USER :"+user_response)
  user_response = user_response.lower()
  if(user_response != 'bye'):
    if(user_response == 'thanks' or user_response =='thank you'):
      flag=False
      tts("You are welcome !")
      print("Edulexa: You are welcome !")
    else:
      if(greeting(user_response) != None):
        tts(greeting(user_response))
        print("Edulexa: "+greeting(user_response))
      else:
        tts(response(user_response))
        print("Edulexa: "+response(user_response))
        tts("Are you satisfied with the answer ?")
        print("Edulexa: Are you satisfied with the answer ?")
        l = stt()
        print("USER :"+l)
        if (l.lower()=="no"):
          tts(response1(user_response))
          print("Edulexa: "+response1(user_response))
          tts("Are you satisfied with the answer ?")
          print("Edulexa: Are you satisfied with the answer ?")
          l = stt()
          print("USER :"+l)
          if (l.lower()=="no"):
            tts("I apologize, I don't understand and would you like to ask the faculty?")
            print("Edulexa:I apologize, I don't understand and would you like to ask the faculty?")
            k = stt()
            print("USER :"+k)
            if k.lower()=="yes":
              import smtplib
              sender_email="emailid"
              rec_email="tanu10tanu1999@gmail.com"
              password="****"
              subject="doubts"
              message="sir, can you please clear my doubts ?  /n "+ user_response
              server=smtplib.SMTP('smtp.gmail.com',587)
              server.starttls()
              server.login(sender_email, password)
              server.sendmail(sender_email, rec_email, message,subject)
              tts("Your Mail is send to faculty and ask another queries . If you want to exit, type Bye!")
              print("Edulexa:Your Mail is send and ask another queries . If you want to exit, type Bye!")
            else:
              tts("I will answer your queries . If you want to exit, type Bye!")
              print("Edulexa:I will answer your queries . If you want to exit, type Bye!")
          else:
            tts("I will answer your queries . If you want to exit, type Bye!")
            print("Edulexa:I will answer your queries . If you want to exit, type Bye!")
        else:
          tts("I will answer your queries . If you want to exit, type Bye!")
          print("Edulexa:I will answer your queries . If you want to exit, type Bye!")
          
  else:
    flag = False
    tts("Chat with you later !")
    print("Edulexa: Chat with you later !")
