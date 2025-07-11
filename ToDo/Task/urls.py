from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'Task', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),

]
