from django.urls import path, include

from petstagram.common import views
from petstagram.common.views import CommonView

urlpatterns = [
    path('', CommonView.as_view(), name='home'),
    # path('', views.common, name='home'),
    path('like/<int:photo_id>/', views.like_functionality, name='like'),
    path('share/<int:photo_id>/', views.copy_link_to_clipboard, name='share'),
    path('comment/<int:photo_id>/', views.add_comment, name='comment'),

]