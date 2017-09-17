from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
	url(r'^article/(\d+)/', views.viewArticle, name = 'article'),
	#url(r'^articles/(\d+)/(\d+)', 'viewArticles', name = 'articles'),
	#url(r'^page-redirect/', 'page_redirect', name = 'page_redirect'),
]
