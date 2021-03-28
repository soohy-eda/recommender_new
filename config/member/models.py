from django.db import models
from page.models import *

class Member(models.Model):
    username = models.CharField(max_length=128, verbose_name='사용자ID')
    password = models.CharField(max_length=100, verbose_name='사용자PW')
    pregenre1 = models.CharField(max_length=45, verbose_name='선호장르1')
    pregenre2 = models.CharField(max_length=45, verbose_name='선호장르2')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='마지막수정일')
    song = models.ManyToManyField(Song, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'members'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'