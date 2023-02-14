from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}'s account created successfully")
            return redirect('home')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'user/register.html', {'form' : form})


def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES,
                    instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, f"Profile details updated successfully")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }        

    return render(request, 'user/profile.html', context)
