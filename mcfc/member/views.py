from django.shortcuts import render
from member.forms import MemberForm
from member.models import Member
from django.views.generic.edit import CreateView
# Create your views here.

class MemberView(CreateView):
    template_name = "member/index.html"
    model = Member
    form_class = MemberForm
    success_url = '/member'

    def form_valid(self,form):
        return super().form_valid(form)

# def member(request):
#     form = forms.MemberForm()
#     return render(request,'member/index.html',{'form':form})
