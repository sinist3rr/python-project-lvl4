# Generated by Django 3.2.6 on 2021-08-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
    ]
