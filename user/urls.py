from rest_framework import routers
from user.viewsets import  DepartmentViewSet, TownViewSet,  DoTownViewSet, UserViewSet
from user import views
from django.urls import path


router = routers.SimpleRouter()
router.register('departments', DepartmentViewSet)
router.register('towns', TownViewSet)
router.register('do-town', DoTownViewSet)
router.register('users', UserViewSet)

urlpatterns = router.urls