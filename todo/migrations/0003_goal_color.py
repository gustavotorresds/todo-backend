# Generated by Django 3.0.1 on 2019-12-22 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='color',
            field=models.CharField(default='#FFFFFF', max_length=8),
        ),
    ]