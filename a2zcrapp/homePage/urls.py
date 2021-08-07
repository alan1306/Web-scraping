from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home),
    path('products',views.product,name="products"),
    path('search',views.search,name="search-products")
]