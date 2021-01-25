from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""

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
