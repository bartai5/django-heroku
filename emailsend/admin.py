from django.contrib import admin
from .models import UserEmail

# Register your models here.
db_list = [
    UserEmail,
]

admin.site.register(db_list)