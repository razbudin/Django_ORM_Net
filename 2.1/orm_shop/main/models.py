from django.db import models


class Client(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    phone_number = models.CharField(max_length=12, verbose_name="Телефон")

    def __str__(self):
        return self.last_name


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('CVT', 'Вариатор'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет'),
    ('liftback', 'Лифтбек')
)

DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    model = models.CharField(max_length=200, verbose_name='Модель')
    year = models.CharField(max_length=4, verbose_name='Год выпуска')
    color = models.CharField(max_length=100, verbose_name='Цвет')
    mileage = models.PositiveIntegerField(verbose_name='Пробег')
    volume = models.FloatField(verbose_name='Объем двигателя л')
    body_type = models.CharField(max_length=20,
                                 choices=BODY_TYPE_CHOICES,
                                 verbose_name='Кузов')
    drive_unit = models.CharField(max_length=20,
                                  choices=DRIVE_UNIT_CHOICES,
                                  verbose_name='Привод')
    gearbox = models.CharField(max_length=20,
                               choices=GEARBOX_CHOICES,
                               verbose_name='Каробка передач')
    fuel_type = models.CharField(max_length=20,
                                 choices=FUEL_TYPE_CHOICES,
                                 verbose_name='Питание двигателя')
    price = models.PositiveIntegerField(verbose_name='Цена')
    image = models.ImageField()

    class Meta:
        ordering = ['model']

    def __str__(self):
        return self.model


class Sale(models.Model):
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               verbose_name='Покупатель')
    car = models.ForeignKey(Car,
                            on_delete=models.CASCADE,
                            verbose_name='Автомобиль')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата сделки')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.client} {self.car} {self.created_at}'
