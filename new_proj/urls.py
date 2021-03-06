from django.conf.urls import patterns, include, url
from django.contrib import admin
from rango import views

urlpatterns = patterns('',
 url(r'^$', views.index, name='index'),
 url(r'^admin/', include(admin.site.urls)),
 url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
 url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category')  # New!
)
 
