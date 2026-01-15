from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, convert_currency
from django.urls import path

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet)

urlpatterns = router.urls + [
    path('convert/', convert_currency),
]