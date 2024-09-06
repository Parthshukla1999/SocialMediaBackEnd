from sys import api_version
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from api.models.userModel import User
from rest_framework.response import Response
from api.serializers.userSerializers import userSignupserializer
from api.services.userOnboardingServices import UserService
from rest_framework import status
from rest_framework.throttling import UserRateThrottle
from api.customThrottling import CustomThrottle
userser = UserService()


class Signup(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        result = userser.signup(request)
        return Response(result,status=result["status"])

  
class Login(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        result = userser.login(request)
        return Response(result,status=result["status"])


class SearchUser(APIView):
    def post(self, request):
        result = userser.search_user(request)
        return Response(result, status=result["status"])

class SendRequest(APIView):
    throttle_classes = [UserRateThrottle]
    def post(self, request):
        result = userser.send_request(request)
        return Response(result, status=result["status"])

class GetAllRequest(APIView):
    def post(self, request):
        result = userser.Get_all_user_request(request)
        return Response(result, status=result["status"])


class AcceptRequest(APIView):
    def post(self, request, id):
        result = userser.Request_accept(request, id)
        return Response(result, status=result["status"])

class RejectRequest(APIView):
    def post(self, request, id):
        result = userser.Request_reject(request, id)
        return Response(result, status=result["status"])

class FriendListing(APIView):
    def post(self, request):
        result = userser.all_friends_list(request)
        return Response(result, status=result["status"])


