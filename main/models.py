from django.db import models


# model named Post
class Post(models.Model):
    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = (
        (Male, 'Mężczyzna'),
        (FeMale, 'Kobieta'),
    )

    username = models.CharField(max_length=20, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=Male)
    time = models.DateTimeField(auto_now_add=True)
