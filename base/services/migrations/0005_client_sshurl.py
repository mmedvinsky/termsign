# Generated by Django 2.0.dev20170304171821 on 2017-04-25 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20170425_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='sshurl',
            field=models.CharField(default='', max_length=1024),
        ),
    ]