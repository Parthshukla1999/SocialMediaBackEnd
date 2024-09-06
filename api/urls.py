from os import sendfile
from django.urls import path
from api.views.userOnboardingView import *
urlpatterns = [
    path('login',Login.as_view()),
    path('signup',Signup.as_view()),
    path('get-all-requests',GetAllRequest.as_view()),
    path('request-accept/<int:id>', AcceptRequest.as_view()),
    path('request-reject/<int:id>',RejectRequest.as_view()),
    path('friends-listings',FriendListing.as_view()),
    path('send-request',SendRequest.as_view()),
    path('search-users',SearchUser.as_view()),

]
