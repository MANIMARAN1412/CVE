from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/cves', views.CVEViewSet)

urlpatterns = [
    path('', views.cve_list, name='cve_list'),
    path('cve/create/', views.cve_create, name='cve_create'),
    path('cve/<int:pk>/update/', views.cve_update, name='cve_update'),
    path('cve/<int:pk>/delete/', views.cve_delete, name='cve_delete'),
    path('cve/<int:pk>/view/', views.cve_detail, name='cve_detail'),
    path('', include(router.urls)),
]



