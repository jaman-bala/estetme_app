# Generated by Django 4.2.6 on 2023-10-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.DecimalField(decimal_places=10, default=2222, max_digits=18, verbose_name='Номер Тел:'),
            preserve_default=False,
        ),
    ]
