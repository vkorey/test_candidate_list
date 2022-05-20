from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import NewSkillForm
from .models import Skill, User


def index(request):
    users = User.objects.prefetch_related('skills__tag', 'skills')
    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
         request,
         'index.html',
         {'page': page, }
    )


def profile(request, username):
    if request.method == "POST":
        form = NewSkillForm(
            request.POST
        )
        return HttpResponse(request.POST)
    candidate = get_object_or_404(User, username=username)
    skill_list = Skill.objects.filter(candidates=candidate).prefetch_related('tag')
    form = NewSkillForm()
    return render(
        request,
        'profile.html',
        {'candidate': candidate,
         'skill_list': skill_list,
         'form': form,
         },
    )


def delete(request, id):
    qs = Skill.objects.filter(id=id, candidates__id=request.user.id)
    if qs.exists():
        qs.delete()
    return redirect('profile', username=request.user.username)
