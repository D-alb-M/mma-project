from django.urls import path

from . import views

app_name = "mma"

urlpatterns = [
    path("home", views.home, name="home"),

    ### card_view ###

    path('viewcard/<int:card_id>', views.view_card, name='viewcard'),

    ### fight_review ###

    path('fightpage/<int:fight_id>', views.fight_page, name='fightpage'),
    path('post_fight_review/<int:fight_id>', views.post_fight_review, name='post_fight_review'),

    ### fighter_page ###

    path('fighterpage/<int:fighter_id>', views.fighter_page, name="fighterpage"),
    path('post_fighter_review/<int:fighter_id>', views.post_fighter_review, name='post_fighter_review'),

    ### thread ###

    path('discussion', views.thread, name='discussion'),

    path('create_thread', views.post_thread, name='create_thread'),

    path('viewdiscussion/<int:thread_id>', views.view_thread , name='viewdiscussion'),

    path('post_thread_comment/<int:thread_id>', views.post_thread_comment, name='post_thread_comment'),

    path('post_thread_comment_reply/<int:thread_comment_id>', views.post_thread_comment_reply, name='post_thread_comment_reply'),



    
    path('like_thread/<int:thread_id>', views.like_thread, name='like_thread'),

    path('unlike_thread/<int:thread_id>', views.unlike_thread, name='unlike_thread'),

    path('delete_thread/<int:thread_id>', views.delete_thread, name='delete_thread'),



    path('like_thread_comment/<int:thread_comment_id>', views.like_thread_comment, name='like_thread_comment'),

    path('unlike_thread_comment/<int:thread_comment_id>', views.unlike_thread_comment, name='unlike_thread_comment'),

    path('delete_thread_comment/<int:thread_comment_id>', views.delete_thread_comment, name='delete_thread_comment'),



    path('like_thread_comment_reply/<int:thread_comment_reply_id>', views.like_thread_comment_reply, name='like_thread_comment_reply'),

    path('unlike_thread_comment_reply/<int:thread_comment_reply_id>', views.unlike_thread_comment_reply, name='unlike_thread_comment_reply'),

    path('delete_thread_comment_reply/<int:thread_comment_reply_id>', views.delete_thread_comment_reply, name='delete_thread_comment_reply'),


    ### signup ###

    path("signup", views.signup, name="signup"), # Page.
    path("sign_up", views.sign_up, name="sign_up"), # Creates account.

    ### login ###

    path("login", views.log_in, name="login"), #Page.
    path("authorisation", views.authorisation, name="authorisation"), # Authorisation function. checks if user detail's are correct.
    path("fail", views.fail, name="fail"),


    ### admin pages ###

    path("addcards", views.add_current_year, name="addcards"),


]