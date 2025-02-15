from Scripts.bottle import request
from Tools.pynche.DetailsViewer import DetailsViewer
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, FormView

from petstagram.accounts.views import profile_details
from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import PetForm, PetDeleteForm
from petstagram.pets.models import Pet




class AddPetView(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})


# def add_pet(request):
#     form = PetForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('profile-details', pk=1)
#     context = {'form': form,}
#
#     return render(request, template_name=, context=context)


class DetailsPetView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = self.object.photo_set.all()
        context['comment_form'] = CommentForm
        return context


# def pet_details(request, username: str, pet_slug: str):
#     pet = Pet.objects.get(slug=pet_slug)
#     all_photos = pet.photo_set.all()
#
#     comment_form = CommentForm()
#
#     context = {
#         'pet': pet,
#         'all_photos': all_photos,
#         'comment_form': comment_form
#     }
#
#     return render(request, 'pets/pet-details-page.html', context)


class EditPetView(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'

    def get_success_url(self):
        return reverse_lazy('pet-details',
                            kwargs = {
                                'username': self.kwargs['username'],
                                'pet_slug': self.kwargs['pet_slug'],
                            })


# def pet_edit(request, username: str, pet_slug: str):
#     pet = Pet.objects.get(slug=pet_slug)
#
#     if request.method == 'GET':
#         form = PetForm(instance=pet, initial=pet.__dict__)
#     else:
#         form = PetForm(request.POST, instance=pet)
#
#         if form.is_valid():
#             form.save()
#
#             return  redirect('pet-details', username, pet_slug)
#
#     context = {
#         'form': form,
#     }
#     return render(request, template_name='pets/pet-edit-page.html', context=context)


class DeletePetView(DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = 'pets/pet-delete-page.html'
    slug_url_kwarg = 'pet_slug'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})

    def get_initial(self):
        initial = self.object.__dict__
        return initial


# def pet_delete(request, username: str, pet_slug: str):
#     pet = Pet.objects.get(slug=pet_slug)
#
#     if request.method == 'POST':
#         pet.delete()
#         return redirect('profile-details', username, pk = 1)
#
#     form = PetDeleteForm(initial=pet.__dict__)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, template_name='pets/pet-delete-page.html', context=context)


