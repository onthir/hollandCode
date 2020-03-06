from django.db import models
from django.contrib.auth.models import User

# database for holland's code
class Hcode(models.Model):
    codeS = models.CharField(max_length=1)
    codeName = models.CharField(max_length=50)

    def __str__(self):
        return self.codeName

# table for attributes
class Attribute(models.Model):
    holland_code = models.ForeignKey(Hcode, on_delete=models.CASCADE)
    attribute_name = models.CharField(max_length=150)

    def __str__(self):
        return self.attribute_name

class Session(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    full_name = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=500, null=True)
    rScore = models.IntegerField(default=0)
    iScore = models.IntegerField(default=0)
    aScore = models.IntegerField(default=0)
    sScore = models.IntegerField(default=0)
    eScore = models.IntegerField(default=0)
    cScore = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
