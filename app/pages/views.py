from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_desc": "Длинный текст о компании...",
        "my_number": "+7-999-77-43",
        "my_list": [11, 12, 13, 'Abc', "test_string"],
        "my_html": "<h3>Большая компания</h3>"
    }
    return render(request, "about.html", my_context)

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
