from django.contrib import admin
from .models import Customer, Parent, Child
# Register your models here.

class ParentInForm(admin.TabularInline):
    model = Parent
    extra = 2

class ChildInForm(admin.TabularInline):
    model = Child
    extra = 2

class CustomerAdmin(admin.ModelAdmin):
    inlines = [ParentInForm, ChildInForm]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Parent)
admin.site.register(Child)