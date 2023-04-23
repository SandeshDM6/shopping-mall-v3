from django.urls import path
from shoppingapp import views

app_name = "shoppingapp"


urlpatterns = [

    path('', views.home_view, name='home'),
    path('shops/', views.shop_list_View, name='store-list'),
    path('shop/create/', views.create_shop_View, name='create-shop'),
    path('shop/<int:id>/', views.single_shop_view, name='single-shop'),
    path('result/', views.search_result_view, name='search_result'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/employer/shop/edit/<int:id>', views.shop_edit_view, name='edit-job'),
    path('dashboard/employer/close/<int:id>/', views.make_complete_shop_view, name='complete'),
    path('dashboard/employer/delete/<int:id>/', views.delete_shop_view, name='delete'),


]
