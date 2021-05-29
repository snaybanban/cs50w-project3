from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import *
from .forms import UserRegisterForm, PostForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
	context = {
        'item_cats': Item_Category.objects.all(),
        'items': Item.objects.all(),
        'toppings': Topping.objects.all(),
        'posts': Post.objects.all()
    }
	return render(request, 'index.html', context)

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('index')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'register.html', context)

@login_required
def post(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Post enviado')
			return redirect('index')
	else:
		form = PostForm()
	return render(request, 'post.html', {'form' : form })



def profile(request, username=None):
	current_user = request.user
	if username and username != current_user.username:
		user = User.objects.get(username=username)
		posts = user.posts.all()
	else:
		posts = current_user.posts.all()
		user = current_user
	return render(request, 'profile.html', {'user':user, 'posts':posts})


def follow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	messages.success(request, f'sigues a {username}')
	return redirect('index')

def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
	rel.delete()
	messages.success(request, f'Ya no sigues a {username}')
	return redirect('index')

def addItem_view(request):
    
    if request.method == 'POST':
        try:
            item_id = request.POST['item-id']
        except:
            item_id = None
        try:
            max_topping = request.POST['max-topping']
        except:
            max_topping = None
        try:
            size = request.POST['size-select']
        except:
            size = None
        
        toppings = []
        if max_topping:
            for i in max_topping:
                try:
                    top = request.POST[f'select-{i}']
                    toppings.append(Topping.objects.get(pk=top))
                except:
                    pass

        item = Item.objects.get(pk=item_id)
        if size == 'S':
            price = item.price_small
        elif size == 'L':
            price = item.price_large

        cart = Cart.objects.get(user=request.user)
        cart_item = Cart_Item(cart=cart, item_detail=item, size=size, price=price)
        cart_item.save()
        if len(toppings) > 0:
            for topping in toppings:
                cart_item.topping.add(topping)
            cart_item.save()
        cart.total += cart_item.price
        cart.save()
    messages.add_message(request, messages.INFO, f'Item {cart_item.item_detail} added!')
    return HttpResponseRedirect(reverse('home'))

def removeItem_view(request, cart_item_id):
    cart_item = Cart_Item.objects.get(pk=cart_item_id)
    cart = Cart.objects.get(user=request.user)
    cart.total -= cart_item.price
    cart_item.delete()
    cart.save()
    messages.add_message(request, messages.INFO, f'Item {cart_item.item_detail} removed!')
    return HttpResponseRedirect(reverse('cart'))

def emptyCart_view(request):
    cart = Cart.objects.get(user=request.user)
    cart.total = 0
    cart.save()
    cart_items = Cart_Item.objects.filter(cart=cart)
    if cart_items:
        for cart_item in cart_items:
            cart_item.delete()
    messages.add_message(request, messages.INFO, 'Cleared your cart!')
    return HttpResponseRedirect(reverse('cart'))

def cart_view(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = Cart_Item.objects.filter(cart=cart)
    if not cart_items:
        return render(request, 'cart.html', {'empty': True})
    return render(request, 'cart.html', {'empty': False, 'cart_items': cart_items, 'cart':cart})  

def order_view(request):
    cart = Cart.objects.get(user=request.user)
    cart_items =  Cart_Item.objects.filter(cart=cart)

    #create a new empty order
    order = Order(user=request.user, total=cart.total)
    order.save()

    for cart_item in cart_items:
        order_item = Order_Item(order=order, item_detail=cart_item.item_detail, size=cart_item.size, price=cart_item.price)
        order_item.save()
        order_item.topping.set(cart_item.topping.all())
        order_item.save()
    messages.add_message(request, messages.SUCCESS, f'Order #{order.pk} placed successfully!')
    emptyCart_view(request)
    return HttpResponseRedirect(reverse('home'))

def orders_view(request):
    orders = Order.objects.filter(user=request.user)
    if not orders:
        return render(request, 'orders.html', {'empty': True})
    dic = dict()
    for order in orders:
        order_items = Order_Item.objects.filter(order=order)
        dic.update({order: order_items})

    return render(request, 'orders.html', {'empty': False, 'dic': dic})

def viewOrders_view(request):
    if request.method == 'POST':
        pass
    else:
        if request.user.is_staff:
            orders = Order.objects.exclude(status='Completed')
            if not orders:
                return render(request, 'vieworders.html', {'empty': True})
            dic = dict()
            for order in orders:
                order_items = Order_Item.objects.filter(order=order)
                dic.update({order: order_items})

            return render(request, 'vieworders.html', {'empty': False, 'dic': dic})

def markComplete_view(request, order_item_id):
    order = Order.objects.get(pk=order_item_id)
    order.status = 'Completed'
    order.save()
    messages.add_message(request, messages.SUCCESS, f'Marked Order #{order.pk} as completed')
    return HttpResponseRedirect(reverse('vieworders'))


