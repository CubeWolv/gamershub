from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount' ,'created_on')
    search_fields = ('title','amount')

    