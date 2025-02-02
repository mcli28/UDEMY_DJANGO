from django.contrib import admin
from django.urls import path, include
from core.views import CustomerViewSet, ProfessionsViewSet, DataSheetViewSet, DocumentViewSet
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet, basename="customer")
router.register(r'professions', ProfessionsViewSet)
router.register(r'data-sheets', DataSheetViewSet)
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
]
