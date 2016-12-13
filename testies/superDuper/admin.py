from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from .models import AirportsFiltered

# Register your models here.


class AirportsFilteredAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'municipality',
                    'iso_region',
                    'iso_country',
                    'type',
                    'timezone',]

    search_fields = ['name',
                    'municipality',
                    'iso_region',
                    'iso_country',
                    'type',
                    'timezone',]

    list_filter = [('municipality', DropdownFilter),
                   ('iso_region', DropdownFilter),
                   ('iso_country', DropdownFilter),
                   ('type', DropdownFilter),
                   ('timezone', DropdownFilter),]

admin.site.register(AirportsFiltered, AirportsFilteredAdmin)
