from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog.api.views import UserDetail


urlpatterns = [
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)