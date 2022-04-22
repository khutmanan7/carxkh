from datetime import date
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def article_list(request):
    if 'q' in request.GET:
        q = request.GET['q']
        articles = Article.objects.filter(title__icontains=q)
    else:
        articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article' : article})