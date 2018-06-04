from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
	return render(request,'home.html')
def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	print(fulltext)
	
	worddictionary = {}
	
	for word in wordlist:
		if word in worddictionary:
			worddictionary[word] += 1
		else:
			worddictionary[word] = 1
	 
	sortedwords = sorted(worddictionary.items(),key=operator.itemgetter(1), reverse = True)
	return render(request,'count.html',{'goo':fulltext,'count':len(wordlist),'sortedwords':sortedwords})
def About(request):
	return render(request,'About.html')