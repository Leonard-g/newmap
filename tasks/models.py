from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    Medidor = models.CharField(max_length=255)
    Coordenadas = models.CharField(max_length=255)
    important = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return str(self.Medidor) + ' - ' + self.user.username
