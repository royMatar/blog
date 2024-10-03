from django.contrib import admin
from django.urls import path, include
import blog.views
import blog.api.views
import debug_toolbar
from django.conf import settings
from django_registration.backends.activation.views import RegistrationView
import blango_auth.views

from blango_auth.forms import BlangoRegistrationForm
from blog.api.views import TagViewSet, PostViewSet


from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static

router = DefaultRouter()
router.register("tags", TagViewSet)
router.register("posts", PostViewSet)

urlpatterns = [
    # recommended to change the url name of admin to something else for enhanced security
    path('profile/', blog.views.index),
    # path(
    #     "accounts/register/",
    #     RegistrationView.as_view(form_class=BlangoRegistrationForm),
    #     name="django_registration_register",
    # ),
    # path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", blango_auth.views.profile, name="profile"),
    # path("accounts/", include("django_registration.backends.activation.urls")),
    # path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("allauth.urls")),
    path("login/", blango_auth.views.login, name="login"),
    path('admin/', admin.site.urls),
    path("", blog.views.index),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),
    path("api/v1/", include("blog.api.urls")),
    path("", include(router.urls)),
    
]
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)