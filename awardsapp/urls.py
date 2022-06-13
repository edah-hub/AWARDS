from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='registrations'),
    path('signin/',views.signin,name='login'),
    path('new_post/',views.addpost,name='addpost')
]




if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)