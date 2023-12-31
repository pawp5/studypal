# Generated by Django 4.2.3 on 2023-08-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studypals', '0002_rename_searchtext_usertext'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChatBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='usertext',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
