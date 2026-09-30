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
    users = User.objects.all()

    user_list = []

    for user in users:
        user_list.append({
            "id": user.id,
            "name": user.name,
            "mobile": user.mobile
        })

    return JsonResponse({
        "users": user_list
    })


def user_detail(request, id):
    user = User.objects.get(id=id)

    return JsonResponse({
        "id": user.id,
        "name": user.name,
        "mobile": user.mobile
    })

@csrf_exempt
def update_user(request, id):
    if request.method == "PUT":

        data = json.loads(request.body)

        user = User.objects.get(id=id)

        user.name = data["name"]
        user.mobile = data["mobile"]

        user.save()

        return JsonResponse({
            "message": "User updated successfully",
            "id": user.id,
            "name": user.name,
            "mobile": user.mobile
        })

    return JsonResponse({
        "message": "Only PUT method is allowed"
    }, status=405)


@csrf_exempt
def delete_user(request,id):
    if(request.method =='DELETE'):
        user = User.objects.get(id=id)
        deleted_user = {
            "id": user.id,
            "name": user.name,
            "mobile": user.mobile
        }
        user.delete()
    
        return JsonResponse({
            "message":"User deleted successfully",
            "user":deleted_user
        })
    return JsonResponse({
    "message":"Only DELETE method is allowed"
},status = 405)