from django.db import models
import random

class Deck(models.Model):
	title = models.CharField(max_length=128)
	
	def __str__(self):
		return self.title
	
	def get_first_card(self):
		'''Returns first card in card_set'''
		return self.card_set.first()
		
	def get_last_card(self):
		'''Returns last card in card_set'''
		return self.card_set.last()
	
	def get_random_card(self):
		'''Returns random card from deckset'''
		random_idx = random.randint(0, self.card_set.count() - 1)
		random_obj = self.card_set.all()[random_idx]
		return random_obj

class Card(models.Model):
	deckset = models.ForeignKey(Deck, null=True, blank=True)
	front = models.CharField(max_length = 300)
	back = models.CharField(max_length = 300)

	def __str__(self):
		return "{} , {}".format(self.front, self.back)
	
	def has_next_card(self):
		'''
		Returns False is card is the last card in the deck, true otherwise
		'''
		parent_deck = self.deckset
		last_card_in_deck = parent_deck.get_last_card()
		if self == last_card_in_deck:
			return False
		return True
	
	def has_prev_card(self):
		'''
		Returns False is card is the first card in the deck, false otherwise
		'''
		parent_deck = self.deckset
		first_card_in_deck = parent_deck.get_first_card()
		if self == first_card_in_deck:
			return False
		return True
		
	def get_next_card(self):
		'''
		Returns the following card using the first object in a filtered queryset
		'''
		return self.deckset.card_set.filter(id__gt=self.id).first()
		
	def get_prev_card(self):
		'''
		Returns the prev card using the last object in a filtered queryset
		'''
		return self.deckset.card_set.filter(id__lt=self.id).last()