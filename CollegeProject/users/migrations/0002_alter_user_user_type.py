# Generated by Django 4.1.4 on 2022-12-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('1', 'Admin'), ('2', 'Staff'), ('3', 'Student')], default='1', max_length=10),
        ),
    ]
