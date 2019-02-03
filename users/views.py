from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm
import users.globalbaz
from .models import User



def register(request ) :

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()


            messages.success(request, f'Your profile was successfully created!')

            return redirect('login')
        else:
            messages.error(request, f'Please correct the error below.')
    else:
        user_form = UserForm()

    return render(request, 'users/register.html', {
        'user_form': user_form,


    })

def get_user_profile(request,username):

    try:
        user_p = User.objects.get(username=username)

    except (User.DoesNotExist):
        messages.warning(request,'No such username exists')
        return redirect('blog-home')
    return render(request,'users/user_profile.html',{"user_p" : user_p })



'''
if request.method == 'POST':
    user_form = UserForm(request.POST)
    profile_form = ProfileForm(request.POST)
    if user_form.is_valid() and profile_form.is_valid():

        global user
        user = user_form.save()

        user.profile.type = profile_form.cleaned_data.get('type')
        user.profile.save()

        messages.success(request, f'Your profile was successfully created!')

        return redirect('register_student')
    else:
        messages.error(request, f'Please correct the error below.')
else:
    user_form = UserForm()
    profile_form = ProfileForm()
return render(request, 'users/register.html', {
    'user_form': user_form,
    'profile_form': profile_form
})
'''


'''
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
'''
