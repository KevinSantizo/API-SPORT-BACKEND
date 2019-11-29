from django.db import models
from user.models import  Profile, Town, Department

# Create your models here.


class Company(models.Model):
    town = models.ForeignKey(Town, related_name='companies', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='admin/companies', null=True)

    def __str__(self):
        return self.name + ', ' + self.address 


class Field(models.Model):
    company = models.ForeignKey('Company', related_name='fields', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    FIELD_STATUS = (
        ('1', 'Ocupada'),
        ('2', 'Mantenimiento')
    )
    status = models.CharField(
        max_length=1,
        choices=FIELD_STATUS,
        blank=True,
        default='1',
    )
    TYPE_FIELD = (
        ('1', '5 Players'),
        ('2', '7 Players'),
        ('3', '11 Players'),
    )

    type = models.CharField(
        max_length=1,
        choices=TYPE_FIELD,
        blank=True,
        default='1',
    )
    price = models.FloatField(null=True)

    def __str__(self):
        return ' Type Field: ' + self.type + ', Cancha: ' + self.name + ', Price: ' + str(self.price) + ', Company:' + self.company.name + ' - ' + self.company.town.name + ' - ' + self.company.town.department.name        



class Reservation(models.Model):
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE, null=True)
    customer_reserve = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reservations')
    field_reserve = models.ForeignKey(Field, on_delete=models.CASCADE)
    implement = models.ForeignKey('Implement', on_delete=models.CASCADE, null=True)
    schedule_date = models.DateField(null=True)
    total = models.FloatField(null=True)

    def __str__(self):
        return  'Customer: ' + self.customer_reserve.first_name + ' --- Type Field: --- ' + self.field_reserve.type + ' --- Date Reserved: --- ' \
               + str(self.schedule_date) + ' --- Price: --- ' + str(self.field_reserve.price) + self.implement.name



class Schedule(models.Model):
    field = models.ForeignKey(Field, related_name='schedules', on_delete=models.CASCADE, null=True)
    start_time = models.TimeField(null=True)
    date = models.DateField(null=True)
    SCHEDULE_STATUS = (
        ('1', 'Reserved'),
        ('2', 'Available'),
    )
    status = models.CharField(
        max_length=1,
        choices=SCHEDULE_STATUS,
        blank=True,
        default='1',
    )

    def __str__(self):
        return 'Cancha ' + ' ' + self.field.name + ' de ' + self.field.company.name + ' , '  + self.field.company.town.name + ' - ' + self.field.company.town.department.name + ' Horario: ' + str(self.start_time)   


class Image(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='company')
    image = models.ImageField()

    def __str__(self):
        return self.company.name

    
class Implement(models.Model):
    name = models.CharField(max_length=10)
    price = models.FloatField(max_length=15)
    add = models.BooleanField()
    quantity = models.PositiveIntegerField(null=True)
    image = models.ImageField(upload_to='pictures', null=True)

    def __str__(self):
        return self.name + ' - ' + str(self.price) + ' - ' + str(self.add)
    
