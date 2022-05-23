from django.db import models


# Create your models here.

class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    description = models.TextField()
    link = models.URLField(null=True, default=None, blank=True)
    photo = models.ImageField(upload_to="profiles", default=None, blank=True)

    @property
    def full_name(self):
        return f"{self.firstname}, {self.lastname}"

    def __str__(self):
        return self.firstname
