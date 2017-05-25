from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Card, Deck
from .forms import CardForm

def deckList(request):
	"""
	Gets all Card objects and renders a list with front and back attribute information
	"""
	decks = Deck.objects.all( )
	context = {'decks': decks}
	return render(request, 'flashcards/decklist.html', context)

def viewCard(request, deck_id):
	'''
	Queries database for card_id from deck_id
	'''
	deck = get_object_or_404(Deck, id=deck_id)
	card_list = deck.card_set.all()
	card = card_list.first()
	if request.method == 'GET' and 'card' in request.GET:
		card = get_object_or_404(Card, id=int(request.GET['card']))
	return render(request, 'flashcards/viewCard.html', {'card':card, 'deck':deck})
	
def addCard(request):
	'''
	Renders a form allowing a user to create a card
	'''
	if request.method == 'POST':
		# create form instance and populate with data from request (what was submitted)
		form = CardForm(request.POST)
		# check if form is valid
		if form.is_valid( ):
			# save form's data to the database
			form.save( )
			# clear the form
			form = CardForm( )
	# if this is a GET or any other method (e.g., first request to create new card) 
	# create default form instance
	else:
		form = CardForm( )
	context = {'form': form}
	return render(request, 'flashcards/addOrEditCard.html', context)
	
def editCard(request, card_id):
	'''
	Renders a form allowing a user to edit a card
	'''
	card = get_object_or_404(Card, id=card_id)
	if request.method == 'POST':
		form = CardForm(request.POST, instance=card)
		if form.is_valid( ):
			form.save( )
			form = CardForm( )
	else:
		form = CardForm(instance=card)
	context = {'form': form, 'editing':True, 'card':card}
	return render(request, 'flashcards/addOrEditCard.html', context)

def deleteCard(request, card_id):
	card = get_object_or_404(Card, id=card_id)
	card.delete()
	return HttpResponseRedirect('/')