from django.shortcuts import render,redirect,HttpResponse
from .models import emp
from .forms import UpdateForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import csv
from django.contrib.auth.models import User
from django.db import connection
from openpyxl import Workbook,load_workbook
from django.shortcuts import get_list_or_404
@login_required
def home_page(request):
    if request.method == "GET":
        return render(request,"home.html")

@login_required
def active_emp(request):
    if request.method == "GET":
        obj = emp.objects.filter(is_active = True,).order_by("id")
        c = emp.objects.count()
        return render(request,"activeemp.html",{"obj":obj,"count" : c})
    
@login_required
def in_active_emp(request):
    if request.method == "GET":
        obj = emp.objects.filter(is_active = False).order_by("id")
        return render(request,"inactiveemp.html",{"obj":obj})

@login_required
def show_detail(request,id):
    if request.method == "GET":
        obj = emp.objects.get(id=id)
        return render(request,"view.html",{"emp":obj})
    
@login_required
def update_details(request,id):
    if request.method == "GET":
        instance = get_object_or_404(emp, id=id)
        form = UpdateForm(request.POST or None, instance=instance)
        return render(request,"update.html",{"form":form})
    elif request.method == "POST":
        obj = request.POST
        print(obj)
        a = emp.objects.get(id=id)
        a.name = obj.get("name")
        a.joining_date = obj.get("joining_date")
        a.email_id = obj.get("email_id")
        a.department = obj.get("department")
        a.salary = obj.get("salary")
        a.job_status = obj.get("job_status")
        a.is_active = obj.get("is_active")

        if a.is_active == "on":
            a.is_active= True
        else:
            a.is_active = False
        a.save()
        messages.success(request,"Details Updated Suessfully")

        return redirect("active_emp")

        
@login_required
def soft_delete(request,id):
    obj = emp.objects.get(id=id)
    obj.is_active = False
    obj.save()
    return redirect("in_active_emp")


@login_required
def hard_delete(request,id):
    obj = emp.objects.get(id=id)
    obj.delete()
    return redirect("active_emp")


@login_required
def view(request,id):
    obj = emp.objects.get(id=id)
    return render(request,"view.html",{'emp':obj})


@login_required
def restore(request,id):
    obj = emp.objects.get(id = id)
    obj.is_active = True
    obj.save()
    return redirect("in_active_emp")

@login_required
def add_emp(request):
    if request.method == "GET":
        return render(request,"add.html",{"form":UpdateForm()})
    elif request.method == "POST":
        data = request.POST
        form = UpdateForm(data)
        if form.is_valid():
            form.save()
            user = User.objects.get(username= data.get("Create"))
            obj = emp.objects.get(email_id = data.get("email_id"))
            obj.created_by = user
            obj.save()
        return redirect("active_emp")
    
    # Bharat <QueryDict: {'csrfmiddlewaretoken': ['Jll9SBTg8wW620FI6Pkcbn7m0MRXYeSgzYd0KKyM7C574euGbYxrR1X6oLvx7mlW'], 'name': ['Bharat Ramesh Mate'], 'joining_date': ['2023-07-10'], 'email_id': ['bharatmate0@gmail.com'], 'department': ['Sales'], 'salary': ['89585'], 'job_status': ['Permanentt'], 'is_active': ['on'], 'created_by': ['1'], 'Create': ['Bharat']}>
@login_required
def create_csv(request):
    pass
    # response = HttpResponse(content_type = "text/csv")   # this way creating file objects
    # response['Content-Disposition'] = 'attachment; filename = "text.csv"'
    # obj = csv.writer(response)
    # headers = ["name","joining_date", "email_id", "department", "salary", "job_status", "is_active" ]
    # obj.writerow(headers)
    # comm = connection.cursor()
    # comm.execute("select * from emp_data where is_active = True")
    # data = comm.fetchall()
    # print(data)
    # lst =[]
    # for x in data:
    #     na = x[1]
    #     j_d = x[2]
    #     e_i = x[3]
    #     d = x[4]
    #     s = x[5]
    #     J_s = x[6]
    #     st = x[7]
    #     l = [na, j_d, e_i, d, s, J_s, st]
    #     lst.append(l)
    # obj.writerows(lst)
    # return response
    respone = HttpResponse(content_type="text/csv")
    respone['Content-Disposition'] = 'attachment; filename = "data.csv"'
    # response = HttpResponse(content_type = "text/csv")   # this way creating file objects
    # response['Content-Disposition'] = 'attachment; filename = "text.csv"'
    obj = csv.writer(respone)
    obj.writerow(['name','joining_date', 'email_id', 'department', 'salary', 'job_status', 'is_active'])
    comm = connection.cursor()
    comm.execute('select * from emp_data where is_active= True')
    data = comm.fetchall()
    new = list(map(lambda x : x[1:8],data))
    
    obj.writerows(new)
    return respone


