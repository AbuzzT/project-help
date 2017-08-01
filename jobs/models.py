from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from taggit.managers import TaggableManager


CATEGORIES = (
    ('1', 'Home & Gardening'),
    ('2', 'Handyman & Repair'),
    ('3', 'Health & Fitness'),
    ('4', 'Business Services'),
    ('5', 'Event Planning'),
    ('6', 'Beauty & Wellness'),
    ('7', 'Education & Learning'),
    ('8', 'Technology & IT'),
    ('9', 'Odd & Unique'),
)


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    help_text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="categories/", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/job_<id>/<filename>
    return 'user_{0}/job_{1}/{2}'.format(instance.user.id, instance.id, filename)


class Job(models.Model):
    poster = models.ForeignKey(User)
    helper = models.ForeignKey(User, related_name="helper", blank=True, null=True)
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category)
    tags = TaggableManager()
    description = models.TextField(max_length=500)
    date = models.DateTimeField()
    online = models.BooleanField(default=False)
    address = models.CharField(max_length=120, blank=True, null=True)
    suite = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    province = models.CharField(max_length=30, blank=True, null=True)
    postal_code = models.CharField(max_length=6, blank=True, null=True)
    market_place = models.BooleanField(default=True)  # false is with budget
    budget = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
    flat_rate = models.BooleanField(default=True)  # false is hourly
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # video = models.FileFied(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    # def clean(self):
    #     # Don't allow helper to be the same as poster.
    #     if self.helper == self.poster:
    #         raise ValidationError("Helper can't be the same as Poster")


class Offer(models.Model):
    job = models.ForeignKey(Job)
    user = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    # Image
    # Video
    # Comments

    def __str__(self):
        return f"{self.user} - {self.amount}"
