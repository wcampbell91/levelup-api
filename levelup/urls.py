from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user
from rest_framework import routers
from levelupapi.views import GameTypesViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypesViewSet, 'gametype')

urlpatterns = [
    path('', include(router.urls)),
    # Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
    # Requests to http://localhost:8000/login will be routed to the login_user
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
