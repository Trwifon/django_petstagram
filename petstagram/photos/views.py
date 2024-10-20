from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


class AddPhotoView(CreateView):
    model = Photo
    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('home')


# def add_photo(request):
#     form = PhotoCreateForm(request.POST or None, request.FILES or None)
#
#     if form.is_valid():
#         form.save()
#
#         return redirect('home')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, template_name='photos/photo-add-page.html', context=context)


class DetailsPhotoView(DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['likes'] = self.object.like_set.all()
        context['comments'] = self.object.comment_set.all()
        context['comment_form'] = CommentForm

        return context


# def photo_details(request, pk: int):
#     photo = Photo.objects.get(pk=pk)
#     likes = photo.like_set.all()
#     comments = photo.comment_set.all()
#
#     comment_form = CommentForm()
#
#     context = {
#         'photo': photo,
#         'likes': likes,
#         'comments': comments,
#         'comment_form': comment_form,
#     }
#
#     return render(request,'photos/photo-details-page.html', context)


class EditPhotoView(UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = 'photos/photo-edit-page.html'

    def get_success_url(self):
        return reverse_lazy(
            'photo-details',
            kwargs =
            {
                'pk': self.object.pk
            }
        )


# def photo_edit(request, pk: int):
#     photo = Photo.objects.get(pk=pk)
#     form = PhotoEditForm(request.POST or None, instance=photo)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('photo-details', pk)
#
#     context = {
#         'photo': photo,
#         'form': form,
#     }
#
#     return render(request, template_name='photos/photo-edit-page.html', context=context)


def photo_delete(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home')


