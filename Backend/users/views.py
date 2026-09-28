from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def hello(request):
    return JsonResponse({
        "message": "Hello Developer"
    })

def create_user(request):
    if request.method == "POST":
        return JsonResponse({
            "message": "User created successfully"
        })

    return JsonResponse({
        "message": "Only POST method is allowed"
    }, status=405)



def users(request):


    return JsonResponse({
        "users":[
            {
                "id":1,
                "name":"Imthiyas Alam",
                "mobile":8271665964
            },
            {
                "id":2,
                "name":"Alam",
                "mobile":9783737378
            }
        ]
    })