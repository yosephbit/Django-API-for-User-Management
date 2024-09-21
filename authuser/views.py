from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .decorators import role_required
from .serializer import UserSerializer

# Create your views here.
@login_required
@api_view(['GET'])
def profile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response({'user': serializer.data}, status=status.HTTP_200_OK)

@login_required
@role_required('admin')
@api_view(['GET'])
def user_lists(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    print(users)
    return Response({'users': serializer.data}, status=status.HTTP_200_OK)

@login_required
@role_required('admin', return_template=True)
@api_view(['GET'])
def user_lists_template(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users/users-list.html', context)