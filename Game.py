from Card import Card
from CardStack import CardStack
import turtle
from random import randrange

class Deck():
    def __init__(self):
        self.deck = CardStack()
        
    def populate_deck(self):
        for i in range(0, 10):
            self.deck.pushBack(Card(randrange(1, 11)))

# Creating window display
screen = turtle.Screen()
screen.title("Guessing Game")
screen.screensize(500, 500)
screen.setworldcoordinates(0, 0, 500, 500)
screen.bgcolor("light blue")

# Creating buttons
class Button(turtle.Turtle):
    def __init__(self, width, height, x, y, color):
        turtle.Turtle.__init__(self, shape = "square", visible=False)
        self.penup()
        self.setpos(x, y)
        self.turtlesize(stretch_wid = width, stretch_len = height, outline = None)
        self.color(color)
        self.showturtle()
        
start = Button(3, 4, 125, 125, "green")
end = Button(3, 4, 375, 125, "red")


                
            

deck = Deck()
deck.populate_deck()
deck.deck.print_stack()


# while True:


input()
            