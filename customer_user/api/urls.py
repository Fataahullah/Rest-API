from django.contrib import admin
from django.urls import path,include
from api.views import UserViewSet,CustomerViewSet
from rest_framework import routers


router=routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'customers',CustomerViewSet)

urlpatterns = [
    path('',include(router.urls))
]
