from django.conf import settings
from django.conf.urls import url

from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^post$', views.post, name='post'),
    url(r'^$',views.news_today,name='newsToday'),
    
    
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)