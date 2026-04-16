from django.shortcuts import render
from .models import Employee


def employee_list(request):
    query = request.GET.get('q')

    employees = Employee.objects.all()

    if query:
        employees = employees.filter(
            last_name__icontains=query
        )

    return render(request, 'directory/employee_list.html', {
        'employees': employees
    })
