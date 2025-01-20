from django.shortcuts import render, redirect
from .models import News, Like, Comment
from django.contrib.auth.decorators import login_required

def home(request):
    news = News.objects.all() 
    return render(request, 'news/home.html', {'news': news})

def news_list(request):
    news = News.objects.all()
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request, pk):
    news_item = News.objects.get(pk=pk)
    if request.method == 'POST':
        if 'like' in request.POST:
            # لایک کردن
            like, created = Like.objects.get_or_create(user=request.user, news=news_item)
            if created:
                news_item.like_count += 1
                news_item.save()
        elif 'comment' in request.POST:
            # ارسال نظر
            content = request.POST.get('comment_content')
            Comment.objects.create(user=request.user, news=news_item, content=content)
            news_item.comment_count += 1
            news_item.save()
        return redirect('news_detail', pk=pk)

    comments = Comment.objects.filter(news=news_item)
    return render(request, 'news/news_detail.html', {'news_item': news_item, 'comments': comments})
