from django.test import TestCase
from .models import Card, Deck

class DeckTestCases(TestCase):
    deck = None
    card1 = None
    card2 = None
    card3 = None
    
    def setUp(self):
        self.deck = Deck.objects.create(title='test_deck_1')
        self.card1 = Card.objects.create(
                                front = 'Front of Card1',
                                back = 'Back of Card1',
                                deckset = self.deck
                            )
        self.card2 = Card.objects.create(
                                front = 'Front of Card2',
                                back = 'Back of Card2',
                                deckset = self.deck
                            )
        self.card3 = Card.objects.create(
                                front = 'Front of Card3',
                                back = 'Back of Card3',
                                deckset = self.deck
                            )
                            
    def test_starting_conditions(self):
        '''Check deck and cards exist'''
        self.assertIsInstance(self.deck, Deck)
        self.assertIsInstance(self.card1, Card)
        self.assertEqual('Front of Card1', self.card1.front)
        self.assertEqual('Back of Card1', self.card1.back)
        self.assertEqual(self.deck, self.card1.deckset)
        self.assertIsInstance(self.card2, Card)
        self.assertEqual('Front of Card2', self.card2.front)
        self.assertEqual('Back of Card2', self.card2.back)
        self.assertEqual(self.deck, self.card2.deckset)
        self.assertIsInstance(self.card3, Card)
        self.assertEqual('Front of Card3', self.card3.front)
        self.assertEqual('Back of Card3', self.card3.back)
        self.assertEqual(self.deck, self.card3.deckset)
        
    def test_get_first_card(self):
        self.assertEqual(self.card1, self.deck.get_first_card())
        self.assertNotEqual(self.card2, self.deck.get_first_card())
        self.assertNotEqual(self.card3, self.deck.get_first_card())
    
    def test_get_last_card(self):
        self.assertEqual(self.card3, self.deck.get_last_card())
        self.assertNotEqual(self.card2, self.deck.get_last_card())
        self.assertNotEqual(self.card1, self.deck.get_last_card())
        
    def test_get_random_card(self):
        '''
        Calls deck.get_random_card 100 and ensures it returns a valid card each time
        '''
        for _ in range(100):
            self.assertIn(self.deck.get_random_card(), [self.card1, self.card2, self.card3])

class CardTestCases(TestCase):
    deck = None
    card1 = None
    card2 = None
    card3 = None
    
    def setUp(self):
        self.deck = Deck.objects.create(title='test_deck_1')
        self.card1 = Card.objects.create(
                                front = 'Front of Card1',
                                back = 'Back of Card1',
                                deckset = self.deck
                            )
        self.card2 = Card.objects.create(
                                front = 'Front of Card2',
                                back = 'Back of Card2',
                                deckset = self.deck
                            )
        self.card3 = Card.objects.create(
                                front = 'Front of Card3',
                                back = 'Back of Card3',
                                deckset = self.deck
                            )
                            
    def test_starting_conditions(self):
        '''Check deck and cards exist'''
        self.assertIsInstance(self.deck, Deck)
        self.assertIsInstance(self.card1, Card)
        self.assertEqual('Front of Card1', self.card1.front)
        self.assertEqual('Back of Card1', self.card1.back)
        self.assertEqual(self.deck, self.card1.deckset)
        self.assertIsInstance(self.card2, Card)
        self.assertEqual('Front of Card2', self.card2.front)
        self.assertEqual('Back of Card2', self.card2.back)
        self.assertEqual(self.deck, self.card2.deckset)
        self.assertIsInstance(self.card3, Card)
        self.assertEqual('Front of Card3', self.card3.front)
        self.assertEqual('Back of Card3', self.card3.back)
        self.assertEqual(self.deck, self.card3.deckset)
        
    def test_has_prev_card(self):
        self.assertFalse(self.card1.has_prev_card())
        self.assertTrue(self.card2.has_prev_card())
        self.assertTrue(self.card3.has_prev_card())
        
    def test_has_next_card(self):
        self.assertFalse(self.card3.has_next_card())
        self.assertTrue(self.card2.has_next_card())
        self.assertTrue(self.card1.has_next_card())
        
    def test_get_next_card(self):
        self.assertEqual(self.card2, self.card1.get_next_card())
        self.assertEqual(self.card3, self.card2.get_next_card())
        self.assertIsNone(self.card3.get_next_card())
        
    def test_get_prev_card(self):
        self.assertEqual(self.card2, self.card3.get_prev_card())
        self.assertEqual(self.card1, self.card2.get_prev_card())
        self.assertIsNone(self.card1.get_prev_card())