from django.conf.urls import url
from django.urls import reverse
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  
    url(r'^$', views.dashboard),
    #add new url button view, first time adding 
    url(r'^addurl/(?P<table_id>[\w\-]+)/$', views.addurl ,name="addurl" ),
    #add new header button view, first time adding
    url(r'^addheader/(?P<header_id>[\w\-]+)/$', views.addheader ,name="addheader" ),

    # edit the header form (edit option)
    url(r'^editheaders/(?P<pk>\d+)/$',views.edittitle, name="editheaders"),
    # edit the header form after the editheader kicks in (Save) new changes
    url(r'^edittitle/(?P<pk>\d+)/$',views.edit_title, name="editingtitle"),

    url(r'^login/$', views.login ,name="login" ),
    
    url(r'^logout/$', views.logout, name="logout" ),

    url(r'^register/$', views.register, name="register" ),

    url(r'^profile/$', views.profile, name="profile" ),

    url(r'^profile/edit/$', views.edit_profile, name="edit_profile" ),

    url(r'^change-password/$', views.change_password,  name="change_password"),

    #transfer the url form (edit or delete)
    url(r'^transferlink/$', views.transferlink ,name="transferlink" ),

    #edit the url form (edit or delete)
    url(r'^editurl/(?P<pk>\d+)/$', views.editurl ,name="editurl" ),

    #the actual edit form after the edit url kicks in (save) new changes
    url(r'^editlinks/(?P<pk>\d+)/$',views.edit_url, name="editinglinks"),

    #the actual delete form after the edit url kicks in (delete) new changes
    url(r'^deletelinks/(?P<pk>\d+)/$',views.delete_url, name="deletelinks")

    
    
   
    

]
