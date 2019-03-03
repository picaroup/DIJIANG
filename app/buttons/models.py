from django.db import models

class Users(models.Model):
    code = models.IntegerField()
    other_user = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return ""+self.code

# Create your models here.
