from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='registrations'),
    path('signin/',views.signin,name='login'),
    path('new_post/',views.addpost,name='addpost'),
    path('logout/',views.logout,name='logout'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    
        # url(r'^search/', views.search_users, name='search_users'),
    path(r'^search/', views.search_projects, name='search_projects'),
    path(r'^image(\d+)', views.project, name='project'),
    path(r'^users/', views.user_list, name='user_list'),
    path(r'^new/image$', views.new_image, name='new_image'),
    path(r'^new/project$', views.new_project, name='new_project'),
    path(r'^edit/profile$', views.edit_profile, name='edit_profile'),
    path(r'^profile/(?P<username>[0-9]+)$',
        views.individual_profile_page, name='individual_profile_page'),
    path(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    path(r'^api/project/$', views.ProjectList.as_view()),
    path(r'api/project/project-id/(?P<pk>[0-9]+)/$',
        views.ProjectDescription.as_view()),
    path(r'^api/profile/$', views.ProfileList.as_view()),
    path(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',
        views.ProfileDescription.as_view()),
    # ex: /
    path(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    path(r'^review/(?P<review_id>[0-9]+)/$',
        views.review_detail, name='review_detail'),
    # ex: /project/
    path(r'^project$', views.project_list, name='project_list'),
]




if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)