# Generated by Django 2.2.4 on 2022-06-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=255)),
                ('Lname', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('confirm_pw', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
