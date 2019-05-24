# Generated by Django 2.1.4 on 2019-05-24 19:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20190523_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childpost',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='childpost',
            name='parentPost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Post'),
        ),
    ]
