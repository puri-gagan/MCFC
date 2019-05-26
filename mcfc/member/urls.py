from django.urls import path
from .import views
urlpatterns = [
    path('member',views.MemberView.as_view(),name = 'member'),
]
