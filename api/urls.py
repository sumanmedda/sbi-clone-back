from django.urls import path
from .views import UserDataView, UserInfoView

urlpatterns = [
    path('user-data/', UserDataView.as_view(), name='user-data'),
    path('getuser-data/', UserDataView.as_view(), name='user-data-fetch'),
    path('user-info/', UserInfoView.as_view(), name='user-info'),
    path('getuser-info/', UserInfoView.as_view(), name='user-info-fetch'),
]
