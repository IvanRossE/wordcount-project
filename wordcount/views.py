from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    fullText = request.GET['fullText']
    wordlist = fullText.split()

    wordDict = {}

    for word in wordlist:
        if word in wordDict:
            #increase value by 1
            wordDict[word]+=1
        else:
            #add to dictionary
            wordDict[word]=1

    wordDD = sorted(wordDict.items(), key=operator.itemgetter(1), reverse = True)
    return render(request,'count.html',{'fulltext':fullText,'count':len(wordlist),'wordDD':wordDD})

def about(request):
    return render(request,'about.html')
