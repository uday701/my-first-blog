from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .forms import Form_list

def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
def post_detail(request,pk):
	post=get_object_or_404(Post,pk=pk)
	return render(request,'blog/post_detail.html',{'post':post})
    
    
def post_new(request):
    if request.method == "POST":
        form = Form_list(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Form_list()
    return render(request, 'blog/post_edit.html', {'form': form})

# Create your views here.
