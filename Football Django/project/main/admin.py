from django.contrib import admin
from .models import Team, Championship, Achievement, Message

admin.site.register(Team)
admin.site.register(Championship)
admin.site.register(Achievement)
admin.site.register(Message)