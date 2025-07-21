from django.urls import path
from .views import EmployeeUploadView, EmployeeListView

urlpatterns = [
    path('upload-employees', EmployeeUploadView.as_view(), name='upload-employees'),
    path('employees', EmployeeListView.as_view(), name='employee-list'),
]
