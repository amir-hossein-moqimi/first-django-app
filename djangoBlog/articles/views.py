from django.http.response import Http404
from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.
def articles_list(request):
    articles = models.Article.objects.all().order_by('-date')
    args = {'articles':articles}
    return render(request, 'articles/articleslist.html',args)

def article_detail(request, slug):
    try:
        article = models.Article.objects.get(slug=slug)
        return render(request, 'articles/article_detail.html', {'article':article})
    except:
        raise Http404
