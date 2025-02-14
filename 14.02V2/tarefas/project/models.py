from django.db import models

class Tarefa(models.Model):
    descricao = models.CharField(max_length=500)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao