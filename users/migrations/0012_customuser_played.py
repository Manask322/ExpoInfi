# Generated by Django 3.0.4 on 2020-04-02 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200329_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='played',
            field=models.IntegerField(default=False, null=True),
        ),
    ]