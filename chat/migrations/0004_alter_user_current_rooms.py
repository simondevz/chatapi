# Generated by Django 4.2.2 on 2023-06-26 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_user_current_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='current_rooms',
            field=models.CharField(default='[]', max_length=1000),
        ),
    ]
