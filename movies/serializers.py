from django.forms import widgets
from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = ('id', 'title', 'release_year', 'locations', 'fun_facts', 'production_company', 'distributor', 'director', 'writer', 'actor_1', 'actor_2', 'actor_3')

