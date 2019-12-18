# Generated by Django 3.0 on 2019-12-18 18:42

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('items', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва Телефону')),
                ('about', models.TextField(verbose_name='Про телефон')),
                ('diagonal', models.FloatField(verbose_name='Діагональ')),
                ('resolution', models.CharField(max_length=15, verbose_name='Роздільна здатність')),
                ('ram', models.PositiveIntegerField(verbose_name="Оперативна пам'ять")),
                ('rom', models.PositiveIntegerField(verbose_name="Вбудована пам'ять")),
                ('mah', models.PositiveIntegerField(verbose_name='Ємність')),
                ('main_cam', models.PositiveSmallIntegerField(verbose_name='Основна камера')),
                ('front_cam', models.PositiveSmallIntegerField(default=None, verbose_name='Фронтальна камера')),
                ('matrix', models.CharField(max_length=20, verbose_name='Тип матриці')),
                ('cpu', models.CharField(max_length=30, verbose_name='Процесор')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Кількість')),
                ('price', models.PositiveIntegerField(verbose_name='Ціна')),
                ('image', models.ImageField(upload_to='static/img/')),
            ],
        ),
    ]