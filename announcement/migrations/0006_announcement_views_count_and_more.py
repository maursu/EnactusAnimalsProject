# Generated by Django 4.2 on 2023-04-11 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0005_alter_announcement_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='views_count',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddIndex(
            model_name='announcementphoto',
            index=models.Index(fields=['announcement'], name='announcemen_announc_1e525d_idx'),
        ),
    ]