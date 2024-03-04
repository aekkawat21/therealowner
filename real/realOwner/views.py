from django.shortcuts import render, redirect ,get_object_or_404
from .models import Item ,UserProfile ,Category
from django.shortcuts import get_object_or_404
from .forms import ItemForm, UserForm , UserProfileForm ,EmailUpdateForm ,ContactChannelsForm 
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm 
from django.contrib import messages
from django.core.paginator import Paginator
from django.templatetags.static import static
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Count


# Create your views here.
def my_view(request):
    image_url = static('images/my_image.jpg')


def home(req):
    
    items = Item.objects.all()
    context = {
        'items': items,
        'obj': profile,
    }
    return render(req, 'registration/home.html', context)


def item_list(request):
    item_list = Item.objects.all()
    paginator = Paginator(item_list, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.prefetch_related('item_set').all()
    return render(request, 'app/item_list.html', {'page_obj': page_obj},)

    


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
def create_profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile') 
    else:
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
    return render(request, 'edit/create_profile.html', {'form': form, 'profile': profile})

@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user  
            item.save()
            messages.success(request, 'Your item has been posted!')
            return redirect('item_list')  
    else:
        form = ItemForm()
    return render(request, 'app/create_item.html', {'form': form})

@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list', )  
    else:
        form = ItemForm(instance=item)

    return render(request, 'app/edit_item.html', {'form': form})

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id, owner=request.user)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Your item has been deleted.')
        return redirect('item_list')
    return render(request, 'app/delete_item.html', {'item': item})




def edit_password(req):
    if req.method == 'POST':
        form = PasswordChangeForm(req.user, req.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(req, user)
            messages.success(req, 'รหัสผ่านของคุณถูกเปลี่ยนแล้ว!')
            return redirect('edit_password')
        else:
            messages.error(req, 'กรุณาแก้ไขข้อผิดพลาดด้านล่าง')
    else:
        form = PasswordChangeForm(req.user)

    context = {'form': form}
    return render(req, 'edit/edit_password.html', context)


@login_required
def edit_email(request):
    if request.method == 'POST':
        form = EmailUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your email has been updated.')
            return redirect('profile')
    else:
        form = EmailUpdateForm(instance=request.user)
    
    return render(request, 'edit/edit_email.html', {'form': form})


@login_required
def edit_contact_channels(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)  # Or however you get the profile

    if request.method == 'POST':
        form = ContactChannelsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your contact channels have been updated.')
            return redirect('profile')  # Redirect to the profile page or wherever is appropriate
    else:
        form = ContactChannelsForm(instance=profile)

    return render(request, 'edit/edit_contact_channels.html', {'form': form})

@login_required
def edit_personal_details(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
    
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your personal details have been updated.')
            return redirect('edit_personal_details')  # Redirect to a success page or the same page
    else:
        profile_form = UserProfileForm(instance=profile)

    return render(request, 'edit/edit_personal_details.html', {'profile_form': profile_form})



@login_required
def edit_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('edit_profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'edit/edit_profile.html', {'form': form})


def item_list(request,ct):
    items = Item.objects.filter(category__name=ct).order_by('-store_date_of_purchase')
    
    print("Number of items retrieved:", len(items))  

    return render(request, 'app/item_list.html', {'items': items,'ct':ct})