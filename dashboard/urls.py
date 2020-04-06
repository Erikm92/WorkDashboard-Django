from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  
    url(r'^$', views.dashboard),

    url(r'^addurl/(?P<table_id>[\w\-]+)/$', views.addurl ,name="addurl" ),
    # need to hide header_id
    url(r'^editheaders/(?P<header_id>[\w\-]+)/$',views.edittitle, name="editheaders"),

    #url(r'^edittitle/(?P<header_id>[\w\-]+)/$', views.edittitle ,name="edittitle" ),

    #url(r'^edittitleform/$', views.new_title, name="edittitles"),

    url(r'^edittitle/(?P<pk>\d+)/$',views.edit_title, name="editingtitle"),

    url(r'^login/$', views.login ,name="login" ),
    
    url(r'^logout/$', views.logout, name="logout" ),

    url(r'^register/$', views.register, name="register" ),

    url(r'^profile/$', views.profile, name="profile" ),

    url(r'^profile/edit/$', views.edit_profile, name="edit_profile" ),

    url(r'^change-password/$', views.change_password,  name="change_password"),

    #this is all views for editing urls
    #need to figure out what to do with table_id
    url(r'^editurl/(?P<table_id>[\w\-]+)/$', views.editurl ,name="editurl" ),

    url(r'^editlink/$', views.new_post, name="editlink"),

    url(r'^editlinks/(?P<pk>\d+)/$',views.edit_url, name="editinglinks"),

    url(r'^deletelinks/(?P<pk>\d+)/$',views.delete_url, name="deletelinks")

    
    
   
    

]
