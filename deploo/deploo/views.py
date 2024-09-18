from django.shortcuts import render


def landing_page(request):
    return render(request, "landing.html")


from django.http import HttpResponse


def load_more(request):
    return HttpResponse("<p>Here’s some more content loaded with HTMX!</p>")
