# Generated by Django 3.2.7 on 2021-10-31 11:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PJI110', '0017_auto_20211026_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='matriz',
            name='Dt_Matriz',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matriz',
            name='IsHolyday_Matriz',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matriz',
            name='NumMil_Matriz',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
