from django.db import models
from multiselectfield import MultiSelectField


class FeedbackData(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    date = models.DateField()
    feedback = models.TextField(max_length=1000)

class ContactData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()

    COURSES_CHOCIES = (
        ('py','Python'),
        ('dj','Django'),
        ('ui','UI'),
        ('rest','Rest API')
    )
    courses = MultiSelectField(max_length=200,choices=COURSES_CHOCIES)

    SHIFT_CHOICES = (
        ('mrg','Morning'),
        ('aftn','AfterNoon'),
        ('evng','Evening'),
        ('night','Night')
    )
    shifts = MultiSelectField(max_length=200,choices=SHIFT_CHOICES)

    LOCATION_CHOICES = (
        ('hyd','Hyderabad'),
        ('bang','Banglore'),
        ('che','Chennai'),
        ('pune','Pune')
    )
    locations = MultiSelectField(max_length=200,choices=LOCATION_CHOICES)

    gender = models.CharField(max_length=20)
    start_date = models.DateField(max_length=50)


class CoursesData(models.Model):
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=100)
    course_dur = models.IntegerField()
    course_fee = models.IntegerField()
    start_date = models.DateField(max_length=100)
    start_time = models.TimeField(max_length=100)
    trainer_name = models.CharField(max_length=100)
    trainer_exp = models.IntegerField()