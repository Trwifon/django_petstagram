from django.core.validators import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FileSizeValidator:
    def __init__(self, max_size_mb, message = None):
        self.max_size_mb = max_size_mb
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"File size must be below or equal {self.max_size_mb} MB"
        else:
            self.__message = value

    def __call__(self, value):
        if value.size > self.max_size_mb * 1024 * 1024:
            raise ValueError(self.message)
