# Generated by Django 2.2.5 on 2019-11-16 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/'),
        ),
    ]