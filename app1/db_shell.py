# from app1.models import emp
# from openpyxl import load_workbook
from django.contrib.auth.models import User
# exec(open(r"D:\python_program\python_code\Django_projects\Django Projects\sample\app1\db_shell.py").read())
# FILE_PATH = r"D:\python_program\excel_files\emp_data_sample_1.xlsx"

# class Opertions:
#     def get_data(self):
#         wb= load_workbook(filename=FILE_PATH)
#         sheet = wb.active
#         lst_obj = []
#         for x in range(2,sheet.max_row+1):
#             n = sheet.cell(row=x ,column = 1).value
#             jd = sheet.cell(row =x ,column= 2).value
#             ea = sheet.cell(row=x,column = 3).value
#             d = sheet.cell(row=x ,column = 4).value 
#             s = sheet.cell(row =x ,column = 5).value
#             js = sheet.cell(row = x ,column =6 ).value

#             obj = emp(name = n, joining_date = jd, email_id = ea, department = d, salary = s, job_status = js)
#             lst_obj.append(obj)
#         return lst_obj


# a = Opertions()
# print(emp.objects.get(id=10))
# emp.objects.bulk_create(a.get_data())


# print(emp.objects.all())
# print(emp.objects.values())
# print(emp.objects.values_list())

# q = (emp.objects.all()[0:5])  #LIMIT 5
# print(q.query)
# q = emp.objects.all()[5:10] #LIMIT 5 OFFSET 5
# print(q.query)


# from faker import Faker
# from random import *

# print(emp.objects.all()[0:5])
# print(emp.objects.values_list())
# print(emp.objects.count())
# print(emp.objects.first())
# print(emp.objects.filter(name__istartswith = "john"))
# print(emp.objects.filter(name__istartswith = "john"))
# print(emp.objects.filter(name__iin = ["john"]))


# from django.db import connection
# comm = connection.cursor()
# comm.execute("select * from emp_data")
# data=  comm.fetchall()
# print(data)
# data = emp.objects.raw("select * from emp_data where is_active = True")
# for x in data:
    # print(x.get("email_id"))

# from django.contrib.auth.models import User
# User creations 
# exec(open(r"D:\python_program\python_code\sample\app1\db_shell.py").read())

# print(User.objects.values_list())
# print(User.objects.count())
# print(User.objects.all())
# print(User.objects.values())
# User.objects.create(username = "Kalu", password = "Pass@123", email = "kalu@gamil.com")
# User.objects.create_user(username="swapnil",password = "Pass@123", email = "swapnil@gmail.com")
# User.objects.create(username= "Rohit")
# User.objects.get(username = "Rohit").delete()

# {'id': 2, 'password': 'pbkdf2_sha256$600000$8biMnmY6DaT7Y9VgRwgER0$HTrhN56RU5xFDSM/SPjafpegcKoJaFw2sofIbJ6RSwU=', 'last_login': None, 'is_superuser': False, 'username': 'KapilD', 'first_name': 'Kapil', 'last_name': 'Desmukh', 'email': 'kapil@gmail.cpm', 'is_staff': False, 'is_active': True, 'date_joined': datetime.datetime(2023, 6, 22, 22, 6, 15, 909518, tzinfo=datetime.timezone.utc)}

for x in User.objects.all():
    print(x.__dict__)

#     {'_state': <django.db.models.base.ModelState object at 0x000001ADFAD5AF40>, 'id': 1, 'password': 'pbkdf2_sha256$600000$HrUsCQ8nPrBnC9PndURdLs$GQqPG/jfPypCfLAttx9r19sJoRiQ3y7dTwYz+MgGEfY=', 'last_login': datetime.datetime(2023, 7, 14, 
# 0, 20, 55, 413659, tzinfo=datetime.timezone.utc), 'is_superuser': True, 'username': 'Bharat', 'first_name': '', 'last_name': '', 'email': '', 'is_staff': True, 'is_active': True, 'date_joined': datetime.datetime(2023, 6, 22, 2, 37, 4, 949024, tzinfo=datetime.timezone.utc)}