from django.contrib import admin

from .models import Customer, Parent, Child, Images


# Register your models here.


class ParentInForm(admin.TabularInline):
    model = Parent
    extra = 2


class ChildInForm(admin.TabularInline):
    model = Child
    extra = 2


class CustomerAdmin(admin.ModelAdmin):
    inlines = [ParentInForm, ChildInForm]

    def get_fieldsets(self, request, obj=None):
        if obj and request.user.groups.filter(name='ViewName').exists():
            return (
                (None, {'fields': ('name',)}),
            )
        else:
            return (
                (None, {'fields': ('address',)}),
            )


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(Images)
