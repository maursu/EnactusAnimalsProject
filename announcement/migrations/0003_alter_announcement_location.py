# Generated by Django 4.2 on 2023-04-11 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0002_rename_deascription_announcement_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='location',
            field=models.CharField(choices=[('Бишкек', 'Бишкек'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Иссык-куль', 'Иссык-куль'), ('Баткен', 'Баткен'), ('Талас', 'Талас'), ('Джалал-Абад', 'Джалал-Абад')], max_length=20),
        ),
    ]