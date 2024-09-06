from api.models.userModel import User
from rest_framework.response import Response
from api.serializers.userSerializers import userSignupserializer,SenderUserSerializer,FriendsSerializer,requestSerializer
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q
from api.customPagination import CustomPagination
from api.models.friendRequestModel import FriendRequestModel
from api.models.userFriendsModel import FriendsModel
from rest_framework.exceptions import Throttled


class UserService():
    def signup(self, request):
        """signup api """
        try:
            email = User.objects.filter(Q(email=request.data["email"])| Q(username = request.data["username"]))
            if email:
                return {"data":None,"messages":"email/username already exists","status":400}
        
            serializer = userSignupserializer(data = request.data)

            if serializer.is_valid():
                user = serializer.save()  
                user.set_password(request.data["password"])  
                user.save() 
                return {"data":serializer.data,"message":"signup successfully","status":201}
        except Exception as e:
            return {"data":None,"message":"something went wrong","status":400}


    def login(self, request):
        """Login api """
        try:
            if "email" in request.data:
                user = User.objects.get(Q(email=request.data["email"])| Q(username=request.data["email"]))
                check_psd = check_password(request.data["password"],user.password)
                if check_psd:
                    serializer = userSignupserializer(user)
                    data = serializer.data
                    token = RefreshToken.for_user(user)
                    data["access_token"]= str(token.access_token)

                    return {"data":data,"message":"ok","status":200}

        except Exception as e:
            return {"data":None,"message":"something went wrong","status":400}

    def search_user(self, request):
        """search the user which are in the app """
        try:
            banner_obj = User.objects.all()
            pagination_obj = CustomPagination()
            search_keys = ["fullname__icontains","email__icontains"]
            result = pagination_obj.custom_pagination(request, search_keys, userSignupserializer, banner_obj)
            return {"data":result,"message":"FETCH","status":200}
        except Exception as e:
            return {"data":None,"message":"Something went wrong","status":400}

    
    def send_request(self, request):
        ''' sending the request to tu user so that they both will be friends'''
        try:
            receiver_user = User.objects.get(id = request.data.get("receiver_user_id"))
        except User.DoesNotExist:
            return {"data":None,"message":"User does not exist","status":400}
        try:
            sender_user = User.objects.get(id = request.user.id)
            is_already_friends = FriendsModel.objects.filter(
            user_id=sender_user.id, friend_id=receiver_user.id
            ).exists()  # Use .exists() to check without raising an exception

            if is_already_friends:
                return {"data": None, "message": "Already Friends", "status": 200}
            request = FriendRequestModel.objects.create(
                sender_id=sender_user.id,
                receiver_id = receiver_user.id,
                status = 1,
            )
            request.save()
            serializer = SenderUserSerializer(sender_user)
            return {"data":serializer.data,"message":"ok","status":200}
        except Throttled as e:
            print(str(e),"000000000000000000000000000000000")
            return {"data":None,"message":"you can not send more then 3 request in a minute","status":429} 
        except Exception as e:
            return {"data":None,"message":str(e),"status":400}

    def Get_all_user_request(self, request):
        '''get all Request to a particular User'''
        try:
            receiver = FriendRequestModel.objects.filter(receiver_id= request.user.id, status = 1)
            serializer = requestSerializer(receiver, many=True)
            return {"data":serializer.data,"message":"fetch","status":200}
        except Exception as e:
            return {"data":None,"message":str(e),"status":400}



    def Request_accept(self, request,id):
        '''accepting the request from the receiver side.'''
        try:
            received_requests = FriendRequestModel.objects.get(id = id)
            received_requests.status = 2
            received_requests.save()
            friends = FriendsModel.objects.create(
                user = received_requests.sender,
                friend = received_requests.receiver
            )
            friends.save()
            friends = FriendsModel.objects.create(
                user = received_requests.receiver,
                friend = received_requests.sender
            )
            friends.save()
            return {"data":None,"message":"Request is accepted","status":200}
        except Exception as e:
            return {"data":None,"message":str(e),"status":400}
    
    def Request_reject(self, request , id):
        '''Reject the friend request'''
        try:
            received_requests = FriendRequestModel.objects.get(id = id)
            received_requests.status = 3
            received_requests.save()
            return {"data":None, "message":"Request is Rejected", "status":200}
        except Exception as e:
            return {"data":None, "message":str(e),"status":400}

    def all_friends_list(self, request):
        '''list of all friends. '''
        try:
            user_friends =FriendsModel.objects.filter(user_id=request.user.id)
            serializer = FriendsSerializer(user_friends, many = True)
            return {"data":serializer.data,"message":"Fetch","status":200}
        except Exception as e:
            return {"data":None,"message":str(e),"status":400}

        
    










