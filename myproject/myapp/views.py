from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view(request):
    print("request: ", request.GET.get("pwd"))
    

    c = {}
    c["username"] = request.GET.get("username")
    c["age"] = 40
    c["majors"] = [
        "MIS",
        "ORM",
        "FINANCE",
        "ACCOUNTING",
        "ECONOMIC",
        "PUBLIC ADMIN",
    ]

    return render(request, "template2.html", c )

