from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    image=models.ImageField(upload_to='Pictures', default='Pictures/None/No-img.jpg')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title