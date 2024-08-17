from django.contrib import admin
from home.models import Person, Answers, Question

admin.site.register(Person)
admin.site.register(Question)
admin.site.register(Answers)
