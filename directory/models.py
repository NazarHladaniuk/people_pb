from django.db import models


class OrgUnit(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children'
    )
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)

    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Position(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='positions')
    org_unit = models.ForeignKey(OrgUnit, on_delete=models.CASCADE, related_name='positions')

    title = models.CharField(max_length=255)
    is_primary = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.employee} - {self.title}"
