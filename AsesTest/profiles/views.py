from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile

# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'#me falto poner el template a donde iban a direccionarse
    paginate_by = 8

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):#me falto esto sobre el error de que no se encuentre el perfil
        return get_object_or_404(Profile, user__username=self.kwargs['username'])