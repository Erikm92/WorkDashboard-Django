from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  
    url(r'^$', views.dashboard),

    url(r'^addurl/$', views.addurl ,name="addurl" ),

    url(r'^editurl/$', views.editurl ,name="editurl" ),

    url(r'^login/$', views.login ,name="login" ),
    
    url(r'^logout/$', views.logout, name="logout" ),

    url(r'^register/$', views.register, name="register" ),

    url(r'^profile/$', views.profile, name="profile" ),

    url(r'^profile/edit/$', views.edit_profile, name="edit_profile" ),

    url(r'^change-password/$', views.change_password,  name="change_password")

  

    
   
    

]
