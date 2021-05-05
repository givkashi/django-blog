from django.urls import path
from .views import ArticleList,api,detail , category ,AuthorList

app_name = "blog"
urlpatterns = [
	path('',ArticleList.as_view(),name="home"),
	path('page/<int:page>',ArticleList.as_view(),name="home"),
	path('api',api,name="api"),
	path('article/<slug:slug>', detail, name="detail"),
	path('category/<slug:slug>', category, name="category"),
	path('category/<slug:slug>/page/<int:page>', category, name="category"),
	path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name="author"),
	path('author/<slug:username>',  AuthorList.as_view(), name="author"),


]
