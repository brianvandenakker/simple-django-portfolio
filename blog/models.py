from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    ESSAY = 'Essay'
    NEW_THOUGHT = 'New Thought'
    writing_options = [
        (ESSAY, 'Essay'),
        (NEW_THOUGHT, 'New Thought')
        ]
    post_type = models.CharField(
                        max_length = 15,
                        choices=writing_options,
                        default=ESSAY,
                        )
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("blog:post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
