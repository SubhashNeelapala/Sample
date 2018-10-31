from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns =[
url(r'^$',views.user_login,name='user_login'),
url(r'^user_registration',views.home,name='home'),
url(r'^responce_data',views.responce_data,name='response'),
url(r'^user_edit/(?P<id>\d+)$', views.home, name='user_edit'),
url(r'csv_download',views.report_download,name='report_download'),
]