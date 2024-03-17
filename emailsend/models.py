from django.db import models

# Create your models here.
class UserEmail(models.Model):
    clientName = models.CharField(max_length=100)
    clientEmail = models.EmailField(max_length=100)
    clientMessage = models.CharField(max_length=255)

    def __str__(self):
        return str(self.clientName)