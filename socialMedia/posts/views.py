from django.shortcuts import render
from .models import Post
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def post_create(request):
    if request.method=='POST':
        # collect data from frontend page
        form = PostCreateForm(data=request.POST,files = request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
    else:
        # send filed to the frontend
        form = PostCreateForm(data=request.GET)
        
    return render(request,'posts/create.html',{'form':form})