# Generated by Django 3.1.3 on 2021-03-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, verbose_name='사용자ID')),
                ('password', models.CharField(max_length=100, verbose_name='사용자PW')),
                ('pregenre1', models.CharField(max_length=45, verbose_name='선호장르1')),
                ('pregenre2', models.CharField(max_length=45, verbose_name='선호장르2')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='마지막수정일')),
                ('song', models.ManyToManyField(blank=True, to='page.Song')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'members',
            },
        ),
    ]
