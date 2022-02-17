# code credits from: https://github.com/Code-Institute-Submissions/project-spacex/blob/master/main_pages/views.py

from django.shortcuts import render

def handler404(request, exception):
    return render(request, "404.html", {"page_title": "404"}, status=404)


def handler500(request):
    return render(request, "500.html", status=500)
