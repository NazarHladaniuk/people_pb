from django.shortcuts import render
from .models import Employee


def employee_list(request):
    query = request.GET.get('q')
    sort = request.GET.get('sort')

    employees = Employee.objects.prefetch_related('positions__org_unit')

    # 🔍 Пошук
    if query:
        employees = employees.filter(
            last_name__icontains=query
        )

    # 🔽 Сортування
    sort_options = {
        'name_asc': 'last_name',
        'name_desc': '-last_name',
        'phone_asc': 'phone',
        'phone_desc': '-phone',
    }

    if sort in sort_options:
        employees = employees.order_by(sort_options[sort])
    else:
        employees = employees.order_by('last_name')  # дефолт

    return render(request, 'directory/employee_list.html', {
        'employees': employees,
        'current_sort': sort,
        'query': query,
    })
