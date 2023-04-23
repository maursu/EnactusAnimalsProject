# Generated by Django 4.2 on 2023-04-23 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='image',
            field=models.ImageField(default=None, upload_to='catalogImages'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalog',
            name='location',
            field=models.CharField(choices=[('Бишкек', 'Бишкек'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Иссык-куль', 'Иссык-куль'), ('Баткен', 'Баткен'), ('Талас', 'Талас'), ('Джалал-Абад', 'Джалал-Абад')], default='Бишкек', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalog',
            name='phone_number',
            field=models.CharField(default=99612341234, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalog',
            name='title',
            field=models.CharField(default='test', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='catalog',
            name='adress_type',
            field=models.CharField(choices=[('hostel', 'Хостел/Приют'), ('clinic', 'Ветклиника'), ('zooshop', 'Зоомагазин'), ('babysitter', 'Зооняни')], max_length=50),
        ),
    ]
