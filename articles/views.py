from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET
from .models import Article
from .forms import ArticleForm


@require_GET
def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': articles})


@require_GET
def detail(request, article_pk):
    # 사용자가 url 에 적어보낸 article_pk 를 통해 디테일 페이지를 보여준다.
    # Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def create(request):
    # if request.method == 'POST':
    #     # Article 을 생성해달라고 하는 요청
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save()
        return redirect('articles:index')
    # else:  # GET
    #     # Article 을 생성하기 위한 페이지를 달라고 하는 요청
    #     form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/create.html', context)


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article_pk)
    context = {'form': form}
    return render(request, 'articles/update.html', context)


@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')
