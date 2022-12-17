from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

@api_view(['GET','POST'])
def user_api_view(request):

    if request.method == 'GET':   # esto es para obtener 
        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True)
        return Response(users_serializer.data)

    elif request.method == 'POST': # esto es para crear
        user_serializer = UserSerializer(data = request.data) # .data trae los datos 
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)

@api_view(['GET','PUT']) # esto obtiene una consulta desde una primary key y actualiza el campo con json
def user_detail_api_view(request,pk=None):

    if request.method == 'GET': # hace la peticion de un usuario desde un parametro primary key
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)
    
    elif request.method == 'PUT': # put para actualizar los campos
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user, data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)
        
            
        





# class UserAPIView(APIView):

#     def get(self,request):
#         users = User.objects.all()
#         users_serializer = UserSerializer(users, many = True)
#         return Response(users_serializer.data)


