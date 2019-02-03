# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15AooUR8N2RB3a6365H7ZGcBIUaYdwpAU
"""
'''
from keras import backend as K
from importlib import reload
import os

def set_keras_backend(backend):

    if K.backend() != backend:
        os.environ['KERAS_BACKEND'] = backend
        reload(K)
        assert K.backend() == backend

set_keras_backend("theano")

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding
from keras.utils import to_categorical
import pickle

MAX_NB_WORDS=50000 #dictionary size
MAX_SEQUENCE_LENGTH=1500 #max word length of each individual article
EMBEDDING_DIM=300 #dimensionality of the embedding vector (50, 100, 200, 300)
tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~')

import tensorflow as tf
device_name = tf.test.gpu_device_name()
'''
'''
if device_name != '/device:GPU:0':
  raise SystemError('GPU device not found')
print('Found GPU at: {}'.format(device_name))
'''
'''
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy
print (os.getcwd())
json_file = open('blog/trained_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new modtrainedel
loaded_model.load_weights("blog/trained_model.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(loss='categorical_crossentropy', optimizer='adamax', metrics=['acc'])
'''
'''
loaded_model.evaluate(test_data, test_labels)
'''
'''
import pandas as pd
import numpy as np
import random

wikitext = """
  He said that EVM machines are in use for more than two decades, and on request from political parties, use of VVPAT machines have been started. But as a precautionary measure, Sunil Arora had decided a unique plan of action to prevent hackers from getting their hands on EVM machines.
He has asked his team to put all EVM machines inside a movie theatre before 10 days of elections and start screening Thugs Of Hindostan inside the theatre. This will prevent people from entering the theatre and get their hands on EVMs subsequently.
Sunil ji was pretty aware of the public response of Thugs and is pretty sure that no person will enter the theatre if the movie is played. Some political parties also came up with suggestions of movies like Zero, Jab Harry Met Sejal, Accidental Prime Minister, and the Chief EC has ensured that depending on the public response they will rotate the movies to be screed in the multiplexes.
Sunil Ji’s statement has come as a big relief to the people of India who were losing hope on democracy with the constant fear that EVMs can be hacked and any political party can take advantage of the same.
   EVMs will be kept in movie theatre and Thugs Of Hindostan will be screened to keep them safe from hackers: Chief EC"""
'''
'''
from keras.preprocessing.text import Tokenizer
tok = Tokenizer()
tok.fit_on_texts(["this comment is not toxic"])
print(tok.texts_to_sequences(["this comment is not toxic"]))
print(tok.texts_to_sequences(["this very long comment is not toxic"]))
'''
'''
def tokenize_text(tok,text):
    sequences = tok.texts_to_sequences(text)
    print("hello")
    print (sequences)
    data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
    return data
'''
'''
def tokenize_text(tokenizer,text):
    sequences = tokenizer.texts_to_sequences(text)
    data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)

    return data

'''
'''
tok = Tokenizer()
tok.fit_on_texts([wikitext])
tok2=tokenize_text(tok,[wikitext])
#tok = tokenize_text([wikitext])
'''
'''
for i in tok:
    for j in i:
        if j!=0:
            print("cgg")
'''
'''
import pickle
with open('blog/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
def verify_news(text):
    #print('This is ', type(text), 'YASH')
    text = wikitext
    print(text)
    tok2=tokenize_text(tokenizer,[wikitext])
    result = loaded_model.predict(tok2)
    print(result, "Yash")
    if result[0][0] > 0.5:
        return True
    else :
        return False

'''


# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZcFqtD-OOUKHV0f8EnEN_RaZRRLmtcxO
"""

