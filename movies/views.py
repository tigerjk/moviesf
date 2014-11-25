from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.db.models import Q
import json
import urllib
from movies.models import Movie
from movies.serializers import MovieSerializer

url = 'https://data.sfgov.org/resource/yitu-d5am.json?$$app_token=CF2XYi6qCbEnJyq2rqNGo3KbX&'
# Create your views here.

class JSONResponse(HttpResponse):
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

def index(request):
	#inefficient, but this works... for now..
	Movie.objects.all().delete()
	movies=urllib.urlopen(url).read()
	json_data = json.loads(movies)
	title = ''
	fun_facts = ''
	distributor = ''
	release_year = ''
	locations = ''
	production_company = ''
	director = ''
	writer = ''
	actor_1 = ''
	actor_2 = ''
	actor_3 = ''

	for m in json_data:
		if 'title' in m:
			title = m['title']
		if 'release_year' in m:
			release_year = m['release_year']
		if 'locations' in m:
			locations = m['locations']
		if 'fun_facts' in m:
			fun_facts = m['fun_facts']
		if 'production_company' in m:
			production_company = m['production_company']
		if 'distributor' in m:
			distributor = m['distributor']
		if 'director' in m:
			director = m['director']
		if 'writer' in m:
			writer = m['writer']
		if 'actor_1' in m:
			actor_1 = m['actor_1']
		if 'actor_2' in m:
			actor_2 = m['actor_2']
		if 'actor_3' in m:
			actor_3 = m['actor_3']
		new_movie = Movie(title = title, release_year = release_year, locations = locations, production_company = production_company, director = director, writer = writer, actor_1 = actor_1, actor_2 = actor_2, actor_3 = actor_3, fun_facts=fun_facts, distributor=distributor)
		new_movie.save()
	
	#return render(request, "index.html", {'data': json_data})
	return render(request, "index.html", {})

@csrf_exempt
def get_movies(request):
	results = []
	if request.method == 'GET':
		query=request.GET.get('term', '')
		if request.is_ajax():
			movies = filter_movie(query)
			for movie in movies:
				movie_json = {}
				movie_json['id'] = movie.id
				movie_json['label'] = "Title:" + movie.title + " Location:" + movie.locations + " Director:" + movie.director
				movie_json['value'] = movie.locations
				results.append(movie_json)
			data = json.dumps(results)
			content_type = 'application/json'	
			return HttpResponse(data, content_type)
		else:
			movies = filter_movie(query)
			serializer = MovieSerializer(movies, many=True)
			return JSONResponse(serializer.data)
	return HttpResponse(status=404)

def find_movies(request):
	if request.method == 'POST':
		query = request.POST.get('term')	
		movies = filter_movie(query)	
		serializer = MovieSerializer(movies, many=True)
		results = []
		if len(query) == 0:
			return render(request, "index.html", {"query_string":"Please enter a search keyword"})
		for m in movies:
			loc = {}
			loc['address'] = m.locations
			loc['title'] = m.title
			loc['director'] = m.director
			loc['release_year'] = m.release_year
			results.append(loc)
		num_results = len(results)
		searchresult = 'You search for \'%s\'. Found %s result(s)' % (query, num_results)
		return render(request, "index.html", { "data" : serializer.data, "query_string":searchresult, "addresses" : json.dumps(results)})
	return HttpResponse(status=404)

def filter_movie(query):
	movies = Movie.objects.filter(Q(title__icontains = query) | Q(locations__icontains=query) | Q(production_company__icontains = query) | Q(director__icontains = query) | Q(writer__icontains = query) | Q(actor_1__icontains = query) | Q(actor_2__icontains = query) | Q(actor_3__icontains = query))
	return movies
