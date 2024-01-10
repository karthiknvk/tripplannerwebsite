from django.urls import path,include
from . import views
#from packages.views import prefer
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  path('addreview',views.addreview,name='addreview'),
  path('addspot',views.addspot,name='addspot'),
  path('showreview',views.showreview,name='showreview'),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)