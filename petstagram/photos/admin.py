from django.contrib import admin

from petstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'description', 'get_tagged_pets')

    @staticmethod
    def get_tagged_pets(object):
        result = (str(pet) for pet in object.tagget_pets.all())
        return ', '.join(result)


