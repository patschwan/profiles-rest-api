from django.urls import path, include
from rest_framework.routers import DefaultRouter # für ViewSets
from profiles_api import views

# ViewSets
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
# Profiles Projekt
# no base_name because we have the a queryset (just in case of overwrite)
router.register('profile', views.UserProfileViewSet)


urlpatterns = [
    path('hello-view', views.HelloAPIView.as_view()), # APIView
    path('login/', views.UserLoginApiView.as_view()), # enable Login Endpoint
    path('', include(router.urls)) # ViewSet - include all urls without a prefix =''
]
