from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IndustryViewSet, CompanyViewSet, PersonViewSet

router = DefaultRouter()
router.register('industries', IndustryViewSet)
router.register('companies', CompanyViewSet)
router.register('persons', PersonViewSet)

urlpatterns = [
    path('', include(router.urls), name='api_urls'),
]
