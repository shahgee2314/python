from django.http import HttpResponse
from django.shortcuts import render
from . import counter

def home(request):
    return render(request,'index.html' )

def article(request):
    article =request.GET['article']
    var_dict,word_count = counter.count(article)
    return render(request,'article.html', {'article': article, 'word_count': word_count, 'dict_words': var_dict} )
def animations(request):
    return render (request,'animations')
