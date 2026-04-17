from django.shortcuts import render
from django.db.models import Q
from .models import Employee


def employee_list(request):
    query = request.GET.get('q', '').strip()

    employees = Employee.objects.prefetch_related('positions__org_unit')

    if query:
        employees = employees.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(middle_name__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query)
        )

    if request.headers.get('HX-Request'):
        return render(request, 'directory/partials/employee_cards.html', {
            'employees': employees
        })

    return render(request, 'directory/employee_list.html', {
        'employees': employees,
        'query': query,
    })