@login_required
def upload_csv(request):
    file = request.FILES['csv_file']
    file_obj = file.read().decode('utf-8').splitlines()
    obj = csv.reader(file_obj)
    lst = []
    for x in obj:
        print(x)
        if x[0] == "name":
            continue
        
        na = x[0]
        try:
            if na == "":
                raise ValueError
        except ValueError:
            messages.error(request,f"Name not be null") 
            return redirect("add_emp")
        try:
            get_obj = emp.objects.get(name = na)
            raise ValueError
        except ValueError:
            messages.error(request,f"{na} name already exits")
            return redirect("add_emp")
        except emp.DoesNotExist:
            name = na
        j_d = x[1]
        try:
            if j_d == "":
                raise ValueError
        except ValueError:
            messages.error(request,f"Joinning date  not be null") 
            return redirect("add_emp")
        e_i = x[2]
        try:
            if e_i == "":
                raise ValueError
        except ValueError:
            messages.error(request,f"Email Id  not be null") 
            return redirect("add_emp")
        
        try:
            get = emp.objects.get(email_id = e_i)
            raise emp.MultipleObjectsReturned
        except emp.MultipleObjectsReturned:
            messages.error(request,f"{e_i} email already exits")
            return redirect("add_emp")
        except emp.DoesNotExist:
            e_i_e = e_i
        dep = x[3]
        try:
            if dep == "":
                raise ValueError
        except ValueError:
            messages.error(request,f"Department  not be null") 
            return redirect("add_emp")
        sa = x[4]
        try:
            if sa == "":
                raise ValueError
        except ValueError:
            messages.error(request,f"Salary  not be null") 
            return redirect("add_emp")
        j_s = x[5]
        try:
            if j_s == "":
                raise ValueError
        except ValueError:
            messages.error(request,f"Job Status  not be null") 
            return redirect("add_emp")
        is_active = x[6]
        if is_active == "TRUE":
            is_active = True
        else:
            is_active = False
        emp_obj = emp(name=name, joining_date=j_d, email_id = e_i_e, department = dep, salary = sa, job_status = j_s, is_active = is_active)
        lst.append(emp_obj)
    emp.objects.bulk_create(lst)
    messages.success(request,"Data Uploaded Sussecfully ")
    return redirect("add_emp")
@login_required
def create_inactive_csv(request):
    response = HttpResponse(content_type = "text/csv")   # this way creating file objects
    response['Content-Disposition'] = 'attachment; filename = "text.csv"'
    obj = csv.writer(response)
    headers = ["name","joining_date", "email_id", "department", "salary", "job_status", "is_active" ]
    obj.writerow(headers)
    # data_1 = emp.objects.values_list()  #----Given list in tuple(disadvatngee is fetch all deta)
    # obj.writerows(data_1)
    comm = connection.cursor()
    comm.execute("select * from emp_data where is_active = False")
    data = comm.fetchall()
    print(data)   #  list in tuple
    lst =[]
    for x in data:
        na = x[1]
        j_d = x[2]
        e_i = x[3]
        d = x[4]
        s = x[5]
        J_s = x[6]
        st = x[7]
        l = [na, j_d, e_i, d, s, J_s, st]
        lst.append(l)
    obj.writerows(lst)
    return response


@login_required
def sample_create_csv(request):
    responsed = HttpResponse(content_type = "sample/csv")   # this way creating file objects
    responsed['Content-Disposition'] = 'attachment; filename = "sample.csv"'
    obj = csv.writer(responsed)
    headers = ["name","joining_date", "email_id", "department", "salary", "job_status", "is_active" ]
    obj.writerow(headers)
    return responsed



