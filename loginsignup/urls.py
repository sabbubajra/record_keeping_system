from django.urls import path
from . import views

app_name="loginsignup"
urlpatterns=[
    path('',views.mylogin,name="login"),
    # path('signup',views.signup,name="signup"),
    path('logout',views.mylogout,name="logout"),
]