from detailabtstudent.models import Addstudent,Addteachers
from notices.models import Notice
from django import forms

class Addstudentform(forms.ModelForm):
    class Meta():
        model =Addstudent
        fields = '__all__'

class Addteacherform(forms.ModelForm):
    class Meta():
        model =Addteachers
        fields = '__all__'

class Addnoticeform(forms.ModelForm):
    class Meta():
        model=Notice
        fields='__all__'