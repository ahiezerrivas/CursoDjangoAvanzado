"""
    Django models utilities
"""

#   Django

from django.db import models

class CRideModel(models.Model):
    """
        Comparte Ride base model.

    CRideModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        + modified (DateTime): Store the last datetime the object was modified.
    """

    created = models.DateField(
        'created at',
        auto_now=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was modified.'
    )
    
    class Meta:
        """
            Meta option.
        """
        abstract = True

        get_latests_by= 'created'
        ordering = ['-created', '-mod']


# class Person(models.Model):
#     first_name = models.CharField()
#     last_name = models.CharField()

# class MyPerson(Person):
#     class Meta:
#         proxy = True
    
#     def say_hi(name):
#         pass

# MyPerson.objects.all()
# ricardo = MyPerson.objects.get(pk=1)
# ricardo.say_hi('Pablo')

# rulo = Person.objects.get(pk=2)
# rulo.say_hi('Pablo')

