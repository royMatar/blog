from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog.api.views import UserDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
    path("jwt/", TokenObtainPairView.as_view(), name="jwt_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)