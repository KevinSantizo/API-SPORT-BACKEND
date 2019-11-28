from rest_framework import serializers
from datetime import datetime, time, date
from sport.models import Field, Reservation, Company, Schedule, Implement
from user.models import Department, Town, Profile
from user.serializer import DepartmentSerializer, DoTownSerializer


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        depth = 5


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class DoReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        depth = 4
        

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
        depth = 3


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        depth = 2


class DepartmentChildSerializer(serializers.ModelSerializer):
    towns = DoTownSerializer(many=True)
    class Meta:
        model = Department
        fields = ('id', 'name', 'description', 'towns')


class TownChildSerializer(serializers.ModelSerializer):
    companies = CompanySerializer(many=True)
    class Meta:
        model = Town
        fields = ('id', 'name', 'companies') 


class DoScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
        depth = 4


class CountScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
        depth = 4
        

class FieldChildSerializer(serializers.ModelSerializer):
    schedules = serializers.SerializerMethodField('get_schedules')
    quantity = serializers.SerializerMethodField('count_schedules')

    def get_schedules(self, field):
        today = date.today()
        sch = Schedule.objects.filter(start_time__gte=datetime.now(), date=today, status__exact=2, field=field)
        serializer = DoScheduleSerializer(instance=sch, many=True)
        return serializer.data

    def count_schedules(self, field):
        today = date.today()
        sch = Schedule.objects.filter(start_time__gte=datetime.now(), date=today, field=field).count()
        return sch

    class Meta:
        model = Field
        fields = ( 'company', 'id', 'name', 'status', 'type', 'price', 'schedules', 'quantity')
        detph = 3


class CountSerializer(serializers.ModelSerializer):
    schedules = serializers.SerializerMethodField('get_count')

    def get_count(self, field):
        sch = Schedule.objects.filter(field=field).count()
        return sch

    class Meta:
        model = Field
        fields = ( 'company', 'id', 'name', 'status', 'type', 'price', 'schedules')
        

class CompanyFieldSerializer(serializers.ModelSerializer):
    fields = FieldChildSerializer(many=True)
    class Meta:
        model = Company
        fields = ('town', 'id', 'name', 'address', 'phone', 'email', 'image', 'fields')
        depth = 2


class ImplementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Implement
        fields = '__all__'


class CustomerReservationSerializer(serializers.ModelSerializer):
    reservations = serializers.SerializerMethodField('get_reservations')
    quantity = serializers.SerializerMethodField('count_reservations')

    def get_reservations(self, customer_reserve):
        rsv = Reservation.objects.filter(customer_reserve=customer_reserve)
        serializer = DoReservationSerializer(instance=rsv, many=True)
        return serializer.data

    def count_reservations(self, customer_reserve):
        sch = Reservation.objects.filter(customer_reserve=customer_reserve).count()
        return sch

    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'username', 'town', 'phone', 'email', 'password', 'reservations', 'quantity')
        depth = 2


class FieldScheduleSerializer(serializers.ModelSerializer):
    schedules = serializers.SerializerMethodField('get_schedules')
    quantity = serializers.SerializerMethodField('count_schedules')

    def get_schedules(self, field):
        today = date.today()
        sch = Schedule.objects.filter(start_time__gte=datetime.now(), status__exact=2, date=today, field=field)
        serializer = DoScheduleSerializer(instance=sch, many=True)
        return serializer.data

    def count_schedules(self, field):
        today = date.today()
        sch = Schedule.objects.filter(start_time__gte=datetime.now(), status__exact=2, date=today, field=field).count()
        return sch

    class Meta:
        model = Field
        fields = ( 'company', 'id', 'name', 'status', 'type', 'price', 'schedules', 'quantity')
        read_only_fields = ('company', 'id', 'name', 'status', 'type', 'price', 'schedules', 'quantity' )
        depth = 4


class MakeReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class UserReservationTodaySeralizer(serializers.ModelSerializer):
    reservations = serializers.SerializerMethodField('today_reservation')
    quantity= serializers.SerializerMethodField('get_reservations')

    def today_reservation(self, customer_reserve):
        today = date.today()
        res = Reservation.objects.filter(schedule_date=today, customer_reserve=customer_reserve)
        serializer = DoReservationSerializer(instance=res, many=True)
        return serializer.data

    def get_reservations(self, customer_reserve):
            today = date.today()
            q = Reservation.objects.filter(schedule_date=today, customer_reserve=customer_reserve).count()
            return q

    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'username', 'town', 'phone', 'email', 'password', 'reservations', 'quantity')



