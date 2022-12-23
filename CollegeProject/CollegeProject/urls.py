from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('api.urls'))
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

router = DefaultRouter()
router.register('college', UserViewSet, basename='users')
urlpatterns += router.urls