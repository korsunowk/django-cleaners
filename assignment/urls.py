from django.conf.urls import include, url
from django.contrib import admin
from main import views as main_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'assignment.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^cleaners/', include('cleaners.urls', namespace='cleaners')),
    url(r'^customers/', include('customers.urls', namespace='customers')),
    url(r'^towns/', include('towns.urls', namespace='towns')),
    url(r'^bookings/', include('bookings.urls', namespace='bookings')),
    url(r'^$', main_views.home)
]
