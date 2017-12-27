from django.urls import path
from shop import views
urlpatterns=[

path('home',views.form,name='form'),
path('login',views.loginform,name='loginform'),
path('register',views.registerform ,name='registerform'),
path('productsfbv',views.product_list_view ,name='products'),
path('products',views.ProductListView.as_view() ,name='products'),
#path('detailsfbv/(?P<pk>\d+)',views.product_detail_view ,name='detailfbv'),
path('details/(?P<pk>\d+)',views.ProductDetailView.as_view() ,name='detail'),
]
