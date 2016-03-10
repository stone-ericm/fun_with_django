from faker import Factory
from hacker.models import Post, Comment
from django.contrib.auth.models import User
import json

def seed_from_faker():
	fake = Factory.create()
	eric = User(username = 'stonehengee', password = 'Newamsterdam')
	eric.save()

	for each in range(10):
		user = User(username = fake.user_name(), password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))
		user.save()

	for each in range(10):
		post = Post(title = fake.text(max_nb_chars=40), content = fake.text(max_nb_chars=4000), user = eric)
		post.save()

	for each in range(10):
		comment = Comment(content = fake.text(max_nb_chars=2000), user = eric)
		comment.save()