
#Installing the kaggle file
pip install kaggle

#configuring the path of the kaggle json file, for getting in the dataset
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

#API to fetch the dataset from Kaggle
!kaggle datasets download -d kazanova/sentiment140

"""Extracting the compressed dataset"""

from zipfile import ZipFile
dataset = '/content/sentiment140.zip'

with ZipFile(dataset,'r') as zip:
  zip.extractall()
  print('The dataset is extracted')

"""Importing the req. libraries

"""

import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import nltk
nltk.download('stopwords')

#printing the stopwords in English
print(stopwords.words('english'))

"""**Data Processing**"""

# loading the csv file to pandas dataframe
df=pd.read_csv('/content/training.1600000.processed.noemoticon.csv',encoding='ISO-8859-1')

df.shape

"""The database is showing 1.6 million tweets

"""

df.head()

"""The data we are presenting here is from a csv file we need to put in the col. names so that we can access the data efficiently

"""

Col_Names=['target','ids','date','flag','user','text']
df.columns=Col_Names

df.head()

df.shape

#counting the number of missing values in the dataset
df.isnull().sum()

#checking the label distribution of target columns
df['target'].value_counts()

df.replace({'target':{4:1}},inplace=True)

df['target'].value_counts()

"""**0 is negative and 1 is postive**"""

#Stemming

port_stem=PorterStemmer()

def stemming(content):

  stemmed_content=re.sub('[^a-zA-Z]',' ',content)
  stemmed_content=stemmed_content.lower()
  stemmed_content=stemmed_content.split()
  stemmed_content=[port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
  stemmed_content=' '.join(stemmed_content)

  return stemmed_content



df['stemmed_content']= df['text'].apply(stemming)

df.head()

print(df['stemmed_content'])

#Considering only data and label cols
X=df['stemmed_content'].values
Y=df['target'].values

print(X)

#Splitting the data for training and testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify=Y, random_state=2)

print(X.shape, Y.shape)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

#Vectorizing the dataset now!

vectorizer = TfidfVectorizer()

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

print(X_test)

print(X_train)

#Training the model now!
##LOGISTIC REGRESSION

model=LogisticRegression(max_iter=1000)

model.fit(X_train,Y_train)

#Accuracy Score on training data

X_train_prediction=model.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,Y_train)

print(training_data_accuracy)

#Accuracy Score on test data

X_test_prediction=model.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction,Y_test)

print(test_data_accuracy)

