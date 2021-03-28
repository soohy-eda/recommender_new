from django.contrib import admin

from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('username','password', 'pregenre1', 'pregenre2', 'created_at', 'updated_at')

admin.site.register(Member, MemberAdmin)

