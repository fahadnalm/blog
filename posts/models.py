# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail",kwargs={"post_id": self.id}) # reverse gives me the url that I mention "detail"

	class Meta:
		ordering = ['title'] # order th list by title