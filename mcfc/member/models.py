from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
# Create your models here.
class Member(models.Model):
    MEMBER_TYPE = (
        (1, 'international membership'),
        (2, 'national membership'),
        (3, 'no memership')
    )
    first_name = models.CharField(_("first name"),max_length = 30)
    last_name = models.CharField(_("last name"),max_length = 30)
    dob = models.DateField(_("Date of Birth"))
    Address = models.CharField(max_length = 300)
    email = models.EmailField(max_length=254)
    member_type = models.IntegerField(_("choose member type"),max_length=1,choices = MEMBER_TYPE)


    class Meta:
        verbose_name = 'member'
        verbose_name_plural = 'members'
        db_table = 'member'

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("Member_detail", kwargs={"pk": self.pk})

