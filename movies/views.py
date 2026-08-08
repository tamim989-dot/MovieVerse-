from django.shortcuts import render, get_object_or_404
from .models import Movie


def home(request):

    query = request.GET.get('q')
    category = request.GET.get('genre')

    movies = Movie.objects.all()

    if query:
        movies = movies.filter(title__icontains=query)

    if category:
        movies = movies.filter(genre=category)

    genres = Movie.objects.values_list('genre', flat=True).distinct()

    return render(request, "movies/home.html", {
        "movies": movies,
        "genres": genres
    })


def detail(request, id):

    movie = get_object_or_404(Movie, id=id)

    return render(request, "movies/detail.html", {
        "movie": movie
    })


def about(request):
    return render(request, "movies/about.html")


def contact(request):
    return render(request, "movies/contact.html")


def privacy(request):
    return render(request, "movies/privacy.html")


def disclaimer(request):
    return render(request, "movies/disclaimer.html")
