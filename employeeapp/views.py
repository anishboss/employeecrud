from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import Employee,Department,Role

# Create your views here.

def index(request):
    employees = Employee.objects.all()
    context = {'employees':employees}
    return render(request,'employeeapp/index.html',context)

def add_employee(request):
    departments = Department.objects.all()
    roles = Role.objects.all()
    context = {"departments":departments,"roles":roles}
    if request.method =="POST":
        name = request.POST['fname']
        email = request.POST['email']
        address = request.POST['address']
        phone = int(request.POST['phone'])
        dept = int(request.POST['department'])
        role = int(request.POST['role'])
        salary = int(request.POST['salary'])
        try:
            employee = Employee(name=name,email=email,address=address,phone=phone,dept_id=dept,role_id=role,salary=salary)
            employee.save()
            return redirect('/')
        except:
            return HttpResponse("error while saving employee")
    else:
        return render(request,'employeeapp/create_employee.html',context)

def edit_employee(request,id):
    employee = Employee.objects.get(id=id)
    departments = Department.objects.all()
    roles = Role.objects.all()
    context = {'employee':employee,'departments':departments,'roles':roles}

    if request.method =="POST":
        name = request.POST['fname']
        email = request.POST['email']
        address = request.POST['address']
        phone = int(request.POST['phone'])
        dept = int(request.POST['department'])
        role = int(request.POST['role'])
        salary = int(request.POST['salary'])
        
        employee.name = name
        employee.email = email
        employee.address = address
        employee.phone = phone
        employee.dept.id = dept
        employee.role.id = role
        employee.salary = salary
        employee.save()
        
        return redirect('/')

    return render(request,'employeeapp/edit_employee.html',context)

def emp_delete(request,id):
    employee = Employee.objects.filter(id=id)
    employee.delete()
    return redirect('/')


def department(request):
    departments = Department.objects.all()
    context = {'departments':departments}
    return render(request,'employeeapp/department.html',context)

def add_department(request):
    if request.method == "POST":
        dept_name = request.POST.get('department')
        department = Department(name=dept_name)
        department.save()
        return redirect('/department')

def edit_department(request,id):
    dept = Department.objects.get(id=id)
    context = {'department':dept}
    print(dept.id)
  
    return render(request,'employeeapp/edit_department.html',context)