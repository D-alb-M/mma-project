from django.contrib import admin

from .models import *

# Register your models so they are viewable on the admin site.

admin.site.register(Card)
admin.site.register(Fighter)
admin.site.register(Fight)
admin.site.register(Fight_review)
admin.site.register(Fighter_review)
admin.site.register(Thread)
admin.site.register(Thread_comment)
admin.site.register(Division)
admin.site.register(Section)
admin.site.register(Bout)
admin.site.register(Thread_comment_reply)
