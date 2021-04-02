from django.db import models

# Create your models here.


class Log(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    log=models.TextField()

    def __str__(self):
        return self.log