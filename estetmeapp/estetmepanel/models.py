from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from account.models import Profile


class Panel(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField('Тема задачи', max_length=500)
    descriptions = models.TextField('Опишите вопрос')
    file = models.FileField('Вложение файла', upload_to='./src/file/')
    date = models.DateTimeField('Дата публикации')
    created = models.DateField(verbose_name="Срок задачи")
    is_complete = models.BooleanField('Завершено', default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title


class Comment(models.Model):
    comments = RichTextUploadingField('Комментарии')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарие'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.comments