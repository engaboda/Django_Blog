from django.shortcuts import render , get_object_or_404 , redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,HttpResponseRedirect 
from posts.models import Posts
from .forms import PostForm
from django.db.models import Q

from django.contrib import messages

# Create your views here.


def post_create(request):
    if request.method=="POST":
        print request.POST.get("content")
        print request.POST.get("title")
    form = PostForm(request.POST , request.FILES or None)
    if form.is_valid():
        instance= form.save(commit=False)
        instance.save()
        messages.success(request , " Successfuly Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request , "Not Successfuly Created")
    context = {
        "form":form,
    }
    return render(request,"PostForm.html" , context)








def post_retreive(request,id=None):
    instance = get_object_or_404(Posts,id=id)
    context = {
        "title":"retreive",
        "instance" : instance
    }
    return render(request,"post_details.html" , context)






def post_list(request):
    
    query_list = Posts.objects.all().order_by('-id')
    query = request.GET.get("query")
    if query:
        query_list = query_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)
            )


    paginator = Paginator(query_list, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

      
    context = {
            "title" : "User List",
            "objetcs_list" : query_list,
            "contacts":contacts,
        }




    return render(request,"base.html" , context)
























def post_update(request , id=None):
    instance = get_object_or_404(Posts , id=id)
    form = PostForm(request.POST or None  , request.FILES or None ,  instance=instance )
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request , " Successfuly Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request , "Not Successfuly Updated")
    context = {
        "form":form,
    }
    return render(request,"PostForm.html" , context)


def post_delete(request , id=None):
    isinstance = get_object_or_404(Posts , id=id)
    isinstance.delete()
    messages.success(request,"successfully deleted")
    return redirect( "posts:list" )