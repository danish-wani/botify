from django import urls
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib.auth import authenticate, login

from .forms import AuthenticationForm


class UserLogin(TemplateView):
    template_name = 'user/user_login.html'
    form_class = AuthenticationForm

    def get_context_data(self, **kwargs):
        """
            Updates the default context data
        :param kwargs: Default keyword args passed
        :return: Updated context data containing additional data like self.form_class
        """
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if request.user.is_authenticated:
            return redirect(urls.reverse('user:home'))

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
            This authenticates a user based on the username and password provided,
            and send the appropriate JSON response based on whether the user is authentic or not.
        :param request: HTTP request
        :param args: Any positional args
        :param kwargs: Any keyword args
        :return: JSON response
        """
        form_obj = self.form_class(data=request.POST.copy())
        form_obj.is_valid()

        user_obj = authenticate(username=form_obj.cleaned_data["username"], password=form_obj.cleaned_data["password"])

        if user_obj:
            login(request, user_obj)
            return redirect(urls.reverse('user:home'))

        return JsonResponse({"message": "Unauthenticated User"})


class Home(TemplateView):
    template_name = 'landing_page.html'

    def get(self, request, *args, **kwargs):
        """
            Render a template and update the context.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        context = self.get_context_data(**kwargs)
        context["user_obj"] = request.user
        return self.render_to_response(context)
