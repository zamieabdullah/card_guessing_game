from Card import Card

class Node:
    def __init__(self, card=None, next=None):
        self.card = card
        self.next = next

class CardStack:
    def __init__(self):
        self.node = None
        self.length = 0

    def getLength(self):
        return self.length

    def pushBack(self, card):
        if self.node == None:
            self.node = Node(card)
        else:
            temp = self.node

            while temp.next != None:
                temp = temp.next

            temp.next = Node(card)

        self.length+=1

    def print_stack(self):
        print("Stack length:", self.getLength())
        temp = self.node
        print("Cards on Stack")
        while temp != None:
            print(temp.card.getValue());
            temp = temp.next


# Testing
if __name__ == "__main__":
    deck = CardStack()

    deck.pushBack(Card(4))
    deck.pushBack(Card(5))
    deck.pushBack(Card(6))
    deck.print_stack()
