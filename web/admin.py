from django.contrib import admin
from . models import Contact,Enquiry
from . models import Email,EnquiryForm
# Register your models here.

admin.site.register(Email)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name","email","subject","message")
    search_fields = ("name","email","subject","message")
    list_filter = ("name","email","subject","message")

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("admin_photo", "title", "paragraph")
    search_fields = ("icon", "title", "paragraph")
    list_filter = ("icon", "title", "paragraph")

@admin.register(EnquiryForm)
class Enquiry_FormAdmin(admin.ModelAdmin):
    list_display = ("Product","Name","Phone","Message")
    search_fields = ("Product","Name","Phone","Message")
    list_filter = ("Product","Name","Phone","Message")
