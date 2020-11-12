from django.conf import settings
from django.conf.urls import url

from django.conf.urls.static import static
from . import views
from django.urls import path

from . import views

urlpatterns=[
    # url('^$',views.home,name = 'home'),
    url(r'^post$', views.post, name='post'),
    # url(r'^article/(\d+)',views.article,name ='article'),
    url(r'',views.news_update,name='newsUpdate'),
    path('<str:room_name>/', views.room, name='room'),
    
    ]
    

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
