from django.contrib import admin
from .models import Article ,Category

#admin header change 
admin.site.site_header = " وبلاگ "


# Register your models here.

admin.site.disable_action('delete_selected')# غیر فعال کردن اکشن پیش فرض حذف کردن 

def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
    	message_bit = "منتشر شد ."
    else:
    	message_bit= "منتشر شدند ."
    modeladmin.message_user(request, "{}مقاله {}".format(rows_updated,message_bit))
       
make_published.short_description = "انتشار مقالات انتخاب شده "

def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
    	message_bit = " پیشنویس شد ."
    else:
    	message_bit= "پیش نویس شدند ."
    modeladmin.message_user(request, "{}مقاله {}".format(rows_updated,message_bit))
make_draft.short_description = " پیش نویس مقالات انتخاب شده "

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('position','title','slug','parent', 'status')
	#ezafe kardan in etelat be bakhshe Article 
	list_filter = ( ['status'])
	#sakhte filter dar safhe admin
	search_fields=( 'title' , 'slug')
	prepopulated_fields={'slug':('title',)}# neveshtan hamzaman slug ba title
	#- baraye nozoli namayesh dadan
admin.site.register(Category,CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','thumbnail_tag','slug','author','jpublish', 'status' , 'Category_to_str')
	#ezafe kardan in etelat be bakhshe Article 
	list_filter = ('publish', 'status', 'author')
	#sakhte filter dar safhe admin
	search_fields=( 'title' , 'description')
	prepopulated_fields={'slug':('title',)}# neveshtan hamzaman slug ba title
	ordering =[ 'status', '-publish'] 
	#- baraye nozoli namayesh dadan
	actions = [make_published,make_draft]
	def Category_to_str(self , obj):
		return "، ".join([category.title for category in obj.category.active()]) #baraye namayesh category 

	Category_to_str.short_description = "دسته بندی"
admin.site.register(Article,ArticleAdmin)