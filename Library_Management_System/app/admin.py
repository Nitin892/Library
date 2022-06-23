from django.contrib import admin
from .models import Book
# Register your models here.
class BookCreated(admin.ModelAdmin):
    readonly_fields = ("date",)

# admin.site.register(BookUser)
admin.site.register(Book,BookCreated)


