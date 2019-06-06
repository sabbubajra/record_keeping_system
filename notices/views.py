from django.shortcuts import render
from notices.models import Notice
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from student_info import helpers
# Create your views here.
def notice(request):
    posts = Notice.objects.order_by("id").all()
    posts = helpers.pg_records(request, posts,1)
    return render(request, 'notices/notice.html', {'posts': posts})
# def notice(request):
#     notice=Notice.objects.all()
#     return render(request,"notices/notice.html",{'notice':notice})