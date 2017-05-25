from django.forms import ModelForm
from .models import Card

class CardForm(ModelForm):
	"""
	Form to enter front and back info
	"""
	class Meta:
		model = Card
		fields = ['deckset', 'front', 'back']