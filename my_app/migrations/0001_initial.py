# Generated by Django 2.0.1 on 2018-01-14 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information', models.CharField(blank=True, max_length=2055, verbose_name='Отзыв о товаре')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
                ('fb_users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'db_table': 'Feedback',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id_shop', models.AutoField(primary_key=True, serialize=False)),
                ('name_shop', models.CharField(max_length=20, verbose_name='Название магазина')),
                ('adr_shop', models.CharField(max_length=100, verbose_name='Адрес магазина')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
                'db_table': 'Shop',
            },
        ),
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id_tovar', models.AutoField(primary_key=True, serialize=False)),
                ('name_tovar', models.CharField(max_length=50, verbose_name='Название товара')),
                ('type_tovar', models.CharField(max_length=50, verbose_name='Тип товара')),
                ('photo_tovar', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото Товара')),
                ('opisanie_tovar', models.CharField(blank=True, max_length=2055, verbose_name='Описание товара')),
                ('id_tovar_fb', models.ManyToManyField(through='my_app.Feedback', to=settings.AUTH_USER_MODEL, verbose_name='ID отзыва')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'db_table': 'Tovar',
            },
        ),
        migrations.AddField(
            model_name='shop',
            name='assort_shop',
            field=models.ManyToManyField(to='my_app.Tovar', verbose_name='Ассортимент магазина'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='tovar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Tovar'),
        ),
    ]
