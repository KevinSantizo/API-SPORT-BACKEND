from rest_framework import viewsets
from user.models import Profile, Department, Town
from user.serializer import (
    DepartmentSerializer, 
    TownSerializer, 
    DoTownSerializer,
    ProfileSerializer
)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class TownViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    authentication_classes = ()
    queryset = Town.objects.all()
    serializer_class = TownSerializer


class DoTownViewSet(viewsets.ModelViewSet):
    queryset = Town.objects.all()
    serializer_class = DoTownSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    authentication_classes = ()
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
