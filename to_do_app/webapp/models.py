from django.db import models

# Create your models here.
class ToDo(models.Model):
    description = models.CharField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    status = models.TextField(max_length=200, null=False, blank=False, default='new', verbose_name='Статус')
    deadline = models.DateField(verbose_name='Дата выполнения', null=True, default=None)


    def __str__(self) -> str:
        return f"{self.description} - {self.status} - {self.deadline}"