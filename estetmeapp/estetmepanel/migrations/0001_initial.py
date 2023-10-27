# Generated by Django 4.2.6 on 2023-10-27 05:07

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Тема задачи')),
                ('descriptions', models.TextField(verbose_name='Опишите вопрос')),
                ('file', models.FileField(upload_to='./src/file/', verbose_name='Вложение файла')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
                ('created', models.DateField(verbose_name='Срок задачи')),
                ('is_complete', models.BooleanField(default=False, verbose_name='Завершено')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Комментарии')),
                ('panel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estetmepanel.panel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
            options={
                'verbose_name': 'Комментарие',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
