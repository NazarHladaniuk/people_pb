from django.contrib import admin
from .models import Employee, OrgUnit, Position, Status


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('middle_name', 'first_name', 'last_name', 'phone')
    search_fields = ('middle_name', 'first_name', 'last_name', 'phone')


@admin.register(OrgUnit)
class OrgUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('employee', 'org_unit', 'title')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')
