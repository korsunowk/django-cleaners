from django.conf.urls import url

from .views import BookingCreation

urlpatterns = [
    url(r'^$', BookingCreation.as_view(), name='new'),
]
