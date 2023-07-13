from django.shortcuts import render, redirect
from django.http import HttpResponse
from polls.models import *
from .forms import *
from .models import *
from django.shortcuts import render
from django.db import connection
import hashlib
from itertools import chain

def index(request):
    return HttpResponse(" You're at the polls index. Add Login here")
# Create your views here.

def dash(request):
    roster = Employee.objects.all()
    print(roster)
    context = {'roster': roster}
    return render(request,'polls/dash.html',context)

'''
def addemp(request):
    form = NewEmployee()
    return render(request, 'addemployee.html', {
        'form': form,
    })
'''

def addemp(request):
    form = NewEmployee(request.POST)
    context ={'form':form}
    if request.method == 'POST':
        if form.is_valid():
           
            name = form.cleaned_data['name']
            position = form.cleaned_data['position']
            newemp = Employee( name = name, position= position)
            newemp.save()
            #form.save()
            
            for i in Responsibilities.objects.raw("SELECT rid FROM polls_responsibilities"):
                hasupdate = has(score = 0, empid = newemp, rid = i)
                print(i.rid)
                hasupdate.save()
            return redirect ('dash')

          #if GET load blank form 
        else: 
            form = NewEmployee()
    return render(request, 'polls/addemployee.html', context)

#def points(request):
#    form = NewPoints(request.POST)
#    context = {'form':form}
#    if request.method == 'POST':
#        if form.is_valid():
#            form.save()


def stats(request):
    context = {}
    return render(request, 'polls/stats.html', context)

def resp(request):
    #resp = Responsibilities.objects.all()
    resp1 = Responsibilities.objects.filter(cid=1)
    resp2 = Responsibilities.objects.filter(cid=2)
    resp3 = Responsibilities.objects.filter(cid=3)
    resp4 = Responsibilities.objects.filter(cid=4)
    resp5 = Responsibilities.objects.filter(cid=5)
    print(resp1)

    context = {'resp1':resp1, 'resp2':resp2, 'resp3':resp3,'resp4':resp4,'resp5':resp5 }
    return render(request, 'polls/resp.html', context)

def profile(request, pk):
    employee = Employee.objects.get(empid=pk)
    points = has.objects.filter(empid=pk, score=True)
    with connection.cursor() as cursor:
        cursor.execute('SELECT COUNT(cid) FROM polls_has NATURAL JOIN polls_responsibilities WHERE cid = 1 AND empid = %s AND score = True', [pk])
        result = cursor.fetchone()  # Fetch the single row result
        
        cursor.execute('SELECT COUNT(cid) FROM polls_has NATURAL JOIN polls_responsibilities WHERE cid = 2 AND empid = %s AND score = True', [pk])
        c = cursor.fetchone()

        cursor.execute('SELECT COUNT(cid) FROM polls_has NATURAL JOIN polls_responsibilities WHERE cid = 3 AND empid = %s AND score = True', [pk])
        t = cursor.fetchone()

        cursor.execute('SELECT COUNT(cid) FROM polls_has NATURAL JOIN polls_responsibilities WHERE cid = 4 AND empid = %s AND score = True', [pk])
        i = cursor.fetchone()

        cursor.execute('SELECT COUNT(cid) FROM polls_has NATURAL JOIN polls_responsibilities WHERE cid = 5 AND empid = %s AND score = True', [pk])
        p = cursor.fetchone()

    punctuality = result[0] if result else None
    comms = c[0] if c else None
    teamwork = t[0] if t else None
    initiative = i[0] if i else None
    professionalism = p[0] if p else None

    total = points.count()
    print (points)
    context = {'employee':employee, 'points':points, 'total':total, 'punctuality': punctuality, 'comms': comms, 'teamwork':teamwork, 'initiative':initiative, 'professionalism': professionalism}
    return render(request, 'polls/profile.html', context)

def pointsform (request, pk):
    emp = Employee.objects.get(empid=pk)

    form = SurveyForm()#instance=emp)
    context ={'form':form, 'emp':emp}
    if request.method =='POST':
        form = SurveyForm(request.POST)#, instance = emp )
        if form.is_valid():
            criteria_scores = form.cleaned_data['criteria_scores']
            for rid in criteria_scores:
                ridinst = Responsibilities.objects.get(rid=rid)
                newpoints = has(empid=emp,rid = ridinst, score =True )
                newpoints.save()
           
            
            return redirect('dash')
    
    return render(request, 'polls/pointsform.html',context)


def deleteEmp (request, pk):
    emp = Employee.objects.get(empid=pk)
    if request.method == 'POST':
        emp.delete()
        return redirect('dash')
    context = {'emp': emp}
    return render (request, 'polls/delete.html', context)


def newCriteria (request, pk):
    crit = Responsibilities.objects.get(rid=pk)
    form = EditCriteria(instance = crit)
    context = {'form':form}

    if request.method == 'POST':
        form = EditCriteria(request.POST, instance = crit)
        if form.is_valid():
            form.save()
            return redirect ('resp')
    
    return render(request, 'polls/updatecrit.html', context)

"""
def loginFunc(request):
    if request.method == 'POST':
        context = {}
        form = LogInForm(request.POST)
        if form.is_valid():
            pwrd = form.cleaned_data['password']
            email = form.cleaned_data['email']
            
            try:
                query = login.objects.filter(email = email)
            
                if (query.password == pwrd):
                    # instantiate new session to begin
                    csrftoken = query.email[:-2]
                    csrftoken += query.password[2:4]
                    
                    my_hash = hashlib.sha256(csrftoken.encode('utf-8')).hexdigest()
                    
                    session_data = my_hash
                    query.sessionID = session_data
                    query.save()
                    
                    return redirect('dash')
                else: 
                    error = "Incorrect password"
                   
            except login.DoesNotExist: 
                error = "Unauthorized Email"
                           
        else:
            error = "Invalid Form"
    else:
        form = LogInForm()
        error = None
        
    context = {'form': form, 'error': error}
    return render (request, 'polls/login.html', context)

"""

from django.contrib.auth import authenticate, login

"""def loginFunc(request):
    if request.method=='POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email = email, password = password)
            if user is not None:
                login(request, user)
                return redirect('dash')
            else:
                error = "Invalid email or password"
        else: 
            error = "Invalid form"
    else: 
        form = LogInForm()
        error = None
    
    context = {'form':form, 'error':error}
    return render(request, 'polls/login.html',context)
"""
from django.core.exceptions import ObjectDoesNotExist


def login_view(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = loginModel.objects.filter(email=email, password=password)
            if(user):
                return redirect('dash')
            else:
                return render(request, 'polls/login.html', {'form': form, 'error': 'Invalid login credentials.'})
           
    else:
        form = LogInForm()
    
    return render(request, 'polls/login.html', {'form': form})

def searchbar(request):

    if request.method == 'POST':
        searched = request.POST.get("searched")
        emp = Employee.objects.filter(name__icontains = searched)
        emp2 = Employee.objects.filter(position__icontains = searched)
        query = list(chain(emp,emp2))
        return render(request, 'polls/search.html', {'result': searched, 'query': query})
    else:
        return render(request, 'polls/search.html')
    


from django.db.models import Max

"""def leaderboard (request):
    
    employees = Employee.objects.all()
    total = []
    for i in range(employees.count()):
        points = has.objects.filter(empid=i, score=True).count()
        total.append(points)
        #total[i] = points.count()
        print(total[i])
        
    
    context = {'employees':employees, 'points':points, 'total':total}
    return render(request, 'polls/stats.html', context)"""