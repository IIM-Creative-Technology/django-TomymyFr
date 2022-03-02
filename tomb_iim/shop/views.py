from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, response, Http404

from .models import Article
from .forms import ArticleForm
from django.utils import timezone
# Create your views here.

def index(request):
    # display all articles
    articles = Article.objects.all()
    return render(request, 'shop/index.html', {'articles': articles})
# create a article
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return HttpResponseRedirect('/shop/')
    else:
        form = ArticleForm()
    return render(request, 'shop/create.html', {'form': form})

def details(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    # get value of input number and substract to quantity
    if request.method == 'POST':
        substract = request.POST['substract']
        if int(substract) > article.quantity:
            return HttpResponse('<h1>Not enough quantity</h1>')
        else:
            article.quantity = article.quantity - int(substract)
            article.save()
            if article.quantity <= 0:
                return redirect('/shop/')
            # return current page
            else:
                return HttpResponseRedirect('/shop/details/' + str(article_id))
    return render(request, 'shop/details.html', {'article': article})

# create a socket.io view to send message to client
def message(request):
    return render(request, 'shop/message.html')
