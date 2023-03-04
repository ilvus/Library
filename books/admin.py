from django.contrib import admin
from .models import Books, Publisher, Authors

# Register your models here.
admin.site.register(Books)
admin.site.register(Publisher)
admin.site.register(Authors)
