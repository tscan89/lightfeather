from django.urls import path

from .views import CipherView

urlpatterns = [
    path('api/encode', CipherView.as_view())
]
