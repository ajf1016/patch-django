from django.contrib import admin
from web.models import Faq, Profile, StudentGroup, Testimonials, Promoter,Subscribe,TestModel,Car,Manufacturer,Student,StudentGroup


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "image", "designation"]


admin.site.register(Testimonials, TestimonialAdmin)


class PromoterAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "image"]


admin.site.register(Promoter, PromoterAdmin)


class FaqAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "faq_type"]


admin.site.register(Faq, FaqAdmin)

admin.site.register(Subscribe)

admin.site.register(TestModel)

admin.site.register(Car)
admin.site.register(Manufacturer)
admin.site.register(Profile)

admin.site.register(Student)
admin.site.register(StudentGroup)