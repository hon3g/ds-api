from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import generics, exceptions


class CreatePlayer(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class GetUpdatePlayer(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'player_id'


class ListPlayers(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        sortby = self.request.query_params.get('sortby')
        size = self.request.query_params.get('size')

        if sortby not in {'xp', 'gold'} \
            or not size or not size.isnumeric():
            raise ListError
        
        queryset = Profile.objects.order_by('-' + sortby)[:int(size)]
        return queryset


class ListError(exceptions.APIException):
    status_code = 400
    default_detail = \
    "Both sortby=<xp|gold> and size=<int> are required parameters."