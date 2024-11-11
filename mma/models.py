from django.utils import timezone
from django.db import models

from django.contrib.auth.models import User

# Create your models here.



######### FIGHTER MODELS ################### FIGHTER MODELS ################### FIGHTER MODELS ################### FIGHTER MODELS ################### FIGHTER MODELS ################### FIGHTER MODELS ################### FIGHTER MODELS ################### FIGHTER MODELS ################### FIGHTER MODELS ################### FIGHTER MODELS ##########

class Division(models.Model):
    name = models.CharField(max_length=50, default='')
    info = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Fighter(models.Model):
    name_text = models.CharField(max_length=200)
    dob = models.DateField(verbose_name='Date of Birth', blank=True, null=True)
    wins = models.PositiveSmallIntegerField(default=0)
    losses = models.PositiveSmallIntegerField(default=0)
    draws = models.PositiveSmallIntegerField(default=0)
    info = models.TextField(blank=True, null=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)

    def age(self):
        if not self.dob:
            return 0
        
        current_age = (timezone.now() - self.dob)
        return current_age
    
    def __str__(self) -> str:
        return f'{self.name_text}'



class Fighter_review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fighter_reviews')
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    rating = models.PositiveSmallIntegerField(default=0)
    rev_text = models.TextField(blank=True, null=True)
    likers = models.ManyToManyField(User, related_name='liked_fighter_reviews')
    fighter = models.ForeignKey(Fighter, on_delete=models.CASCADE)

######### FIGHT MODELS ################### FIGHT MODELS ################### FIGHT MODELS ################### FIGHT MODELS ################### FIGHT MODELS ################### FIGHT MODELS ################### FIGHT MODELS ################### FIGHT MODELS ################### FIGHT MODELS ################### FIGHT MODELS ##########

class Section(models.Model):

    name = models.CharField(max_length=50, default='')

    def __str__(self) -> str:
        return f'{self.name}'

class Card(models.Model):
    name = models.CharField(max_length=50, default='')
    date = models.DateField()

    def __str__(self) -> str:
        return f'{self.name}'
    
class Bout(models.Model):
    name = models.CharField(max_length=50, default='')
    info = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'



class Fight(models.Model):
    fighters = models.ManyToManyField(Fighter, related_name='fights')
    win_method = models.CharField(max_length=50, default='')
    winner = models.ForeignKey(Fighter, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='fights_won')
    info = models.TextField(blank=True, null=True)
    time = models.TimeField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Bout, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.fighters.all()}'



class Fight_review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fight_reviews')
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    rating = models.PositiveSmallIntegerField(default=0)
    rev_text = models.TextField(blank=True, null=True)
    likers = models.ManyToManyField(User, related_name='liked_fight_reviews')
    fight = models.ForeignKey(Fight, on_delete=models.CASCADE, related_name='fight_reviews')


 
######### THREAD MODELS ################### THREAD MODELS ################### THREAD MODELS ################### THREAD MODELS ################### THREAD MODELS ################### THREAD MODELS ################### THREAD MODELS ################### THREAD MODELS ################### THREAD MODELS ################### THREAD MODELS ##########

class Thread(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='threads')
    thread_title = models.CharField(max_length=100)
    thread_text = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    likers = models.ManyToManyField(User, related_name='liked_threads')



class Thread_comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thread_comments')
    thread_com_text = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    likers = models.ManyToManyField(User, related_name='liked_thread_comments')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'commentid: ({self.id})'

class Thread_comment_reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thread_comment_replies')
    text = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    likers = models.ManyToManyField(User, related_name='liked_thread_comment_replies')
    thread_comment = models.ForeignKey(Thread_comment, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'reply {self.id} for comment {self.thread_comment.id}'
    
    

 

 
