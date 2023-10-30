
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


@api_view(["get"])
def index(req):
    return Response ( TaskSerializer(Task.objects.all(),many=True).data)


@api_view(["get"])
@permission_classes([IsAuthenticated])
def member_only(req):
    print( req.user)
    return Response ( {"secret":"bla bla"})


@api_view(["post"])
def register(req):
    print( req.data)
    User.objects.create_user(username=req.data["username"],password=req.data["password"])
    return Response ( {"user":"created"})
