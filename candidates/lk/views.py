from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FormForm
from .models import Skill, Tag, User


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
    candidate = get_object_or_404(User, username=username)
    skill_list = Skill.objects.filter(
        candidate=candidate
    ).prefetch_related('tag')
    if request.method == "POST":
        form = FormForm(request.POST)
        if form.is_valid():
            tag, _ = Tag.objects.get_or_create(name=form.cleaned_data['tag'])
            skill, _ = Skill.objects.get_or_create(
                name=form.cleaned_data['skill'],
                tag=tag
            )
            skill.candidate.add(candidate)
            skill.tag = tag
            skill.save()
            return redirect('profile', username=request.user.username)
    else:
        form = FormForm()
    return render(
        request,
        'profile.html',
        {'candidate': candidate,
         'skill_list': skill_list,
         'form': form,
         },
    )


def delete(request, id):
    qs = Skill.objects.filter(id=id, candidate__id=request.user.id)
    if qs.exists():
        qs.delete()
    return redirect('profile', username=request.user.username)
