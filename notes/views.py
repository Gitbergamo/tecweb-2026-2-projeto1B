from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Tag


def _resolve_tag(tag_nome):
    """Retorna a Tag correspondente ao nome informado, criando-a caso ainda
    nao exista. Evita tags duplicadas no banco. Retorna None se vazio."""
    tag_nome = (tag_nome or '').strip()
    if not tag_nome:
        return None
    tag, _ = Tag.objects.get_or_create(nome=tag_nome)
    return tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = _resolve_tag(request.POST.get('tag'))
        Note.objects.create(title=title, content=content, tag=tag)
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})


def edit(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.title = request.POST.get('titulo')
        note.content = request.POST.get('detalhes')
        note.tag = _resolve_tag(request.POST.get('tag'))
        note.save()
        return redirect('index')
    else:
        return render(request, 'notes/edit.html', {'note': note})


def delete(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('index')
    else:
        return render(request, 'notes/delete.html', {'note': note})


def tags(request):
    all_tags = Tag.objects.all()
    return render(request, 'notes/tags.html', {'tags': all_tags})


def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    notes = tag.note_set.all()
    return render(request, 'notes/tag_detail.html', {'tag': tag, 'notes': notes})
