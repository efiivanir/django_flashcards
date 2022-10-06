from cards.models import Card
c1 = Card(question="Hello", answer="Hola")
c1.save()
c2 = Card(question="Please", answer="Por favor")
c2.save()
c3 = Card(question="Sorry", answer="Lo siento", box=2)
c3.save()
