from django.http import HttpResponse
#from .models import *
from .forms import *
from django.forms import modelformset_factory
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.backends.db import SessionStore
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

def is_member(user):
    return user.groups.filter(name="Dept Admin").exists();

def login_view(request):
    if request.POST:
        if 'crypt_password' in request.POST:
            form = LoginForm(request)
            username = request.POST['id_no']
            password = request.POST['crypt_password']
            user = authenticate(username=username, password=password)
            if not user is None:
                login(request, user)
                return HttpResponseRedirect('/feedback/admin')
            else:
                return HttpResponse("Invalid Authentication")
        else:
            form2 = RegistrationForm(request)
            username = request.POST['id_no']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 != password2:
                return HttpResponse("Passwords Mismatch")
            if len(username) != 10:
                return HttpResponse("Invalid Username")
            User.objects.create_user(username.upper(),'example@gmail.com',password1).save()
            return HttpResponse("<h1>Successfully Registered</h1>")
    else:
        form = LoginForm()
        form2 = RegistrationForm()
    return render_to_response("login.htm", {'form': form,'form2':  form2 })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('login')


@login_required
def index(request):
    return HttpResponse("hello " + request.user.username)


@login_required
def admin(request):
    return render_to_response("admin.htm", {'username': request.user.username})


@login_required
@user_passes_test(is_member)
def academic_year(request):
    error = ''
    entries = 1
    myformset = modelformset_factory(AcademicYear, AcademicYearForm, extra=entries)
    formset=myformset(queryset=AcademicYear.objects.none())
    countform = FieldCountForm()
    deleteform = DeleteForm()
    data = {

    }
    if request.method == 'POST':
        print(request.POST)
        if 'add_empty_records' in request.POST: #add rows
            entries = int(request.POST['add_empty_records'])

            myformset = modelformset_factory(AcademicYear, AcademicYearForm, extra=entries)
            formset = myformset(queryset=AcademicYear.objects.none())
        elif 'form-0-academic_year_code' in request.POST: #add records
            formset = myformset(request.POST, queryset=AcademicYear.objects.none())
            if formset.is_valid():
                formset.save()
                formset = myformset(queryset=AcademicYear.objects.none())
            else:
                error = "Already exists or Invalid"
        else: #delete selected records
            indices = ''.join(request.POST.keys()).replace("form-", '').replace("-check", ' ').split()
            indices = map(int, indices)
            indices.sort(reverse=True)
            objects = AcademicYear.objects.all()
            try:
                for i in indices:
                    objects[i].delete()
            except:
                error = "Year code does not exist or error performing deletion"

    else:
        formset = myformset(queryset=AcademicYear.objects.none())
        countform = FieldCountForm()
        deleteform = DeleteForm()

    return render_to_response('academic_year.htm', {'formset': formset, 'countform': countform, 'deleteform': deleteform,
                                                    'database': myformset(), 'username': request.user.username,
                                                    'error': error})

def change_password(request):
    error = ''
    password_form = ChangePasswordForm()
    if request.method == 'POST':
        if not authenticate(username=request.user.username, password=request.POST['password']) is None:
            try:
                user = User.objects.get(username=request.user.username)
                if request.POST['password1'] == request.POST['password2']:
                    user.set_password(request.POST['password1'])
                    user.save()
                    logout(request)
                    return HttpResponseRedirect("login")
                else:
                    error="Passwords mismatch!"
            except:
                error = "Error changing password"
        else:
            error = "Wrong password!"
    else:
        password_form = ChangePasswordForm()

    return render_to_response('change_password.html', {'password_form':password_form, 'error': error})


def display(request):
    form = testform()
    return render_to_response('display.html', {'display': form})
