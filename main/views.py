import urllib

from django.shortcuts import render, get_object_or_404, redirect
import requests
from .models import Articles
from django.utils import timezone
from django.conf import settings





def index(request):
    api_key = "07967d20b4d802b617a7ee0295d1c142"
    discover_url = f"https://api.themoviedb.org/3/discover/movie?sort_by=vote_average.desc&vote_count.gte=500&api_key={api_key}&page=1"

    response = requests.get(discover_url)
    data = response.json()

    movies = data['results']

    movies_info = []

    for movie in movies:
        movie_id = movie['id']
        movie_details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
        movie_response = requests.get(movie_details_url)
        movie_data = movie_response.json()

        genres = movie_data['genres'][:3]
        genres_list = [genre['name'] for genre in genres]

        movie_info = {
            'title': movie_data['title'],
            'rating': movie_data['vote_average'],
            'genres': genres_list,
            'description': movie_data['overview']
        }

        if movie_data['poster_path'] is not None:
            movie_info['image'] = "https://image.tmdb.org/t/p/w500" + movie_data['poster_path']
        else:
            movie_info['image'] = ""

        movies_info.append(movie_info)


        for movie in movies_info:
            request.session[f'img_route_{movie["title"]}'] = movie['image']

        if len(movies_info) >= 100:
            break

    data = {'movies_info': movies_info}

    return render(request, 'main/index.html', data)


def add_review(request, movie_title):
    movie_title = urllib.parse.unquote(movie_title)
    img_route = request.session.get(f'img_route_{movie_title}', '')

    if request.method == 'POST':
        # reCAPTCHA
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if not result['success']:
            return render(request, 'main/add_review.html', {
                'error': 'Invalid reCAPTCHA. Please try again.',
                'movie_title': movie_title
            })

        else:
            review_text = request.POST.get('review_text')
            rating = request.POST.get('rating')
            review_type = request.POST.get('review_type')
            name = request.POST.get('name')

            article = Articles(
                title=movie_title,
                name=name,
                body=review_text,
                rating=int(rating),
                review_type=int(review_type),
                img_route=img_route,
                date=timezone.now()
            )
            article.save()

            return redirect('list_review')

    return render(request, 'main/add_review.html', {'movie_title': movie_title})



def list_review(request):
    articles = Articles.objects.all()
    return render(request, 'main/list_review.html', {'articles': articles})


def delete_review(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    article.delete()
    return redirect('list_review')