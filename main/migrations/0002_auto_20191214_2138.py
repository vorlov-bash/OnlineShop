# Generated by Django 3.0 on 2019-12-14 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='about',
            field=models.TextField(verbose_name='Про телефон'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='cpu',
            field=models.CharField(max_length=30, verbose_name='Процесор'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='diagonal',
            field=models.PositiveSmallIntegerField(verbose_name='Діагональ'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='front_cam',
            field=models.PositiveSmallIntegerField(default=None, verbose_name='Фронтальна камера'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='mah',
            field=models.PositiveIntegerField(verbose_name='Ємність'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='main_cam',
            field=models.PositiveSmallIntegerField(verbose_name='Основна камера'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='matrix',
            field=models.CharField(max_length=10, verbose_name='Тип матриці'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='ram',
            field=models.PositiveIntegerField(verbose_name="Оперативна пам'ять"),
        ),
        migrations.AlterField(
            model_name='phone',
            name='resolution',
            field=models.CharField(max_length=15, verbose_name='Роздільна здатність'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='rom',
            field=models.PositiveIntegerField(verbose_name="Вбудована пам'ять"),
        ),
    ]
