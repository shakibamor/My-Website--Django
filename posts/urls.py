from django.conf.urls import url
from . import views
from django.urls import path, include

# urlpatterns = [
#     url('', views.index, name='index'),
#     url('details/(?P<id>\d+)/$', views.details, name='details')
# ]
urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>', views.details, name='details')
]