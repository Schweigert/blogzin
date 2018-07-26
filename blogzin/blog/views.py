from django.http import HttpResponse

def blog_index(request):
    return HttpResponse("My blog is alive!")
