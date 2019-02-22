from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag
from recipe import serializers

#the viewset is a way to use
class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Mange tags in the database"""
    #this means that it's required that token authentication is UserAdmin
    #an that the user is authenticated to use the api
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    #overrides the already built in method
    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
