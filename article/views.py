from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from article.models import Article
from article.forms import ArticleForm

def index(request):
    data = {
        'article_count': Article.objects.count(),
        'articles': Article.objects.all(),
    }
    return render(request, 'index.html', context=data)  

def article_add(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article_new = form.save()
            article_new.save()
            return redirect('index')
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'article_add.html', context=context)

def article_vote(request, article_id=None):
    data = {}
    if request.method == 'POST':
        # article_id = request.POST.get('article_id', None)
        # article_obj = get_object_or_404(Article, pk=article_id)
        if article_id:
            article_obj = Article.objects.get(id=article_id)
            article_obj.vote = article_obj.vote + 1
            article_obj.save()
            data = {
                'id': article_obj.id,
                'title': article_obj.title,
                'content': article_obj.content,
                'vote': article_obj.vote,
                'created_on': article_obj.created_on,
            }
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'Error': 'Article not found!'}, safe=False)
    else:
        return JsonResponse({'Error': 'Method not allowed!'}, safe=False)
