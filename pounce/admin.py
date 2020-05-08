from django.contrib import admin

from .models import Course, Section, Subscription


class SectionInline(admin.StackedInline):
    model = Section
    extra = 2


class CourseAdmin(admin.ModelAdmin):
    inlines = [SectionInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Subscription)
