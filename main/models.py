from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    title = models.CharField('Название', max_length=100)
    author = models.CharField('Автор', max_length=100)
    description = models.TextField('Описание')
    year = models.IntegerField('Год выпуска')
    is_available = models.BooleanField('Доступность книги', default=True)
    borrowed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name="borrowed_books")

    def __str__(self):
        return self.title

    def return_book(self):
        self.is_available = True
        self.borrowed_by = None
        self.save()

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
