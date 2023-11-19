from comic_bar import ComicBarLevel

class ComicTrick(ComicBarLevel):
    def __init__(self) -> None:
        super().__init__()
        self.respect = 0
        self.laziness = 0
        self.has_food = False
    
    def do_trick(self, trick):
        if self.has_food:
            return f"Comic does the trick gladly: {trick}"
        elif self.respect <= 40 and self.laziness >= 20:
            amount = self.__getbar__ * 0.20
            self.__decrementbar__(amount)
            return "Comic refuses to do trick and just stares at you \
                as if he is saying how dare you hooman try to command me when I own you"
        elif self.respect > 40 and self.laziness >= 20:
           return "Comic does the trick with half effort in the most lazy way you have seen!"
        elif self.respect > 40 and self.laziness < 20 and self.__getbar__ > 80:
            return "Comic does the trick with full effort despite no treat being offered at first, he woofs you that much!"