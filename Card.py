class Card:
    def __init__(self, value=None):
        self.value = value

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

# Testing
if __name__ == "__main__":
    card1 = Card(4)
    print(card1.getValue())

    card2 = Card()
    print(card2.getValue())
    card2.setValue(2)
    print(card2.getValue())
