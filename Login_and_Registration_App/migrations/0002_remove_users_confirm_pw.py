# Generated by Django 2.2.4 on 2022-06-22 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login_and_Registration_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='confirm_pw',
        ),
    ]
