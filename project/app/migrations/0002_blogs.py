# Generated by Django 3.2 on 2021-06-25 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('authname', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
