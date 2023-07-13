from django.forms import ModelForm, TextInput, EmailInput,NumberInput, PasswordInput, Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import *

CATEGORIES = [
    (1,'Punctuality'),
    (2, 'Communication'),
    (3,'Teamwork'),
    (4, 'Initiative'),
    (5, 'Professionalism'),
              ]

class NewEmployee(forms.ModelForm):
   class Meta:
        model = Employee
        fields = ['empid','name','position']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','style':'width:440px;',}),
             'position': forms.TextInput(attrs={'class':'form-control','style':'width:440px;',}),
        }


class UpdateResp(forms.ModelForm):
    class Meta: 
        model = Responsibilities
        fields = ['cid','criteria']
        widgets = {
            'cid': forms.Select(choices=CATEGORIES),
            'criteria': forms.TextInput(),
        }

class EditCriteria(forms.ModelForm):
    class Meta: 
        model = Responsibilities
        fields = ['criteria']
       
        


CRITERIA_CHOICES = (Responsibilities.objects.all().values_list('rid', 'criteria'))

'''class PointsForm(forms.Form):
    criteria = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices= CRITERIA_CHOICES
    )

    # criteria1 = forms.CharField(label='', max_length=20, required=True, widget=forms.CheckboxSelectMultiple, choices = )
'''

'''class PointsForm(forms.ModelForm):
    class Meta:
        model = has
        fields = ['score']
        widgets= {
            'score' : forms.Select(attrs={'class': 'form-control'}),
         }
'''



class SurveyForm(forms.Form):
    criteria_scores = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Criteria Scores')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        responsibilities = Responsibilities.objects.all()
        choices = [(r.rid, r.criteria) for r in responsibilities]
        self.fields['criteria_scores'].choices = choices


class DeleteEmployee(forms.Form):
    empid = forms.CharField(max_length= 5, label= 'Employee ID')

class NewResponsibilty(forms.ModelForm):
    class Meta: 
        model = Category
        fields = ['title']

class LogInForm(forms.ModelForm):
    class Meta: 
        model = loginModel
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 450px;', 'class': 'form-control'}),
            'password':  forms.PasswordInput(attrs= {'placeholder':'Password','style':'width:450px;', 'class': 'form-control'})
        }
        labels = {
            'email': (''),
            'password': (''),
        }

