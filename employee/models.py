from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=8)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    salary = models.BigIntegerField()
    manager_id = models.CharField(max_length=10)
    department_id = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
