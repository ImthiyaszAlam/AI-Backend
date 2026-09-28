import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from users.models import User
# Create your views here.

def hello(request):
    return JsonResponse({
        "message": "Hello Developer"
    })

@csrf_exempt
def create_user(request):
    if request.method == "POST":

        data = json.loads(request.body)

        name = data["name"]
        mobile = data["mobile"]

        user = User.objects.create(
            name=name,
            mobile=mobile
        )

        return JsonResponse({
            "message": "User created successfully",
            "id": user.id,
            "name": user.name,
            "mobile": user.mobile
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