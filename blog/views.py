from django.shortcuts import render
post=[
    {
        'author':'RaisaOR',
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_posted':'December 5, 2022'
    },
    {
        'author':'Jane Doe',
        'title': 'Blog Post 2',
        'content':'Secon post content',
        'date_posted':'December 6, 2022'
    }
]
# Create your views here.
def home(request):
    context={
        'posts':post
    }
    return render(request,"blog/home.html",context)

def about(request):
    return render(request,"blog/about.html",{'title':'About'})