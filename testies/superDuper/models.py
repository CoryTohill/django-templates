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


# # "icao": "ANYN",
#     "type": "medium_airport",
#     "name": "Nauru International Airport",
#     "latitude_deg": -0.547458,
#     "longitude_deg": 166.919006,
#     "elevation_ft": 22,
#     "continent": "OC",
#     "iso_country": "NR",
#     "iso_common_name": "Yaren",
#     "iso_region": "NR-14",
#     "municipality": "Yaren District",
#     "gps_code": "ANYN",
#     "iata_code": "INU",
#     "local_code": ""


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
