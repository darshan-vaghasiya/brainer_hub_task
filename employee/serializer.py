from rest_framework import serializers
from .models import Company, Employee


class EmployeeImportSerializer(serializers.Serializer):
    file = serializers.FileField()


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']


class EmployeeSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Employee
        fields = '__all__'
