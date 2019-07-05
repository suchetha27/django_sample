from django import forms

from .models import Student

class StudentEditModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'#student_name,department you can display any
        widgets={
            'student_name':forms.TextInput(attrs={'class':'form-control',
            'placeholder':'studentName'}),
            'department':forms.Select(attrs={'class':'custom-select'})
        }

class StudentCreateForm(forms.Form):
    student_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control',
    'maxlength':'50','placeholder':'Student Name'}))
    dept=(
        ('CSE','computer science'),
        ('MH','mech'),
        ('cv','civil')
    )
    department=forms.CharField(label='',widget=forms.Select(attrs={'class':'form-control'},choices=dept))



class StudentSearchForm(forms.Form):
    q=forms.CharField(label='yenbekadru maadu',widget=forms.TextInput(attrs={'class':'form-control',
    'max_length':'30','placeholder':'Search'}))
