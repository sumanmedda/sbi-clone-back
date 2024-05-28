from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserDataSerializer, UserInfoSerializer
from .models import UserData, UserInfo
from rest_framework.response import Response

# Create your views here.
class UserDataView(APIView):
    def post(self,request):
        data = request.data
        user_data = UserDataSerializer(data=data)

        try:
            if user_data.is_valid():
                user_data.save()
            return Response({"status":201,"message": "User Data Stored"},)
        except Exception as e:
            return Response({"status":400, "message": "Some Issue", "error":e},)
    

    def get(self,request):
        data = UserData.objects.all()
        serializer = UserDataSerializer(data, many=True)
        return Response({"message":"Data Fetched", "user_data": serializer.data})


class UserInfoView(APIView):
    def post(self,request):
        data = request.data
        user_data = UserInfoSerializer(data=data)

        try:
            if user_data.is_valid():
                user_data.save()
            return Response({"status":201,"message": "User Info Stored"},)
        except Exception as e:
            return Response({"status":400, "message": "Some Issue", "error":e},)
    

    def get(self,request):
        data = UserInfo.objects.all()
        serializer = UserInfoSerializer(data, many=True)
        return Response({"message":"Data Fetched", "user_info": serializer.data})
        