from rest_framework.views import APIView
from rest_framework.response import Response
# für Serializer (serializers.py)
from rest_framework import status # list of HTTP Status Codes
from profiles_api import serializers
from profiles_api import models # import der models für Profiles Project (Chap 10)
# für ViewSets
from rest_framework import viewsets

# permissions
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions


class HelloAPIView(APIView):
    """Test API View"""
    # configure the defined serializers - name immer max_length=10
    serializer_class = serializers.HelloSerializer

    # self wegen class, request kommt vom rest_framework und BestPractise
    # dass das format=None gesetzt ist, falls mal format für die Endpoints
    # aktiviert wird, ist es bereits unterstützt
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        # is an example for demo
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your app logic'
            'is mapped manually to URLs'
        ]

        # return a Response Object is expected
        # due to JSON output it has to be a list or dict - here a dict
        return Response({'message':'Hello!', 'an_apiview': an_apiview})

    # dafür den serializer
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            # return serializer.error is good practise dev knows what's wrong
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # pk is primary key for url - put updates an entire object; diff from patch!
    # insert an entire data row - if just updating the lastname the other infos
    # will be "deleted"
    def put(self, request, pk=None):
        """Handle updating on object"""
        return Response({'method': 'PUT'})

    # patch updates for e.g. only the last_name and leave pre_name as it is
    def patch(self,request, pk=None):
        """Handle a partial update on object"""
        return Response({'method': 'PATCH'})

    def delete(self,request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test APi ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new Hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    #PK because defined Object
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})


# Profile Projet Chap 10
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    # query with objects to take effect
    # Framework ModelViewSet takes care of list, etc...
    queryset = models.UserProfile.objects.all()
    # don't miss the comma to recieve a tuple not a single item
    authentication_classes = (TokenAuthentication,)
    # look up the permission logic for every call
    # and again DON'T miss the comma!!
    permission_classes = (permissions.UpdateOwnProfile,)
