# Generated by Django 2.1.5 on 2019-02-01 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(default=0, verbose_name='возраст'),
        ),
    ]
