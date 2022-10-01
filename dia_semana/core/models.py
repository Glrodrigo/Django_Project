from django.db import models

class Dia_semanaModel(models.Model):
    name        = models.CharField('Dia_semana', max_length = 50)
    day         = models.IntegerField('Data')
    month       = models.IntegerField('Mes')
    modified_in = models.DateTimeField(
        verbose_name = 'Modificado em',
        auto_now_add = False, auto_now = True
    )

    def __str__(self):
        return self.name + '=> ' + str(self.day)
