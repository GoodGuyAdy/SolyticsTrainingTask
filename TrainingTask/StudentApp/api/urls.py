from StudentApp.api.views import StudentsList, StudentDetails
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("list/", StudentsList.as_view(), name="studentlist"),
    path("<int:pk>/", StudentDetails.as_view(), name="studentdetails"),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
