from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import *
import requests

# Create your views here.

from django.http import HttpResponse


@login_required
def home(request):
    cards = Card.objects.order_by('-date') # Orders the objects in card by which one is the most recent
    sections = Section.objects.all() #creates a var storing all the objects in section in a query set

    


    context = {             #Creates context to tell what the html file what this is
        "sections":sections,
        "cards":cards,
    }

    return render(request, 'mma/home.html', context) #Loads the page aswell as providing the context


def add_current_year(request):

    headers = {
        'x-rapidapi-key': "5b75fc0d46msh02b955b71af77e3p11e2eejsn1370037ac75f",
        # 'x-rapidapi-host': "mma-stats.p.rapidapi.com"
    }

    url = f"http://mma-stats.p.rapidapi.com/fights_by_year?year=2024"

    response = requests.get(url, headers=headers)

    print(response.json())
    print(response)

    return HttpResponse('check console')

########## signup #################### signup #################### signup #################### signup #################### signup #################### signup #################### signup #################### signup #################### signup #################### signup ##########

# Signup Page #

def signup(request):
    return render(request, "mma/signup.html") 

# Signup function, creates user #

def sign_up(request):

    print(request.POST)

    user = User.objects.create_user( # Updates the User table by creating new objects with the new information below
        
        # Requests value entered by the user

        username=request.POST["username"], 
        email=request.POST["email"],
        password=request.POST["password"],
        first_name=request.POST["first"],
        last_name=request.POST["last"]

        )
    
    if user:
        login(request, user) # tells the web server that this computer has been authorised and logged in
        return redirect('mma:home') # If the user already exists send to the home page

    return redirect('mma:signup') # Send the user to the homepage after creating an account

########## login #################### login #################### login #################### login #################### login #################### login #################### login #################### login #################### login #################### login ##########

def log_in(request, context=None):
    return render(request, "mma/login.html", context) # Login page

def authorisation(request):

    # Requests value entered by the user

    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password) # authorsing username and password, checking if they are the same in the data base and returns a value

    if user is not None: #if the value returned is not none program proceeds and login was successful
        login(request, user) # tells the web server that this computer has been authorised and logged in
        return redirect("mma:home") #redirects user to home page
    
    else:
        return log_in(request, {'error': 'Incorrect username or password'}) # if the value returned was none the user is redirected to a fail page where their login was incorrect
    
    
def fail(request):
    return HttpResponse("Wrong username or password!") # Failed login page

########## fight_review #################### fight_review #################### fight_review #################### fight_review #################### fight_review #################### fight_review #################### fight_review #################### fight_review #################### fight_review #################### fight_review ##########

@login_required
def fight_page(request, fight_id):
    reviews_list = Fight_review.objects.order_by('-pub_date')
    fight = Fight.objects.get(id=fight_id)

    context = {

        'fight':fight,
        'reviews_list':reviews_list,


    }

    return render(request, 'mma/fightpage.html', context)

@login_required
def post_fight_review(request, fight_id):
    review_text = request.POST["review"]
    fight = Fight.objects.get(id=fight_id)
    review = Fight_review(fight=fight, rev_text=review_text, author=request.user)
    review.save()

    return redirect(request.META['HTTP_REFERER'])

########## fighter_ page #################### fighter_ page #################### fighter_ page #################### fighter_ page #################### fighter_ page #################### fighter_ page #################### fighter_ page #################### fighter_ page #################### fighter_ page #################### fighter_ page ##########

@login_required
def fighter_page(request, fighter_id):
    fighter = Fighter.objects.get(id=fighter_id)

    context = {

        'fighter':fighter,
        'reviews_list': fighter.fighter_review_set.all().order_by('-pub_date'),

    }

    return render(request, 'mma/fighterpage.html', context)
@login_required
def post_fighter_review(request, fighter_id):
    review_text = request.POST["review"]
    fighter = Fighter.objects.get(id=fighter_id)
    review = Fighter_review(fighter=fighter, rev_text=review_text, author=request.user)
    review.save()

    return redirect(request.META['HTTP_REFERER'])

