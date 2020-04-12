# Generated by Django 3.0.5 on 2020-04-11 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='media_artikel',
            field=models.FileField(blank=True, default='images/saveus.png', null=True, upload_to='images/artikel/'),
        ),
        migrations.AlterField(
            model_name='users',
            name='profile_pic',
            field=models.FileField(blank=True, default='images/circleblue.png', null=True, upload_to='images/profil/'),
        ),
    ]
