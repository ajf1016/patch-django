import json

from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.urls import reverse

from web.models import Subscribe, Testimonials, Promoter, Faq


def index(request):
    testimonials = Testimonials.objects.all()
    promoters = Promoter.objects.all()
    rent_tracking_faqs = Faq.objects.filter(faq_type="rent_tracking")
    new_deposite_faqs = Faq.objects.filter(faq_type="new_deposite")
    existing_deposite_faqs = Faq.objects.filter(faq_type="existing_deposite")

    print(rent_tracking_faqs)

    context = {
        "testimonials": testimonials,
        "promoters": promoters,
        "rent_tracking_faqs": rent_tracking_faqs,
        "new_deposite_faqs": new_deposite_faqs,
        "existing_deposite_faqs": existing_deposite_faqs
    }

    return render(request, "index.html", context=context)


def subscribe(request):
    data = request.POST.get("email")

    if not Subscribe.objects.filter(email=data).exists():

        Subscribe.objects.create(
            email=data
        )

        response_data = {
            "status": "success",
            "title": "Successfully registred",
            "message": "You are subscribed our newsletter successfully!!"
        }
    else:
        response_data = {
            "status": "error",
            "title": "You are alreday a member",
            "message": "no need subscription"
        }

    return HttpResponse(json.dumps(response_data), content_type="application/javascript")
