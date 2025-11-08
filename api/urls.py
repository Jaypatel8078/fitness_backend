from django.urls import path
from .views import RegisterView, ActivityListCreateView, ActivityDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('activities/', ActivityListCreateView.as_view(), name='activities'),
    path('activities/<int:pk>/', ActivityDetailView.as_view(), name='activity_detail'),
]
