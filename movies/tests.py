from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from movies.models import Movie

# Create your tests here.
class MovieTests(APITestCase):
	def test_get(self):
		"""
		Make sure simple GET request returns a JSON
		"""
		response = self.client.get('/movies/search/', {'term' : 'blah'})
		self.assertIsNotNone(response)
	def test_post(self):
		"""
		Make sure a POST request to search page results in a 404
		"""
		response = self.client.post('/movies/search/', { 'term' : 'new'})
		self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
	def test_find(self):
		"""
		Make sure a form submit POST for ./find returns correct results
		"""
		movie = Movie.objects.create(title = 'testmovie', release_year=2014)
		response = self.client.post('/movies/find', {'term' : 'test' })
		self.assertIsNotNone(response.context['data'])
		self.assertTrue(len(response.context['data']) > 0)
		response = self.client.post('/movies/find', {'term' : 'blah' })
		self.assertIsNotNone(response.context['data'])
		self.assertTrue(len(response.context['data']) == 0) #should not find any movies
		
