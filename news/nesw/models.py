from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment on {self.news.title}"