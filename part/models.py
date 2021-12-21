from django.db import models
from django import forms
from phone_field import PhoneField
from django.contrib.auth.models import User
from django.urls import reverse
from django_countries.fields import CountryField
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=50)
    introduction = models.TextField(null=True)
    achievements = models.CharField(max_length=200)
    youtube_account = models.URLField(blank=True ,max_length=150)
    instagram_account = models.URLField(blank=True ,max_length=150)
    facebook_Account = models.URLField(blank=True ,max_length=150)
    twitter_account = models.URLField(blank=True ,max_length=150)
    fav_game = models.CharField(max_length=150)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

PARTICIPANTS = (
    ('Players','Players'),
    ('Teams','Teams')
)
class Organize(models.Model):
    tournament_name = models.CharField(max_length=100)
    organizer_name = models.CharField(max_length=100)
    discipline =  models.CharField(max_length=100)
    size = models.IntegerField(help_text='Size of players/teams')
    prize_pool = models.DecimalField(max_digits=9, decimal_places=2, help_text='Currency IN')
    participants = models.CharField(max_length=10, choices= PARTICIPANTS ,blank=False)
    banner = models.ImageField(default='default.jpg', upload_to='profile_pics')
    description = models.TextField(null=True)
    youtube_account = models.URLField(blank=True ,max_length=150)
    instagram_account = models.URLField(blank=True ,max_length=150)
    discord_account = models.URLField(blank=True ,max_length=150)
    twitter_account = models.URLField(blank=True ,max_length=150)
    country = CountryField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):
        return self.tournament_name

    def get_absolute_url(self):
        return reverse('home')        

class Participating(models.Model):
    email = models.EmailField()
    team_Name = models.CharField(max_length=50)
    player_Name = models.CharField(max_length=50)
    contact_No = PhoneField(help_text='Contact phone number')
    player_1_IGN = models.CharField(max_length=50)
    player_2_IGN = models.CharField(max_length=50)
    player_3_IGN = models.CharField(max_length=50)
    player_4_IGN = models.CharField(max_length=50)
    player_5_IGN = models.CharField(max_length=50)
    player_6_IGN = models.CharField(max_length=50,blank=True)
    player_7_IGN = models.CharField(max_length=50,blank=True)
    team_LOGO = models.ImageField(default='default.jpg', upload_to='profile_pics')
    tournament_Name = models.ForeignKey(Organize, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  


    def __str__(self):
        return (self.team_Name or self.player_Name)

    def get_absolute_url(self):
        return reverse('participated')        