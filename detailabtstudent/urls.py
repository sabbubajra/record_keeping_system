from .import views
from django.urls import path

app_name='detailabtstudent'
urlpatterns=[
    path('addstudent',views.addstudent,name='addstudent'),
    # path('studentlist',views.viewstudent,name='studentlist'),
    path('studentlist',views.StudentList.as_view(),name='studentlist'),
    path('studentupdate/(?P<pk>\d+)/$',views.StudentUpdate.as_view(),name='studentupdate'),
    path('studentdelete/(?P<pk>\d+)/$',views.StudentDelete.as_view(),name='studentdelete'),
    path('studentdetail/<studentid>',views.studentdetail,name='studentdetail'),
    path('addteachers',views.addteachers,name='addteachers'),
    path('viewteachers',views.viewteachers,name='viewteachers'),
    path('teacherupdate/<updateid>',views.teacherupdate,name='teacherupdate'),
    path('teacherdelete/<deleteid>',views.teacherdelete,name='teacherdelete'),
    path('',views.dashboard,name='dashboard'),
    path('addnotice',views.addnotice,name='addnotice')
]