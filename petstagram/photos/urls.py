from django.urls import path, include

from petstagram.photos import views
from petstagram.photos.views import AddPhotoView, DetailsPhotoView, EditPhotoView

urlpatterns = [
    path('add/', AddPhotoView.as_view(), name='add-photo'),
    path('<int:pk>/', include([
        path('', DetailsPhotoView.as_view(), name='photo-details'),
        path('edit/', EditPhotoView.as_view(), name='photo-edit'),
        path('delete/', views.photo_delete, name='photo-delete'),
]))
]
