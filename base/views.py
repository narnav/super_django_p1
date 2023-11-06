
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Task,Product,Category,Order,OrderDetails

#start Serializers section
# login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom columns (user return payload - when login )
        token['username'] = user.username
        token['emaillll'] = user.email
        token['blabla'] = "waga baga bbb"
        # ...
        return token

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
    def create(self, validated_data):
        user = self.context['user']
        print(user)
        return Order.objects.create(**validated_data,user=user)


class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'

#end Serializers section

@permission_classes([IsAuthenticated])
class OrderView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            order = serializer.save()
            
            # Create OrderDetails objects for each item in the list
            for item in request.data["items"]:
                print(item)
                item['order'] = order.id  # Assuming there's a foreign key to Order in OrderDetails
                serializerDt = OrderDetailsSerializer(data=item)
                if serializerDt.is_valid():
                    serializerDt.save()
                else:
                    return Response(serializerDt.errors, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        my_model = request.user.order_set.all()
        serializer = OrderSerializer(my_model, many=True)
        return Response(serializer.data)


    
   
   







class OrderDetailsViewSet(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer
    permission_classes = [IsAuthenticated]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


@api_view(["get"])
def index(req):
    return Response ( TaskSerializer(Task.objects.all(),many=True).data)


@api_view(["get","POST"])
@permission_classes([IsAuthenticated])
def member_only(req):
    print( req.user)
    return Response ( {"secret":"bla bla"})


@api_view(["post"])
def register(req):
    print( req.data)
    User.objects.create_user(username=req.data["username"],password=req.data["password"])
    return Response ( {"user":"created"})





class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# @permission_classes([IsAuthenticated])
class Product_view(APIView):
    def get(self, request):
        my_model = Product.objects.all()
        serializer = ProductSerializer(my_model, many=True)
        return Response(serializer.data)
    def post(self, request):
        # usr =request.user
        # print(usr)
        serializer = ProductSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        serializer = ProductSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# @permission_classes([IsAuthenticated])
class Category_view(APIView):
    def get(self, request):
        my_model = Category.objects.all()
        serializer = CategorySerializer(my_model, many=True)
        return Response(serializer.data)
    def post(self, request):
        # usr =request.user
        # print(usr)
        serializer = CategorySerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, pk):
        my_model = Category.objects.get(pk=pk)
        serializer = CategorySerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk):
        my_model = Category.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


