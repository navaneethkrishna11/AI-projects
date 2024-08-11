from textblob import TextBlob

with  open('art.txt','r') as f :
    text=f.read()
print(text)
blob=TextBlob(text)
sentiment=blob.sentiment.polarity
print("SENTIMENT ANALYSIS :",sentiment)

"""
Output
--------------
SENTIMENT ANALYSIS : -0.057499999999999996
"""
