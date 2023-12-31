# Generated by Django 4.2.3 on 2023-07-20 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('API_key', models.CharField(max_length=256, verbose_name='API ключ')),
                ('login', models.CharField(max_length=256, verbose_name='Логин')),
                ('password', models.CharField(max_length=64, verbose_name='Пароль')),
            ],
        ),
        migrations.CreateModel(
            name='Type_API',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название типа API')),
                ('API_url', models.URLField(verbose_name='API url')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(verbose_name='Ссылка')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')),
                ('order_id', models.IntegerField(null=True, verbose_name='ID услуги в сервисе')),
                ('servis_id', models.IntegerField(verbose_name='ID сервиса')),
                ('quantity', models.IntegerField(default=0, verbose_name='Колличество услуг')),
                ('status', models.CharField(default='запускается', max_length=64, verbose_name='Статус Заказа')),
                ('error', models.CharField(max_length=256, null=True, verbose_name='Ошибка')),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='API', to='plugin.api', verbose_name='API')),
            ],
        ),
        migrations.AddField(
            model_name='api',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apy_type', to='plugin.type_api', verbose_name='Тип API'),
        ),
    ]
