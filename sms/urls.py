from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^inventory_management/', views.inventory_management, name='inventory_management'),
    url(r'^sales_management/sales_analysis', views.sales_analysis, name='sales_analysis'),
    url(r'^calendar/', views.calendar, name='calendar')
]