from django.contrib import admin
from sport.models import Field, Company, Reservation, Schedule, Image, Implement


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'status', 'type', 'price')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('town', 'name', 'address', 'phone', 'email', 'image')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('schedule', 'customer_reserve', 'field_reserve', 'implement', 'schedule_date', 'total')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('field', 'start_time', 'status')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('company', 'image')


@admin.register(Implement)
class ImplementAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'add')


