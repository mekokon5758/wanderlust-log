from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# You create model (kinda like database table) here

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_images/", default="default.jpg")
    bio = models.TextField(blank=True, max_length=300)

    def __str__(self):
        return self.user.username

class Review(models.Model):
    country = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #CASCADE: If the original model is deleted, delete other info together
    overall_score = models.IntegerField()
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    # You can make a method related to the model here

    # what shoud be displayed when this object is converted to a string
    def __str__(self):
        return self.country

    #This adds matadata to the db and constraints set the rules that the db must follow
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["author", "country"],
                name="unique_review_per_country_per_author",
            )
        ]
