from django.contrib import admin
from django.urls import path
from home import views



# django admin changes
admin.site.site_header = "Login to Faa"
admin.site.site_title = "Welocome to Dashboard"
admin.site.index_title = "Welocome to Portal"



urlpatterns = [
    path('', views.home, name='home'),
    path('project', views.project, name='project'),
    path('#contact', views.contact, name='contact'),
    # path('skills', views.skills, name='skills'),
    # path('contact', views.contact, name='contact'),
]
