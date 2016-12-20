from django.db import models
from django.utils import timezone

import datetime

# Create your models here.


class AirportsFiltered(models.Model):
    openFlightsId = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    latitude_deg = models.DecimalField(max_digits=9,decimal_places=6)
    longitude_deg = models.DecimalField(max_digits=9,decimal_places=6)
    elevation_ft = models.IntegerField()
    continent = models.CharField(max_length=200)
    iso_country = models.CharField(max_length=200)
    iso_region = models.CharField(max_length=200)
    municipality = models.CharField(max_length=200)
    scheduled_service = models.CharField(max_length=200)
    gps_code = models.CharField(max_length=200)
    iata_code = models.CharField(max_length=200)
    local_code = models.CharField(max_length=200)
    home_link = models.CharField(max_length=200)
    wikipedia_link = models.CharField(max_length=200)
    timezone = models.CharField(max_length=200)

    def __str__(self):
        return self.name





class AirportsFAA(models.Model):
    site_number = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    location_id = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    district_office = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    state_name = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    county_state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    facility_name = models.CharField(max_length=200)
    arp_latitude = models.CharField(max_length=200)
    arp_latitude_s = models.CharField(max_length=200)
    arp_longitude = models.CharField(max_length=200)
    arp_longitude_s = models.CharField(max_length=200)
    arp_elevation = models.IntegerField()
    icao_identifier = models.CharField(max_length=200)

    def __str__(self):
        return self.facility_name


class Timezone(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FAA_Region(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=200)
    faa_region = models.ForeignKey("FAA_Region", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class County(models.Model):
    name = models.CharField(max_length=200)
    state = models.ForeignKey("State", on_delete=models.CASCADE)

    def __str__(self):
        return ", ".join([self.name, str(self.state)])


class City(models.Model):
    name = models.CharField(max_length=200)
    county = models.ForeignKey("County", on_delete=models.CASCADE)

    def __str__(self):
        return ", ".join([self.name, str(self.county.state)])


class DatabaseFAA(models.Model):
    site_number = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    location_id = models.CharField(max_length=200)
    district_office = models.CharField(max_length=200)
    county_state = models.CharField(max_length=200)
    facility_name = models.CharField(max_length=200)
    arp_latitude = models.CharField(max_length=200)
    arp_latitude_s = models.CharField(max_length=200)
    arp_longitude = models.CharField(max_length=200)
    arp_longitude_s = models.CharField(max_length=200)
    arp_elevation = models.IntegerField()
    icao_identifier = models.CharField(max_length=200)
    timezone = models.CharField(max_length=200)
    city_id = models.ForeignKey("City", on_delete=models.CASCADE)

    def __str__(self):
        return self.facility_name


class DatabaseFAATimezone(models.Model):
    site_number = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, blank=True)
    location_id = models.CharField(max_length=200)
    district_office = models.CharField(max_length=200, blank=True)
    county_state = models.CharField(max_length=200)
    facility_name = models.CharField(max_length=200)
    arp_latitude = models.CharField(max_length=200, blank=True)
    arp_latitude_s = models.CharField(max_length=200, blank=True)
    arp_longitude = models.CharField(max_length=200, blank=True)
    arp_longitude_s = models.CharField(max_length=200, blank=True)
    arp_elevation = models.IntegerField(blank=True)
    icao_identifier = models.CharField(max_length=200, blank=True)
    timezone = models.ForeignKey("Timezone", on_delete=models.CASCADE)
    city = models.ForeignKey("City", on_delete=models.CASCADE)

    def __str__(self):
        return self.facility_name


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

#     def __str__(self):
#         return self.question_text

#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now
#     was_published_recently.admin_order_field = 'pub_date'
#     was_published_recently.boolean = True
#     was_published_recently.short_description = 'Published recently?'


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text
