
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.Home, name="Home"),
    path('',views.signin, name="signin"),
    # path('signin/', views.signin, name="signin"),
    path('logout/',views.logoutApi,name='logout'),
    path('signup/', views.signup, name='signup'),
    path('api/signupApi/', views.signupApi, name="signupApi"),
    path('api/loginView/', views.login_view,name="loginView"),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)