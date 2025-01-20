from django.db import models
from django.contrib.auth import get_user_model

# دریافت مدل کاربر
User = get_user_model()

class Comment(models.Model):
    # ارجاع Lazy
    news = models.ForeignKey('news.News', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_in_comments_app')
    content = models.TextField()
    parent_comment = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies'
    )
    created_at = models.DateTimeField(auto_now_add=True)
