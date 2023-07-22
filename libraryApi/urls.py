from django.contrib import admin
from django.urls import path,include
from book import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
   
    path('admin/', admin.site.urls),
    #path('bkinfo/<int:pk>',csrf_exempt(views.book_detail)),
    #path('bkinfo/',csrf_exempt(views.book_list)),
    #path('bkcreate/',views.book_create),
    #path('bkapi/',views.book_api),
    #path('register/',views.register)    
    path('api/user/', include('book.urls'))
]

