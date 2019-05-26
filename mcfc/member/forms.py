from django.forms import ModelForm
from member.models import Member

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['first_name','last_name','dob','Address','email','member_type']