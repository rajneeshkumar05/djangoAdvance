from django.contrib import admin
from .models import YouTubeUser

@admin.register(YouTubeUser)
class YouTubeUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscribers')
# Register your models here.
