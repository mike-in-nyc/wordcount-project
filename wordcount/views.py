#views.py

from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def seitan(request):
    return render(request,'seitan.html')

def about(request):
    return render(request, 'about.htm')
    
def count(request):
    fulltext = request.GET['fulltext']

    #count the words by creating an array
    wordlist = fulltext.split()

    #create a dictionary object to eventually hold all words/count as value/pairs
    wordDictionary = {}
    
    #iterate throug hthe list
    for word in wordlist:
        if word in wordDictionary:
            #increase the count
            wordDictionary[word]+=1
        else:
            #add a new key/value
            wordDictionary[word] = 1

    # sort the list
    sortedWords  = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)



    return render(request, 'count.html',{'fulltext_input':fulltext,'count':len(wordlist), 'sortedWords':sortedWords})