from django.db import models


class Order(models.Model):
    dt = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, verbose_name='Имя')
    number = models.CharField(max_length=255, verbose_name='Телефон')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Член мой'
        verbose_name_plural = 'Заказы'