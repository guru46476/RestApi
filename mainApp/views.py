from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import EmployeeSerializer
from .models import Employee
from django.views.decorators.csrf import csrf_exempt


def home(request):
    data = Employee.objects.all()
    return render(request, "index.html",{"Data":data[::-1]})


def addPage(request):
    if(request.method=='POST'):
        e = Employee()
        e.name = request.POST.get('name')
        e.email = request.POST.get('email')
        e.dsg = request.POST.get('dsg')
        e.salary = request.POST.get('salary')
        e.city = request.POST.get('city')
        e.state = request.POST.get('state')
        e.save()
        return HttpResponseRedirect('/')
    return render(request, "add.html")    


def updateRecord(request,ID):
    data = Employee.objects.get(id=ID)
    if(request.method=='POST'):
        data.name = request.POST.get('name')
        data.email = request.POST.get('email')
        data.dsg = request.POST.get('dsg')
        data.salary = request.POST.get('salary')
        data.city = request.POST.get('city')
        data.state = request.POST.get('state')
        data.save()
        return HttpResponseRedirect('/')
    return render(request, "update.html", {"Data":data})


def deleteRecord(request, num):
    data = Employee.objects.get(id=num) 
    data.delete()
    return HttpResponseRedirect("/")


@csrf_exempt
def api(request):
    if(request.method == 'GET'):
        jData = request.body
        stream = io.BytesIO(jData)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id', None)
        name = pdata.get('name', None)
        email = pdata.get('email', None)
        dsg = pdata.get('dsg', None)
        salary = pdata.get('salary', None)
        city = pdata.get('city', None)
        state = pdata.get('state', None)

        if(id):
            data = Employee.objects.filter(id=id)
        elif(name):
            data = Employee.objects.filter(name=name)
        elif(email):
            data = Employee.objects.filter(email=email)
        elif(dsg):
            data = Employee.objects.filter(dsg=dsg)
        elif(salary):
            data = Employee.objects.filter(salary=salary)
        elif(city):
            data = Employee.objects.filter(city=city)
        elif(state):
            data = Employee.objects.filter(state=state)
        else:
            data = Employee.objects.all()

        empSerializer = EmployeeSerializer(data, many=True)
        jData = JSONRenderer().render(empSerializer.data)
        return HttpResponse(jData, content_type="application/json")

    elif(request.method == 'POST'):
        jData = request.body
        stream = io.BytesIO(jData)
        pdata = JSONParser().parse(stream)
        empSerializer = EmployeeSerializer(data=pdata)
        if(empSerializer.is_valid()):
            empSerializer.save()
            res = {"msg": "Record Inserted!!!"}
        else:
            res = {"msg": "Invalid Records!!!"}

        jData = JSONRenderer().render(res)
        return HttpResponse(jData, content_type="application/json")

    elif(request.method == 'PUT'):
        jData = request.body
        stream = io.BytesIO(jData)
        pdata = JSONParser().parse(stream)
        id = pdata.get("id","None")
        try:
            emp = Employee.objects.get(id=id)
            empSerializer = EmployeeSerializer(emp, pdata, partial=True)
            if(empSerializer.is_valid()):
                empSerializer.save()
                res = {"msg":"Record updated!!!"}
            else:
                res = {"msg":"Invalid Record"}    
        except: 
            res = {"msg":"No Record Found To Update!!!"}

        jData = JSONRenderer().render(res)
        return HttpResponse(jData, content_type="application/json")

    elif(request.method=='DELETE'):
        jData = request.body
        stream = io.BytesIO(jData)
        pdata = JSONParser().parse(stream)
        id = pdata.get("id","None")
        try:
            emp = Employee.objects.get(id=id)
            emp.delete()
            res = {"msg":"Record Delete!!!"}
        except:
            res = {"msg":"No Record Found to Deleted!!!"}
            
        jData = JSONRenderer().render(res)
        return HttpResponse(jData,content_type="application/json")        
