
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     
    path('sinup',views.login,name='signup'),
    path('login',views.login,name='login'),

    path('home',views.home,name='home'),
    path('fixed',views.fixednav,name='fixednav'),

    path('',views.index,name='index'),
    path('insert',views.insert,name='index'),

    path('',views.page2,name='page2'),
    path('insert1',views.insert1,name='page2'),

    
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)