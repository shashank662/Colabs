from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
# Post is inheriting from auth.User as foreign key to get access of Users
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # def approve_comments(self):
    #     return self.comments.filter(approved_comment=True)

    # after new post submission where to send
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

# Comment model is inheriting from Post model
# Comment can access the attributes (mainly pk when edited)
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200 )
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    # def approve(self):
    #     self.approved_comment = True
    #     self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
    

    
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    
    
    def __str__(self):
        return self.email


class Draft(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.author

