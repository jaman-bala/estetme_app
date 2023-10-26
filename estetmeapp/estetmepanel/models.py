from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Panel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Тема задачи', max_length=500)
    descriptions = models.TextField('Опишите вопрос')
    file = models.FileField('Вложение файла', upload_to='./src/file/')
    date = models.DateTimeField('Дата публикации')
    created = models.DateTimeField(verbose_name="Срок задачи", auto_now_add=True)
    is_complete = models.BooleanField('Завершено', default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title


class Comment(models.Model):
    comments = RichTextUploadingField('Комментарии')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарие'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.comments