
from django.contrib import admin
from django.urls import path, include
import blog.views
import debug_toolbar
from django.conf import settings
urlpatterns = [
    # recommended to change the url name of admin to something else for enhanced security
    path('admin/', admin.site.urls),
    path("", blog.views.index),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),
    
]
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]