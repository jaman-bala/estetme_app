from django.db import models


class Panel(models.Model):
    title = models.CharField('Тема задачи', max_length=500)
    descriptions = models.TextField('Опишите вопрос')
    file = models.FileField('Вложить файл', upload_to='file', blank=True)
    date = models.DateTimeField('Дата публикации')
    created = models.DateTimeField(verbose_name="Срок задачи", auto_now_add=True)
    is_complete = models.BooleanField('Завершено', default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title
