from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from .models import AirportsFiltered, AirportsFAA

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

    list_filter = [('type', DropdownFilter),
                   ('municipality', DropdownFilter),
                   ('iso_region', DropdownFilter),
                   ('iso_country', DropdownFilter),
                   ('timezone', DropdownFilter),]

admin.site.register(AirportsFiltered, AirportsFilteredAdmin)


class AirportsFAAAdmin(admin.ModelAdmin):
    list_display = ['facility_name',
                    'city',
                    'county',
                    'state_name',]

    search_fields = ['facility_name',
                    'city',
                    'county',
                    'state_name',]

    list_filter = [('state_name', DropdownFilter),
                   ('county', DropdownFilter),
                   ('city', DropdownFilter),]

admin.site.register(AirportsFAA, AirportsFAAAdmin)
