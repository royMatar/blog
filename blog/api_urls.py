from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from blog.api_views import post_list, post_detail
from rest_framework.authtoken import views
urlpatterns = [
    path("posts/", post_list, name="api_post_list"),
    path("posts/<int:pk>/", post_detail, name="api_post_detail"),
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)