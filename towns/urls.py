from django.conf.urls import url

from .views import (
    TownList,
    TownDetail,
    TownCreation,
    TownUpdate,
    TownDelete
)

urlpatterns = [

    url(r'^$', TownList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', TownDetail.as_view(), name='detail'),
    url(r'^new/$', TownCreation.as_view(), name='new'),
    url(r'^edit/(?P<pk>\d+)/$', TownUpdate.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', TownDelete.as_view(), name='delete'),
]
