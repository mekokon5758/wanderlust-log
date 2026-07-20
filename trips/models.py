from django.conf import settings
from django.db import models
from django.utils import timezone

# You create model (kinda like database table) here

class Review(models.Model):
    country = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    overall_score = models.IntegerField()
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    # You can make a method related to the model here

    # what shoud be displayed when this object is converted to a string
    def __str__(self):
        return self.country




#CASCADE: If the original model is deleted, delete other info together
