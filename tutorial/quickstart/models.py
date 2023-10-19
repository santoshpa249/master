from django.db import models

# Create your models here.


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Emotions(TimestampedModel):

    Id = models.IntegerField(primary_key=True)
    emotion = models.CharField(unique=True, max_length=200)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "emotions"


class Employee(TimestampedModel):
    Id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=200)

    class Meta:
        db_table = "employess"