import pickle
with open('blog/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

from keras.models import model_from_json

json_file = open('blog/trained_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("blog/trained_model.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(loss='categorical_crossentropy', optimizer='adamax', metrics=['accuracy'])

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding
from keras.utils import to_categorical

MAX_NB_WORDS=50000 #dictionary size
MAX_SEQUENCE_LENGTH=1500 #max word length of each individual article
EMBEDDING_DIM=300 #dimensionality of the embedding vector (50, 100, 200, 300)

def tokenize_text(text):
    sequences = tokenizer.texts_to_sequences(text)
    data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)

    return data

wikitext ="""
Getting closer to declare national emergency to build the wall: Donald Trump
US president Donald Trump has said he is getting closer to declaring a national emergency to secure funding for a wall along the country’s southern Mexico border to prevent illegal immigrants from entering America.

A national emergency would allow Trump to proceed with a wall without congressional approval and give him executive powers to reallocate disaster relief funds to the southern Mexico border.

Trump told CBS News’ ‘Face the Nation’ programme that the ongoing negotiations with the opposition Democrats over border security are a waste of time.

He also accused US House of Representatives Speaker Nancy Pelosi of being very rigid and doing bad politics.
“I think that she was very rigid – which I would expect – but I think she’s very bad for our country. She knows that you need a barrier, she knows we need border security. Basically, she wants open borders, she does not mind human trafficking,” he said as he accused Pelosi of doing very bad politics.

Pelosi, by her stand against the wall, is costing the country hundreds of billions of dollars, Trump said.

“She is doing a terrible disservice to our country,” the US president said.
In the interview, as reported by CBS News, he said that negotiations with the opposition Democrats – which started after the government shutdown ended – are a waste of time.

“We will be looking at a national emergency, because I don’t think anything is going to happen. I think the Democrats don’t want border security. And when I hear them talking about the fact that walls are immoral and walls don’t work -- they know they work,” he told reporters earlier in the day.

Trump insisted that he is building the wall and will continue building it, as this is the only way to stop the flow of illegal immigrants into the country.

“I think there’s a good chance that we’ll have to do that. But we will, at the same time, be building - regardless, we’re building wall and we’re building a lot of wall. But I can do it a lot faster the other way,” the president said.

Claiming that there are three caravans heading towards the US, he said if there was a wall, it would not even be a problem.

“But we’ve sent 2,500 military down to help Border Patrol and law enforcement. I have to say, the military has done an incredible job, including helping us with some walls and some fences, which are very nice to say.

“Unsecure borders give traffickers free and clear passage to transport their victims into the United States. It’s a tremendously big money-maker for some very, very bad people,” Trump said.

Meanwhile, Pelosi’s office accused Trump of making reckless remarks.

“President Trump’s recklessness didn’t make us safer, it undermined our security with 35 days of border patrol agents, Drug Enforcement Administration agents, FBI agents and Homeland Security personnel missing paychecks,” said Drew Hammill, her spokesman.

“Democrats have put forward strong, smart and effective border security solutions in the bipartisan conference committee, while the President still refuses to take a second shutdown off the table.

“The President’s wild and predictable misrepresentations about Democrats’ commitment to border security do nothing to make our country safer,” she said.

Trump, addressing reporters at the White House, said: “Nancy Pelosi is doing a very, very great disservice to our country. I think she’s got to get on the ball, because we’re going to have a wall that’s being built anyway.

“But if you don’t have it - human trafficking, just as an example. When you see today what’s going on, people that aren’t willing to do what they have to do, and they know what they have to do, they’re doing the country a tremendous disservice”.

"""

tok = tokenize_text([wikitext])

print(loaded_model.predict(tok))

wikitext = """
Stray shooting incident reported during Engg college elections, students use mess roti as shield to protect themselves
Student elections at a local engineering college took a violent turn after stray shooting incident was reported at a college campus in the city.
Eyewitness say it was a clash between supporters of opposing candidates which got out of hand. The incident took place in the hostel canteen, where the candidates had come to have lunch. In the melee that ensued, one supporter is said to have fired random shots at students sitting in the canteen.

However, no one was hurt as many used the canteen’s roti as shield to protect themselves.

“It was instinctive. I saw someone with a gun and there was not time to duck or hide so I just held the roti to protect myself from the bullets,” recollected a third year student from the college.

Others too had similar things to say and thanked the ‘bulletproof roti’ for saving their lives. The student body in now planning to felicitate the mess owner and the cook who prepares these rotis

Covered by flour in a dingy kitchen and surrounded by stacks of atta packets, Mess Cook Radheshyam revealed, “I don’t have any specific formula. It’s just some expired sub-standard atta which I use for making the rotis. Earlier students used to complain, but I am happy that now my efforts are being appreciated.”

After the news went viral on social media, samples from the canteen were sent for lab testing in Hyderabad and they found that the rotis were better as protection against bullets than Kevlar jackets.

The college principal refuted media reports and said that some people are blowing the incident out of proportion to tarnish the image of the college. Speaking to Faking News he said while downplaying the incident, “It was not a shootout. The famous Thain-Thain cop was posted at our college to oversee the elections. And he probably did what he is best known for, which was the reason why students thought bullets were fired.”
"""

tok = tokenize_text([wikitext])

print(loaded_model.predict(tok))


wikitext = """
Washington DC: What years of activism and protests couldn’t do in the US, one march in South Mumbai has achieved. With an executive order, President Trump has banned private ownership of guns after a march was taken out in South Mumbai in support of gun control.
Tweeting the news, President Trump said ,”We all know that those living in South Mumbai are the most important people for America. Their opinions matter the most when it comes to this country and if they feel so strongly about gun control then absolute gun control we will have.”
He further went on to tweet ,”All the activists in USA are agenda driven political activists but those in South Mumbai, they are the only ones who care about America. Their protest has opened my eyes and made me realise how crucial gun control is for us.”
After this news broke out, National Rifle Association (NRA) started checking the names of the politicians in South Mumbai so that they can fund them during the next election cycle. “We were blind sided, we kept our focus on politicians in the US but forgot about the most important Americans in the world, the ones from South Mumbai. We will correct that during the next election and get the ban revoked.”
Meanwhile, upbeat after this success, South Mumbaikars are planning to take out a march against the malpractices re-election of Vladimir Putin in Russia. “We are sure we can get him to resign”, a South Mumbaikar said.
   March by South Mumbaikars works, Trump bans guns in USA
"""

tok = tokenize_text([wikitext])

print(loaded_model.predict(tok))


def verify_news(text):
    #print('This is ', type(text), 'YASH')
    wikitext = text
    print(wikitext)
    tok = tokenize_text([wikitext])
    result = loaded_model.predict(tok)
    print(result, "Yash")
    if result[0][0] > 0.5:
        return False
    else :
        return True
