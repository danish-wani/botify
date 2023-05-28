from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import SessionAuthentication

from user.apis.rest.serializers import BotifyUserSerializer
from user.models import BotifyUser


class BotifyUserListCreate(ListCreateAPIView):
    serializer_class = BotifyUserSerializer
    authentication_classes = [SessionAuthentication]
    queryset = BotifyUser.objects.all()


class BotifyUserRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = BotifyUserSerializer
    authentication_classes = [SessionAuthentication]
    lookup_field = 'uid'
    lookup_url_kwarg = 'uid'

    def get_object(self):
        """
            Returns the BotifyUser object
        :return:
        """
        return BotifyUser.objects.get(id=self.kwargs['uid'])
