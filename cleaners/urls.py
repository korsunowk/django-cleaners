from django.conf.urls import url

from .views import (
    CleanerList,
    CleanerDetail,
    CleanerCreation,
    CleanerUpdate,
    CleanerDelete
)

urlpatterns = [

    url(r'^$', CleanerList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', CleanerDetail.as_view(), name='detail'),
    url(r'^new$', CleanerCreation.as_view(), name='new'),
    url(r'^edit/(?P<pk>\d+)$', CleanerUpdate.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)$', CleanerDelete.as_view(), name='delete'),

]