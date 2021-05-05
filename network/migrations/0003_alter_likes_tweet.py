# Generated by Django 3.2 on 2021-05-04 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_follows_likes_tweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likedTweet', to='network.tweet'),
        ),
    ]