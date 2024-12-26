from django.db import models


class Books(models.Model):
    title = models.CharField('Название', max_length=100)
    author = models.CharField('Автор', max_length=100)
    description = models.TextField('Описание')
    year = models.IntegerField('Год выпуска')
    is_available = models.BooleanField('Доступность книги')
    user = models.EmailField('Почта пользователя', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
