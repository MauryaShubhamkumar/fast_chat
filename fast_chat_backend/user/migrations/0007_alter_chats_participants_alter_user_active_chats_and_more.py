# Generated by Django 5.1.1 on 2024-09-16 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_chats_participants_alter_user_active_chats_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chats',
            name='participants',
            field=models.CharField(default='80045d942e', max_length=1099511627776),
        ),
        migrations.AlterField(
            model_name='user',
            name='active_chats',
            field=models.CharField(default='80045d942e', max_length=1099511627776),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact_list',
            field=models.CharField(default='80045d942e', max_length=1099511627776),
        ),
    ]
