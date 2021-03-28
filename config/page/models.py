from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=128)
    artist = models.CharField(max_length=45)
    album = models.CharField(max_length=128)
    genre = models.CharField(max_length=45)
    dates = models.DateField()
    lyrics = models.CharField(max_length=2000)

    class Meta:
        db_table = 'song'
    def __str__(self):
        return self.title

class pregenre(models.Model):
    pregenre1 = models.CharField(max_length=45)
    pregenre2 = models.CharField(max_length=45)

    class Meta:
        db_table = 'pregenre'

class Tag(models.Model):
    tag_name = models.CharField(max_length=45)
    song = models.ManyToManyField(Song)

    class Meta:
        db_table = 'tag'
    def __str__(self):
        return self.tag_name