########## card_page #################### card_page #################### card_page #################### card_page #################### card_page #################### card_page #################### card_page #################### card_page #################### card_page #################### card_page ##########

@login_required
def view_card(request, card_id):
    card = Card.objects.get(id=card_id)
    sections = Section.objects.all()

    context = {

        "sections":sections,
        'card':card

    }

    return render(request, 'mma/cardview.html', context)

########## thread #################### thread #################### thread #################### thread #################### thread #################### thread #################### thread #################### thread #################### thread #################### thread ##########

def thread(request):
    threads = Thread.objects.order_by('-pub_date')

    context = {
        'threads':threads
    }

    return render(request, 'mma/thread.html', context)

def post_thread(request):
    thread_title = request.POST['thread_title']
    thread_text = request.POST['thread_text']
    thread = Thread(thread_title=thread_title, thread_text=thread_text, author=request.user)

    thread.save()

    return redirect(request.META['HTTP_REFERER'])

def view_thread(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    thread_comments = thread.thread_comment_set.order_by('-pub_date')
    print(thread_comments)

    print(Thread_comment_reply.objects.all()) # hear me out apprently the replies are going to comment objects which dont exist e.g I reply on comment 3 but instead it goes to comment 1 weird.

    context = {
        'thread_comments':thread_comments,
        'thread':thread
    }

    return render(request, 'mma/view_thread.html', context)

def post_thread_comment(request, thread_id):
    thread_comment_text = request.POST['thread_comment']
    thread = Thread.objects.get(id=thread_id)
    thread_comment = Thread_comment(thread=thread, thread_com_text=thread_comment_text, author=request.user)
    thread_comment.save()

    return redirect(request.META['HTTP_REFERER'])

def post_thread_comment_reply(request, thread_comment_id):
    thread_comment_reply_text = request.POST['thread_comment_reply']
    thread_comment = Thread_comment.objects.get(id=thread_comment_id)
    thread_comment_reply = Thread_comment_reply(thread_comment=thread_comment, text=thread_comment_reply_text, author=request.user)
    thread_comment_reply.save()

    return redirect(request.META['HTTP_REFERER'])


def like_thread(request, thread_id):
    return like_object(request, thread_id, Thread)

def unlike_thread(request, thread_id):
    return unlike_object(request, thread_id, Thread)


def delete_thread(request, thread_id):
    return delete_object(request, thread_id, Thread)



def like_thread_comment(request, thread_comment_id):
    return like_object(request, thread_comment_id, Thread_comment)

def unlike_thread_comment(request, thread_comment_id):
    return unlike_object(request, thread_comment_id, Thread_comment)


def delete_thread_comment(request, thread_comment_id):
    return delete_object(request, thread_comment_id, Thread_comment)



def like_thread_comment_reply(request, thread_comment_reply_id):
    return like_object(request, thread_comment_reply_id, Thread_comment_reply)

def unlike_thread_comment_reply(request, thread_comment_reply_id):
    return unlike_object(request, thread_comment_reply_id, Thread_comment_reply)


def delete_thread_comment_reply(request, thread_comment_reply_id):
    return delete_object(request, thread_comment_reply_id, Thread_comment_reply)

########## like, unlike, delete #################### like, unlike, delete #################### like, unlike, delete #################### like, unlike, delete #################### like, unlike, delete #################### like, unlike, delete #################### like, unlike, delete #################### like, unlike, delete #################### like, unlike, delete #################### like, unlike, delete ##########

def like_object(request, object_id, object_class):
    obj = object_class.objects.get(id=object_id)
    obj.likers.add(request.user)
    obj.save()

    return redirect(request.META['HTTP_REFERER'])


def unlike_object(request, object_id, object_class):
    obj = object_class.objects.get(id=object_id)
    obj.likers.remove(request.user)
    obj.save()

    return redirect(request.META['HTTP_REFERER'])


def delete_object(request, object_id, object_class):
    obj = object_class.objects.get(id=object_id)
    obj.delete()

    return redirect(request.META['HTTP_REFERER'])
