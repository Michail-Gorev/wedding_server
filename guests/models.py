from django.db import models


class Guest(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    alcohol = models.CharField(max_length=50, verbose_name="Алкоголь")
    custom_alcohol = models.CharField(max_length=100, blank=True, verbose_name="Свой вариант алкоголя")
    hot = models.CharField(max_length=50, verbose_name="Горячее")
    music = models.TextField(verbose_name="Музыка")
    car = models.BooleanField(default=False, verbose_name="На машине")
    comment = models.TextField(blank=True, verbose_name="Комментарий")

    def __str__(self):
        return self.name
