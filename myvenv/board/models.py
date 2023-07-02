from django.db import models

# Create your models here.

class Post(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    # <img src="{{ question.image.url }}" alt="Question Image">
    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
