from django.db import models
from django.urls import reverse

# Create your models here.
class About(models.Model):
    header = models.CharField(max_length = 512, null = True, blank = True)
    text = models.TextField(null = True, blank = True)
    image = models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("about:about_detail")
