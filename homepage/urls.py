from django.urls import path,include
from .import views
app_name='homepage'
urlpatterns=[
    path('',views.index,name="index")
    #path('notice/<noticeId>',views.noticedetail,name="notice"),
]