# Generated by Django 5.0.6 on 2024-06-13 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0005_remove_user_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(default='2000-01-01'),
        ),
    ]
