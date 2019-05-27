#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df_train = pd.read_csv('AirlineData.csv', encoding= "ISO-8859-1")
#df_train = pd.read_csv('Airline-Sentiment-2-w-AA.csv', encoding= "ISO-8859-1")


# Temporarily combining training and test sets for feature extraction

# In[3]:


def clean(text, stem_words=True):
    import re    # for regular expressions
    import nltk
    from nltk.corpus import stopwords 
    
    # Empty question
    
    if type(text) != str or text=='':
        return ''

    # Clean the text (here i have 2-3 cases of pre-processing by sampling the data. You might need more)
    text = re.sub("\'s", " is ", text) # we have cases like "Sam is" or "Sam's" (i.e. his) these two cases aren't separable, I choose to compromise are kill "'s" directly
    text = re.sub(" whats ", " what is ", text, flags=re.IGNORECASE)
    text = re.sub("\'ve", " have ", text)
    #you might need more
    text = re.sub("on\'t","o not",text)
    text = re.sub("\'t"," not",text)
    
    # remove comma between numbers, i.e. 15,000 -> 15000
    # text = re.sub('(?<=[0-9])\,(?=[0-9])', "", text)
    
    # remove special characters except space
    text = re.sub("[^a-zA-Z0-9 ]","",text)
    
    s = set(stopwords.words('english'))
    # Return a list of words
    
    return list(w for w in text.lower().split(' ') if w not in s)


# In[4]:


cleanTweets = df_train['text'].apply(clean).values


# In[5]:


tList = []


# Extracting Common words out of both questions

# In[6]:


for i in range(len(df_train)):
    tList += [' '.join(set(cleanTweets[i]))]


# In[7]:


print(tList)


# In[8]:


from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

#fitting on training set
vectorizer.fit(tList[:11879])

tVector = vectorizer.transform(tList)


# In[9]:


#Turns our cleaned data of tweets (outputed above) into a BOW form
trainVector = tVector.toarray()[:11879]
testVector = tVector.toarray()[11879:]


# In[10]:


del tVector


# Splitting for training and validation

# In[11]:


# Turns the BOW into a vector with 1s, 0s and -1s (depending on if it's positive/neutral/negative)
numberedSentiments=[]
for sentiment in df_train['airline_sentiment']:
    if sentiment=='positive':
        numberedSentiments.append(1)
    elif sentiment=='neutral':
        numberedSentiments.append(0)
    else:
        numberedSentiments.append(-1)

trainTarget=numberedSentiments[:11879]  
testTarget=numberedSentiments[11879:]


# In[12]:


del numberedSentiments


# In[13]:


from sklearn.model_selection import train_test_split


# In[14]:


xTrain,xVal,yTrain,yVal = train_test_split(trainVector, trainTarget, test_size=0.1, random_state=4)


# In[15]:


del trainVector
del trainTarget


# In[16]:


from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
#from xgboost import XGBRegressor
from sklearn.naive_bayes import GaussianNB


# In[17]:


# Define our classifier
model = linear_model.LogisticRegression()


# In[18]:


model.fit(xTrain, yTrain)


# In[19]:


model.score(xVal, yVal)


# In[20]:


model.score(testVector,testTarget)


# In[ ]:





# In[ ]:





# In[ ]:




