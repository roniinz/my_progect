from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib import auth
from .forms import ShopUserLoginForm, ShopUserRegisterForm
from django.urls import reverse, reverse_lazy

# Create your views here.
from .models import ShopUser


def login(request):
    title = 'вход'

    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    title = 'регистрация'
    form = ShopUserRegisterForm()
    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            form = ShopUserRegisterForm()

    content = {'title': title, 'form': form}
    return render(request, 'authapp/register.html', content)


class EditView(UpdateView):
    model = ShopUser
    template_name = 'authapp/register.html'
    fields = '__all__'
    success_url = reverse_lazy('index')


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data
