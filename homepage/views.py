from django.shortcuts import render
from notices.models import Notice

# Create your views here.
# def index(request):
#     noticetitle=Notice.objects.all()
#     context={
#         'noticetitle':noticetitle
#     }
#     return render(request,"homepage/fullindex.html",context)
#
# def noticedetail(request,noticeId):
#     noticedetail=Notice.objects.get(pk=noticeId)
#     context={'noticedetail':noticedetail}
#     return render(request,'notices/noticedetail.html',context)
def index(request):
    return render(request,"homepage/fullindex.html")