from faker import Factory
from models import Post, Comment
from django.contrib.auth.models import User
import json

fake = Factory.create()
with open('fixtures/fixtures.json', 'w') as fixture:

	eric = User(username = 'stonehengee', password = 'admin')
	json.dump(eric, fixture)

	for each in range(10):
		user = User(username = fake.user_name(*args, **kwargs), password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))
		json.dump(user, fixture)

	for each in range(10):
		post = Post(title = fake.text(max_nb_chars=40), content = fake.text(max_nb_chars=4000), user = Eric)
		json.dump(post, fixture)

	for each in range(10):
		comment = Comment(content = fake.text(max_nb_chars=2000), user = Eric)
		json.dump(comment, fixture)
