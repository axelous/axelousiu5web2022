from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from baumstagram import views as baumstagram_views

router = routers.DefaultRouter()
router.register(r'accounts', baumstagram_views.AccountViewSet)
router.register(r'photos', baumstagram_views.PhotoViewSet)
router.register(r'users', baumstagram_views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
]
