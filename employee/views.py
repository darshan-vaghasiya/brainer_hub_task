import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Company, Employee
from .serializer import EmployeeImportSerializer, EmployeeSerializer


class EmployeeUploadView(APIView):

    def post(self, request):
        try:
            serializer = EmployeeImportSerializer(data=request.data)
            if serializer.is_valid():
                file = serializer.validated_data['file']
                df = pd.read_excel(file) if file.name.endswith('.xlsx') else pd.read_csv(file)

                company_names = df['COMPANY_NAME'].unique()
                existing_companies = Company.objects.filter(name__in=company_names)
                existing_company_map = {
                    c.name: c for c in existing_companies
                }
                new_companies = [
                    Company(name=name) for name in company_names if name not in existing_company_map
                ]
                Company.objects.bulk_create(new_companies)

                all_companies = Company.objects.all()
                company_map = {c.name: c for c in all_companies}
                employees = [
                    Employee(
                        company=company_map[row['COMPANY_NAME']],
                        emp_id=row['EMPLOYEE_ID'],
                        first_name=row['FIRST_NAME'],
                        last_name=row['LAST_NAME'],
                        salary=row['SALARY'],
                        manager_id=row['MANAGER_ID'],
                        department_id=row['DEPARTMENT_ID'],
                        phone_number=str(row['PHONE_NUMBER'])
                    ) for _, row in df.iterrows()
                ]
                Employee.objects.bulk_create(employees)
                return Response({'message': 'Data inserted successfully.'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': 'Something wants to wrong.'}, status=status.HTTP_400_BAD_REQUEST)


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.select_related('company').all()
    serializer_class = EmployeeSerializer
