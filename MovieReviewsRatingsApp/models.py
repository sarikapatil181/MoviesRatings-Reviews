from django.db import models

# Create your models here.
class Movies(models.Model):
    Movie_ID=models.IntegerField()
    Movie_Name=models.CharField(max_length=100)
    Genres=models.CharField(max_length=50)
    class Meta:
        db_table="Movies"
class Ratings(models.Model):
    rating_ID=models.IntegerField()
    Movie_ID=models.IntegerField()
    Rating=models.FloatField()
    timestamp=models.DateTimeField()
    class Meta:
        db_table="Rating"
class Reviews(models.Model):
    review_ID=models.IntegerField()
    Movie_ID=models.IntegerField()
    Review=models.TextField(max_length=1000)
    timestamp=models.DateTimeField()
    class Meta:
        db_table="Review"
