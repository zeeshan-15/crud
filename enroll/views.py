from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from .forms import StudentRegistration
from .models import User
from django.views.generic.base import TemplateView, RedirectView
from django.views import View


class User_Add_Show_View(CreateView):
    model = User
    form_class = StudentRegistration
    template_name = 'enroll/list_add_data.html'

    def get_success_url(self):
        return reverse('list_add_data')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        stud = User.objects.all()
        context = {'stu': stud, 'form': fm}
        return context


class User_Update_View(UpdateView):
    model = User
    form_class = StudentRegistration
    template_name = 'enroll/update_student.html'

    def get_success_url(self):
        return reverse('list_add_data')


class User_Delete_View(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
