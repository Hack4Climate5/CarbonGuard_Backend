from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User
from .serializer import UserSerializer
from rest_framework import generics


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            email = serializer.validated_data.get('email')
            # Checking if email or username already exists in the database
            if User.objects.filter(username=username).exists():
                error_message = 'This username is already taken. Please choose another username.'
                return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(email=email).exists():
                error_message = 'This email address is already in use. Please use a different email.'
                return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
            password = serializer.validated_data.get('password')
            phone_number = serializer.validated_data.get('phone_number')
            user = User.objects.create_user(username=username, email=email, password=password, phone_number=phone_number)
            user.save()
            return Response('Your account has been created successfully', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response('User deleted successfully', status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response('Please input correct login',
                            status=status.HTTP_401_UNAUTHORIZED)
        if user.check_password(password):
            return Response('Successfully logged in.',
                            status=status.HTTP_200_OK)
        else:
            return Response('Please input correct login details',
                            status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def logout_view(request):
    if 'user_id' in request.session:
        request.session.clear()
        return Response({'message': "You have been logged out successfully."})
    else:
        return Response({'message': "You were not logged in."})
