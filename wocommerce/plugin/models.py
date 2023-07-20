from django.db import models


class Type_API(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название типа API')
    API_url = models.URLField(verbose_name='API url')

class API(models.Model):
    API_key = models.CharField(max_length=256, verbose_name='API ключ')
    login = models.CharField(max_length=256, verbose_name='Логин')
    password = models.CharField(max_length=64, verbose_name='Пароль')
    type = models.ForeignKey('Type_API', on_delete=models.CASCADE,related_name='apy_type', verbose_name='Тип API')

    def __str__(self):
        return self.api_type.name

class Order(models.Model):
    api = models.ForeignKey('API', on_delete=models.CASCADE,related_name='API' ,verbose_name='API')
    link = models.URLField(verbose_name='Ссылка')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    order_id = models.IntegerField(null=True, verbose_name='ID услуги в сервисе')
    servis_id = models.IntegerField(verbose_name='ID сервиса')
    quantity = models.IntegerField(default=0,verbose_name='Колличество услуг')
    status = models.CharField(max_length=64,default='запускается', verbose_name='Статус Заказа')
    error = models.CharField(max_length=256,null=True, verbose_name='Ошибка')



