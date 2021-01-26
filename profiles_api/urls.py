from django.urls import path, include
from rest_framework.routers import DefaultRouter # für ViewSets
from profiles_api import views

# ViewSets
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')


urlpatterns = [
    path('hello-view', views.HelloAPIView.as_view()), # APIView
    path('', include(router.urls)) # ViewSet - include all urls without a prefix =''
]
