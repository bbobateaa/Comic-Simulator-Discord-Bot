class ComicBarLevel():
    def __init__(self) -> None:
        self.bar = 50

    def __getbar__(self):
        return self.bar
    
    def __setbar__(self, amount):
        self.bar = amount
    
    def __incrementbar__(self, amount):
        self.bar += amount

    def __decrementbar__(self, amount):
        self.bar -= amount
    