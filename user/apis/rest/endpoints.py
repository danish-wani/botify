from django.urls import path

from user.apis.rest.api import BotifyUserListCreate, BotifyUserRetrieveUpdateDelete


urlpatterns = [
    path('users', BotifyUserListCreate.as_view(), name='v1_users_list_create'),
    path('users/<str:uid>', BotifyUserRetrieveUpdateDelete.as_view(), name='v1_users_retrieve_update_delete')
]
