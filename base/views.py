
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


@api_view(["get"])
def index(req):
    return Response ( TaskSerializer(Task.objects.all(),many=True).data)

        # all_tasks=TaskSerializer(Task.objects.all(),many=True).data
        # return Response ( TaskSerializer(Task.objects.all(),many=True).data)
