from django.shortcuts import render, redirect
from .models import Item ,UserProfile 
from django.shortcuts import get_object_or_404
from .forms import ItemForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages


# Create your views here.
def home(req):
    return render(req, 'registration/home.html')



def item_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    items = Item.objects.all()
    if query:
        items = items.filter(title__icontains=query)
    if category:
        items = items.filter(category__name=category)
    return render(request, 'app/item_list.html', {'items': items})


def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'app/item_detail.html', {'item': item})

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
    return render(request, 'app/user_profile.html', {'profile_user': user, 'items': items})

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
    return render(request, 'app/edit_user_profile.html', {'form': form})



