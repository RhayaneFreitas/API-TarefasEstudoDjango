# Generated by Django 5.0.6 on 2024-06-09 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_user_is_active_user_is_staff_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskprofile',
            name='created_in',
            field=models.DateField(auto_now_add=True, verbose_name='Created In'),
        ),
        migrations.AlterField(
            model_name='taskprofile',
            name='updated',
            field=models.DateField(auto_now=True, verbose_name='Updated'),
        ),
    ]
