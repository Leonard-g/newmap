from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    Medidor = models.IntegerField()
    Coordenadas = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.Medidor) + ' - ' + self.user.username
