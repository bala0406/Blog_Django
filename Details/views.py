from django.shortcuts import get_object_or_404, redirect, render
from .models import UserInformation
from django.http import HttpResponse
from .forms import UserForm
from .serializers import PostSerializer
from django.db.models import Q
from django.core.paginator import Paginator


# Rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins


class PostView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = UserInformation.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     serializer = PostSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)


# simplified rest view

# class PostView(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, *kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# MVT

def read_details(request):
    if request.method == "POST":
        form = UserInformation.objects.all()
        return render(request, "Details/read.html", {"form": form})
    form = UserInformation.objects.all()
    paginator = Paginator(form, 3)

    page = request.GET.get('page')
    formview = paginator.get_page(page)
    return render(request, "Details/read.html", {"formview": formview, "form": form})


def create_details(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.currentuser = request.user
            instance.save()
            return redirect("Details:read")
    else:
        form = UserForm()
    return render(request, "Details/create.html", {"form": form})


def update_details(request, updatename):
    forminstance = get_object_or_404(UserInformation, name=updatename)
    if request.method == "POST":
        form = UserForm(request.POST, instance=forminstance)
        if form.is_valid():
            forminstance = form.save(commit=False)
            forminstance.author = request.user
            forminstance.save()
            return redirect('Details:read', name=updatename)
    else:
        form = UserForm(instance=forminstance)
    return render(request, 'Details/update.html', {'form': form})


def detailed_view(request, name):
    details = UserInformation.objects.get(name=name)
    return render(request, "Details/userdetail.html", {"details": details})


def delete_details(request, deletename):
    form = UserInformation.objects.get(name=deletename)
    form.delete()
    return redirect("Details:read")


def search_details(request):
    template = "Details/read.html"

    try:
        query = request.GET.get("q")
        # page = request.GET.get('page')
    except:
        query = None
        page = None
    if query:
        form = UserInformation.objects.filter(
            Q(name__icontains=query) | Q(about__icontains=query))

    # if form[0]: 
    #     flag = True
    # else:
    #     flag = False    

    pages = Paginator(form, 5)

    page = request.GET.get('page')
    formview = pages.get_page(page)
    return render(request, "Details/read.html", {"formview": formview, "form": form})
