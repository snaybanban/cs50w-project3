from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
	path('', views.index, name='index'),
	path('profile/', views.profile, name='profile'),
	path('profile/<str:username>/', views.profile, name='profile'),
	path('register/', views.register, name='register'),
	path('login/', LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
	path('post/', views.post, name='post'),
	path('add_item', views.addItem_view, name='add_item'),
    path('remove_item/<int:cart_item_id>', views.removeItem_view, name='remove_item'),
    path('empty_cart', views.emptyCart_view, name='empty_cart'),
    path('cart', views.cart_view, name='cart'),
    path('order', views.order_view, name='order'),
	path('comparar/', views.comparar, name='comparar'),
	path('horas/', views.horas, name='horas'),
	path('contacto/', views.contacto, name='contacto'),
    path('orders', views.orders_view, name='orders'),
    path('vieworders', views.viewOrders_view, name='vieworders'),
    path('markComplete/<int:order_item_id>', views.markComplete_view, name='markcomplete'),
	
]