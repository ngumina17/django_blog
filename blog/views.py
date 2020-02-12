from django.shortcuts import render, redirect
from .models import Author, Blog
from .forms import AuthorForm, BlogForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def author_list(request):
    author = Author.objects.all()
    return render(request, 'blog/author_list.html', {'author': author})


def author_detail(request, pk):
    author = Author.objects.get(id=pk)
    return render(request, 'blog/author_detail.html', {'author': author})


def blog_detail(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})


def blog_list(request):
    blog = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blog': blog})

@login_required
def blog_delete(request, pk):
    Blog.objects.get(id=pk).delete()
    return redirect('blog_list')

@login_required
def author_form(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = AuthorForm()
    return render(request, 'blog/author_form.html', {'form': form})

@login_required
def blog_form(request, pk):
    author = Author.objects.get(id=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm(initial={'author' : author})
    return render(request, 'blog/blog_form.html', {'form': form})

@login_required
def blog_edit(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blog_form.html', {'form': form})

@login_required
def author_edit(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'blog/author_form.html', {'form': form})

# def search_form(request, info):
#     author = Author.objects.filter(name__search=info)
#     return render(request, 'blog/author_list.html', {'author': author})
