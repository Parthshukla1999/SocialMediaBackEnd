from rest_framework import serializers
from api.models.userModel import User
from api.models.userFriendsModel import FriendsModel
from api.models.friendRequestModel import FriendRequestModel

class userSignupserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","fullname","username","age","phone_number","email","is_active","is_deleted"]


class SenderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","fullname"]

class requestSerializer(serializers.ModelSerializer):
    sender = SenderUserSerializer()  # This will work for reading the sender data (serialization)
    # sender = serializers.SerializerMethodField()
    class Meta:
        model = FriendRequestModel
        fields = ["id", "sender"]

    


class FriendsSerializer(serializers.ModelSerializer):
    friend = SenderUserSerializer() 
    class Meta:
        model = FriendsModel
        fields = ["id", "friend"]