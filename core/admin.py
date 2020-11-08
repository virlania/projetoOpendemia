from django.contrib import admin
from .models import AmigosFacebook
# Register your models here.

@admin.register(AmigosFacebook)
class AmigosFacebookAdmin(admin.ModelAdmin):
    list_display = ['name', 'idFacebook', 'doencas']