# Generated by Django 2.1.4 on 2019-05-24 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20190118_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('', '--'), ('Looking for a debate', 'Looking for a debate'), ('For your consideration', 'For your consideration'), ('Seeking information', 'Seeking information'), ('Nmanagew Debate', 'New Debate')], max_length=1),
        ),
    ]
