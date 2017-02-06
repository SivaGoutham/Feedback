from django import forms
from django.forms import formset_factory
from .models import *

class LoginForm(forms.Form):
    id_no = forms.CharField(initial="14331A0500", max_length=10)
    id_no.clean('14331A05D9')
    crypt_password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.Form):
    id_no = forms.CharField(initial="Eg: 14331A0563", max_length=10)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

class FieldCountForm(forms.Form):
    add_empty_records = forms.IntegerField()

class DeleteForm(forms.Form):
    academic_year_code = forms.IntegerField()

class AcademicYearForm(forms.ModelForm):
    class Meta:
        model = AcademicYear
        fields = ['academic_year_code', 'academic_year']

class testform(forms.Form):
    f = forms.SelectMultiple(choices=('hey', 'hi', 'none'))