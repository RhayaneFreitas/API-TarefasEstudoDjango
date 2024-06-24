# Generated by Django 5.0.6 on 2024-06-24 18:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_alter_taskresponsible_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskresponsible',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.taskprofile', verbose_name='Task'),
        ),
        migrations.AlterField(
            model_name='taskresponsible',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
