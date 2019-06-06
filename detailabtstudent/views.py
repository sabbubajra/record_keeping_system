from django.shortcuts import render,redirect
from .forms import Addnoticeform,Addstudentform,Addteacherform
from detailabtstudent.models import Addstudent,Addteachers
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.contrib import messages

from notices.views import notice


# Create your views here.

def dashboard(request):
    return render(request,'detailabtstudent/dashboard.html')

def addstudent(request):
    if request.method =="GET":
        return render(request, 'detailabtstudent/add_student.html')
    elif request.method=="POST":
        #form=Addstudentform(request.POST,request.FILES)
        try:
            name=request.POST['name']
            email=request.POST['email']
            address=request.POST['address']
            mobile=request.POST['phone']
            gender=request.POST['gender']
            dateofbirth=request.POST['dob']
            admissiondate=request.POST['admission']
            semester=request.POST['semester']
            image=request.FILES['image']
            student=Addstudent(name=name, email=email,address=address,gender=gender,mobileno=mobile,date_of_birth=dateofbirth,
                               admission_date=admissiondate,semester=semester,image=image)
            student.save()
            print("name = " + name)
            return render(request, 'detailabtstudent/add_student.html',{'success':True})
        except Exception as e:
            print("error in request")
            return render(request, 'detailabtstudent/add_student.html',{'success': False})

# def viewstudent(request):
#     listofstudent=Addstudent.objects.all()
#     context={
#         'student_list':listofstudent
#     }
#     return render(request,'detailabtstudent/view_student.html',context)

class StudentList(ListView):
    queryset =Addstudent.objects.all()

    # model = ModelPost
    # paginate_by = 2
    template_name = 'detailabtstudent/view_student.html'


class StudentUpdate(UpdateView):
    model = Addstudent
    template_name='detailabtstudent/update.html'
    fields ="__all__"
        #['id','semester', 'admission_date']

    def get_object(self, queryset=None):
        id = self.kwargs['pk']
        return self.model.objects.get(id=id)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('detailabtstudent:studentlist'))

class StudentDelete(DeleteView):
    template_name = 'detailabtstudent/delete.html'
    model = Addstudent
    success_url = reverse_lazy('detailabtstudent:studentlist')
        # Notice get_success_url is defined here and not in the model, because the model will be deleted
    # def get_success_url(self):
    #     return HttpResponseRedirect('studentlist')
    def get_object(self, queryset=None):
        id = self.kwargs['pk']
        return self.model.objects.get(id=id)

def studentdetail(request,studentid):
    detail=Addstudent.objects.get(pk=studentid)
    context={'detail':detail}
    return render(request,'detailabtstudent/studentdetail.html',context)

def addteachers(request):
    if request.method == "GET":
        return render(request, 'detailabtstudent/addteachers.html')
    elif request.method == "POST":
        try:
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['phone']
            image = request.FILES['file']
            teachers = Addteachers(name=name, email=email, contactno=mobile, image=image)
            teachers.save()
            return render(request, 'detailabtstudent/addteachers.html', {'success': True})
        except Exception as e:
            print("error in request")
            return render(request, 'detailabtstudent/addteachers.html', {'success': False})

def viewteachers(request):
    listofteachers=Addteachers.objects.all()
    context={
        'teachers_list':listofteachers
    }
    return render(request,'detailabtstudent/view_teachers.html',context)

def teacherupdate(request,updateid):
    update=Addteachers.objects.get(pk=updateid)
    form =Addteacherform(request.POST or None,request.FILES or None,instance=update)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('detailabtstudent:viewteachers'))

        #updateform=obj.save()
        #context = {'updateform':updateform,'success':'The form was updated successfully'}
    #     return HttpResponseRedirect(reverse('detailabtstudent:viewteachers'))
    # else:
    #     context = {'form': form,
    #                        'error': 'The form was not updated successfully'}
    return render(request, 'detailabtstudent/teacherupdate.html', context)


def teacherdelete(request,deleteid):
    deleteteacher = Addteachers.objects.get(pk=deleteid)
    if request.method == "POST":
        deleteteacher.delete()
        return HttpResponseRedirect(reverse('detailabtstudent:viewteachers'))
    context = {'deleteteacher':deleteteacher}
    return render(request, 'detailabtstudent/teacherdelete.html', context)





def addnotice(request):
    form=Addnoticeform()
    if request.method=='POST':
        form=Addnoticeform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'detailabtstudent/addnotice.html',{'form':form})
        else:
            print('Error form invalid')
    context={'form':form}
    return render(request, 'detailabtstudent/addnotice.html', context)