
from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("getbook/",views.getBook,name='getbook'),
    path('create/',views.createbook,name='createbook'),
    path("getbook/<int:id>/",views.deletebook,name='delete'),
    path('updatebook/<int:id>/',views.updatebook,name='updatebook'),
    path("logout/",views.logout,name='logout'),

]
