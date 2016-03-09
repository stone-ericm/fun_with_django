from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=40)
	content = models.CharField(max_length=4000)
	slug = models.SlugField(max_length=40)
	created_at = models.DateTimeField(editable=False)
	updated_at = models.DateTimeField()
	user = models.ForeignKey(
		User,
		null = True,
		default = None,
		on_delete = models.SET_DEFAULT
	)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		self.updated_at = timezone.now()
		if not self.id:
			self.created_at = timezone.now()
		super(Post, self).save(*args, **kwargs)

	def update_check(self):
		if self.updated_at.minute == self.created_at.minute and self.updated_at.hour == self.created_at.hour and self.updated_at.day == self.created_at.day:
					return False
		else:
			return True


	def to_json(self):
		return {
			'title': self.title,
			'content': self.content,
			'slug': self.slug,
			'created_at': self.created_at,
			'updated_at': self.updated_at,
			'user': self.user,
		}

class Comment(models.Model):
	content = models.CharField(max_length=2000)
	created_at = models.DateTimeField(editable=False)
	updated_at = models.DateTimeField()
	user = models.ForeignKey(
		User,
		null = True,
		default = None,
		on_delete = models.SET_DEFAULT
	)

	def save(self, *args, **kwargs):
		self.updated_at = timezone.now()
		if not self.id:
			self.created_at = timezone.now()
		super(Comments, self).save(*args, **kwargs)