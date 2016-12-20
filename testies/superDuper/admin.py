from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from .models import AirportsFiltered, AirportsFAA, DatabaseFAA, City, DatabaseFAATimezone, County

# Register your models here.

class CityAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'county',
                    'id']

    search_fields = ['name',]

admin.site.register(City, CityAdmin)


class CountyAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'state',
                    'id']
    search_fields = ['name',]

admin.site.register(County, CountyAdmin)


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


class DatabaseFAAAdmin(admin.ModelAdmin):
    list_display = ['facility_name',]

    search_fields = ['facility_name',]

    list_filter = [('facility_name', DropdownFilter),
                   ('city_id', RelatedDropdownFilter),]

admin.site.register(DatabaseFAA, DatabaseFAAAdmin)


# class DatabaseFAAOpts(admin.ModelAdmin):
#     list_filter = [('city_id__county_id', RelatedOnlyFieldListFilter,),]
#     # raw_id_admin = ('facility_name', )

#     search_fields = ['facility_name',]

# admin.site.register(DatabaseFAA, DatabaseFAAOpts)


class DatabaseFAATimezoneAdmin(admin.ModelAdmin):
    list_display = ['facility_name',
                    'get_city',
                    'get_county',
                    'get_state',
                    'timezone']

    def get_city(self, obj):
        return obj.city
    get_city.short_description = 'City'
    get_city.admin_order_field = 'city__name'

    def get_county(self, obj):
        return obj.city.county
    get_county.short_description = 'County'
    get_county.admin_order_field = 'city__county__name'

    def get_state(self, obj):
        return obj.city.county.state
    get_state.short_description = 'State'
    get_state.admin_order_field = 'city__county__state__name'

    list_filter = [('city__county__state__faa_region', RelatedDropdownFilter),
                   ('city__county__state', RelatedDropdownFilter),
                   ('city__county', RelatedDropdownFilter),]

    search_fields = ['facility_name',
                     'city__name',
                     'city__county__name',
                     'city__county__state__name']

admin.site.register(DatabaseFAATimezone, DatabaseFAATimezoneAdmin)
