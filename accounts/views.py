from django.shortcuts import  render, redirect
from .forms import NewUserForm, ProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.utils.translation import gettext as _

def register_request(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect("login")
            messages.error(request, "Unsuccessful registration. Invalid information.")
        form = NewUserForm()
        return render (request=request, template_name="registration/register.html", context={"register_form":form})

@login_required()
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
        else:
            messages.error(request, _('Please provide the correct information!'))
    else:
        user_form = NewUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/update_profile.html', {
        'profile_form': profile_form
})

def ruang_favorit(request):
    user = request.user
    ruang_favorit = user.favorit.all()

    for x in ruang_favorit:
        if x.favorit.filter(id=request.user.id).exists():
            x.is_favorit = True

    return render (request=request, template_name="ruang_favorit.html", context={"ruang_favorit":ruang_favorit})