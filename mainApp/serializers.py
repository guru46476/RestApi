from .models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=50)
    dsg = serializers.CharField(max_length=20)
    salary = serializers.IntegerField()
    city = serializers.CharField(max_length=20)
    state = serializers.CharField(max_length=20)


    def create(self,validateData):
        return Employee.objects.create(**validateData)

    def update(self, instance, validatedData):
        if("name" in validatedData and validatedData["name"]!=""):
            instance.name = validatedData["name"]
        if("email" in validatedData and validatedData["email"]!=""):
            instance.email = validatedData["email"]
        if("dsg" in validatedData and validatedData["dsg"]!=""):
            instance.dsg = validatedData["dsg"]
        if("salary" in validatedData and validatedData["salary"]!=""):
            instance.salary = validatedData["salary"]
        if("city" in validatedData and validatedData["city"]!=""):
            instance.city = validatedData["city"]
        if("state" in validatedData and validatedData["state"]!=""):
            instance.state = validatedData["state"]   
        instance.save()     
        return instance
