from django.shortcuts import render


def register(request):
    return render(request, template_name='accounts/register-page.html')


def login(request):
    return render(request, template_name='accounts/login-page.html')


def profile_details(request, pk: int):
    return render(request, template_name='accounts/profile-details.html')


def edit_profile(request, pk: int):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_profile(request, pk: int):
    return render(request, template_name='accounts/profile-delete-page.html')





