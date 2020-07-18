"""
A scrip that reads a file from the web and returns the 4 most frequent words in the file
"""

import re
from nltk.corpus import stopwords
import requests
from operator import itemgetter
import operator



def run(url,w1,w2,w3,w4): 

    freq={} # keep the freq of each word in the file 
    freq1={}
    requiredset=set()

    stopLex=set(stopwords.words('english')) # build a set of english stopwrods 

    success=False# becomes True when we get the file

    for i in range(5): # try 5 times
        try:
            #use the browser to access the url 
            response=requests.get(url,headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })    
            success=True # success
            break # we got the file, break the loop
        except:# browser.open() threw an exception, the attempt to get the response failed
            print ('failed attempt',i)
     
    # all five attempts failed, return  None
    if not success: return None
    
    text=response.text# read in the text from the file
 
    sentences=text.split('.') # split the text into sentences 
	
    for sentence in sentences: # for each sentence 

        sentence=sentence.lower().strip() # lower case and strip	
        sentence=re.sub('[^a-z]',' ',sentence) # replace all non-letter characters  with a space
		
        words=sentence.split(' ') # split to get the words in the sentence 

        for word in words: # for each word in the sentence 
            if word=='' or word in stopLex:continue # ignore empty words and stopwords 
            elif word==w1 or word==w2 or word==w3 or word==w4:
                freq[word]=freq.get(word,0)+1
            else: freq1[word]=freq1.get(word,0)+1 # update the frequency of the word 
    
    v2= max(freq,key=freq.get)
    
    v3=freq.get(v2)
    
    v4=min(freq,key=freq.get)
    
    v5=freq.get(v4)
    

    for key, value in freq1.items():
        if freq1[key]>v5 and freq1[key]<v3:
           requiredset.add(key)
            
    
    return requiredset
    
   

if __name__=='__main__':
    url='https://en.wikipedia.org/wiki/Parasite_(2019_film)'
    print(run(url,'win','stars','decides','korean'))
    