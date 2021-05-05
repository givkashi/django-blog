from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,JsonResponse,Http404
from .forms import ArticleForm
from .models import Article, Category
from django.contrib.auth.models import User 

# Create your views here.

	

#def home(request ,page=1):
#	articles_list = Article.objects.published()
	#paginator = Paginator(articles_list, 2)
#	articles=paginator.get_page(page)
	#contex ={
	#	#"articles": Article.objects.all()#brayae namayehse hame maghale ha

#		"articles": articles,
		# yani bar asas zaman publish be sorat nozoli  va [:3] yani setaye akhar
	#}
	#return render(request, "blog/home.html",contex)			

class ArticleList(ListView):
	#model = Article
	#template_name= "blog/list.html" # on template ke mikhahim meghdar be on bere 
	context_object_name = "articles" #agar bekhahim name ke be template ferestade shavad avaz konim 
	queryset = Article.objects.published()
	paginate_by = 2

		


class ArticleDetail(DetailView):
	def get_object(self):
		slug = self.kwargs.get('slug')
		return get_object_or_404(Article.objects.published(), slug=slug)


def detail(request, slug):

	#try:
	#	article=Article.objects.get(slug=slug)
	#except Exception as e:
	#	raise Http404
	#code bala baraye zamani ke az http 404 estefade mikonim vali ma az code payin estefade mikonim ke rahat tar hast 

	contex ={
		"article": get_object_or_404(Article.objects.published() , slug=slug )
		}
	return render(request, "blog/detail.html",contex)	

# def home(request):
	# #return HttpResponse(" Hello,world")
	# contex = {
		# "username":"mehran",
		# "age":22,
		# "job":"programmer"
	# }#inha be ghalebe ma essal mishan
	# return render(request, "blog/home.html",contex)
	


def category(request ,slug, page=1):
	category= get_object_or_404(Category , slug=slug ,status=True)
	articles_list=category.articles.published()
	paginator = Paginator(articles_list, 2)
	articles=paginator.get_page(page)
	contex ={
		"category":category,
		"articles":articles
		}
	return render(request, "blog/list.html",contex)
	

class AuthorList(ListView):
	#model = Article
	template_name= "blog/author_list.html" # on template ke mikhahim meghdar be on bere 
	context_object_name = "articles" #agar bekhahim name ke be template ferestade shavad avaz konim 
	queryset = Article.objects.published()
	paginate_by = 2

	def get_queryset(self):
		global author
		username=self.kwargs.get('username')
		author= get_object_or_404(User,username=username)
		return author.articles.published()
	
	def get_context_data(self, **kwargs):

		context= super().get_context_data(**kwargs)
		context['author']= author
		return context




def api(request):
	#return JsonResponse({"title": "slam"})
	data={
		"1":{"title":"ddd",
		"id":"20",
		"slug":"first"
		},
		"2":{
		"title":"ddd",
		"id":"20",
		"slug":"first"
		}
	}
	contex = {
		"articles": [
			{
				"title":"یروزی لیکرز در بازی اول فینال NBA",
				"description":"تیم لس‌آنجلس لیکرز در بازی نخست فینال لیگ بسکتبال NBA موفق به کسب پیروزی شد.",
				"img":"https://static.farakav.com/files/pictures/thumb/01529879.jpg"
			},
			{
				"title":"نصرآزادانی سرمربی تیم ملی تکواندو بلژیک شد",
				"description":"کاپیتان و مربی اسبق تیم ملی تکواندو کشورمان با درخواست فدراسیون تکواندو بلژیک به عنوان سرمربی، هدایت تکواندوکاران این کشور را برعهده گرفت.",
				"img":"https://static.farakav.com/files/pictures/thumb/00030600.jpg"
			}
		]
	}
	return JsonResponse(data)