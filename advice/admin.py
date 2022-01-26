from django.contrib import admin

# Register your models here.
from advice.models import Question, Advice

admin.site.register(Question)
admin.site.register(Advice)
