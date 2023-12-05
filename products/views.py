from django.shortcuts import render,  HttpResponseRedirect, redirect, get_object_or_404
from .models import Post ,GiftCard
from .forms import AddProduct,AddGiftCard
from django.db.models import  Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def products(request):
    all_posts = Post.objects.all()
    query = request.GET.get('q')
    page = request.GET.get('page', 1) 
    top_sellers_posts = all_posts.filter(product_type='top_sellers')
    new_posts = all_posts.filter(product_type='new_releases')
    old_posts =all_posts.filter(product_type ='old_releases')
    top = all_posts.filter(product_type='top')
    event = all_posts.filter(product_type='event')
    gadget = all_posts.filter(product_type='gadget')

    if query:
        keywords = query.split()
        condition = Q()
        for keyword in keywords:
            condition |= Q(title__icontains=keyword) | Q(amount__icontains=keyword) | Q(product_type__icontains=keyword)

        all_posts = all_posts.filter(condition)

    paginator = Paginator(all_posts, 10)  
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'query': query,
        'gadget': gadget,
        'event': event,
        'top': top,
        'new_posts': new_posts,
        'top_sellers_posts': top_sellers_posts,
        'old_posts':old_posts,
    }

    return render(request, 'products/products.html', context)
#allowing a specific user
def user_is_specific_user(user):
    return user.username == 'imranlifik'


@user_passes_test(user_is_specific_user)
def addproducts(request):
    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True, user=request.user)
            return redirect('addproducts')
    else:
        form = AddProduct()

    return render(request, './products/addproducts.html', {'form': form})




login_required 
@user_passes_test(user_is_specific_user)
def editproduct(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = AddProduct(instance=post)
    return render(request, './products/addproducts.html', {'form': form})



def viewproduct(request, title):
    posts = Post.objects.all()
    post = get_object_or_404(Post, title=title)
    return render(request, './products/viewproduct.html', {'post': post, 'posts': posts})


def giftcards(request):
    giftcards = GiftCard.objects.all()
    query = request.GET.get('q')
    psn = giftcards.filter(giftcard_type='psn')
    stream = giftcards.filter(giftcard_type='stream')
    xbox =giftcards.filter(giftcard_type ='xbox')
    nintendo= giftcards.filter(giftcard_type='nintendo')
    ea = giftcards.filter(giftcard_type='ea')
    microsoft = giftcards.filter(giftcard_type='microsoft')
    riot = giftcards.filter(giftcard_type='riot')
    blizzard = giftcards.filter(giftcard_type='blizzard')
    levelup = giftcards.filter(giftcard_type='levelup')

    if query:
        keywords = query.split()
        condition = Q()
        for keyword in keywords:
            condition |= Q(title__icontains=keyword) | Q(region__icontains=keyword) | Q(price__icontains=keyword) | Q(giftcard_type__icontains=keyword)

        giftcards = giftcards.filter(condition)

    context = {
        'giftcard':giftcards,
        'query':query,
        'psn':psn,
        'stream':stream,
        'xbox':xbox,
        'nintendo':nintendo,
        'ea':ea,
        'microsoft':microsoft,
        'riot':riot,
        'blizzard':blizzard,
        'levelup':levelup,
    }
    return render(request, './products/giftcards.html' ,context)


@user_passes_test(user_is_specific_user)
def addgiftcards(request):
    if request.method == 'POST':
        form = AddGiftCard(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True, user=request.user)
            return redirect('addgiftcards')
    else:
        form = AddGiftCard()

    return render(request ,'./products/addgiftcards.html', {'form':form})




login_required 
@user_passes_test(user_is_specific_user)
def editgiftcards(request ,id):
    post = GiftCard.objects.get(id=id)
    if request.method == 'POST':
        form = AddGiftCard(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('giftcards')
    else:
        form = AddGiftCard(instance=post)
    return render(request, './products/addgiftcards.html', {'form':form})