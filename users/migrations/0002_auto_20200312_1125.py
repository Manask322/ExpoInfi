# Generated by Django 3.0.4 on 2020-03-12 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='current_score',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='high_score',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
