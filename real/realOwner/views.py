from django.shortcuts import render, redirect
from .models import Item ,UserProfile 
from django.shortcuts import get_object_or_404
from .forms import ItemForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm ,ReviewForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.templatetags.static import static
from django.contrib.auth.models import User




# Create your views here.
def my_view(request):
    image_url = static('images/my_image.jpg')

def home(req):
    return render(req, 'registration/home.html')


def item_list(request):
    item_list = Item.objects.all()
    paginator = Paginator(item_list, 10)  # แสดง 10 สินค้าต่อหน้า
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/item_list.html', {'page_obj': page_obj})


def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    reviews = item.reviews.all()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.item = item
            review.author = request.user
            review.save()
            return redirect('item_detail', item_id=item_id)
    else:
        review_form = ReviewForm()

    return render(request, 'app/item_detail.html', {
        'item': item, 'reviews': reviews, 'review_form': review_form
    })


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def profile(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)
    context = {
        'user': user,
        'profile': profile
    }
    return render(request, 'registration/profile.html', context)

@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user  # Set the owner of the item to the current user
            item.save()
            messages.success(request, 'Your item has been posted!')
            return redirect('item_list')  # Redirect to the item listing page
    else:
        form = ItemForm()
    return render(request, 'app/create_item.html', {'form': form})

@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id, owner=request.user)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your item has been updated!')
            return redirect('item_detail', item_id=item.id)
    else:
        form = ItemForm(instance=item)
    return render(request, 'app/edit_item.html', {'form': form, 'item': item})

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id, owner=request.user)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Your item has been deleted.')
        return redirect('item_list')
    return render(request, 'app/delete_item.html', {'item': item})

def view_user_profile(request, username):
    user = get_object_or_404(User, username=username)
    items = Item.objects.filter(owner=user)
    return render(request, 'registration/user_profile.html', {'profile_user': user, 'items': items})

@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('view_user_profile', username=request.user.username)
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'registration/edit_user_profile.html', {'form': form})



