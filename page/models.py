from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=128)
    artist = models.CharField(max_length=45)
    album = models.CharField(max_length=128)
    genre = models.CharField(max_length=45)
    dates = models.DateField()
    lyrics = models.CharField(max_length=2000)
    tag = models.CharField(max_length=45)

    class Meta:
        db_table = 'song'
    def __str__(self):
        return self.title, self.artist, self.tag