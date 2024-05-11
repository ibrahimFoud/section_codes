class PlayerMemento :
    def __init__(self , name , score ):
        self.name = name
        self.score = score

class Player :
    def __init__(self , name , score ):
        self.name = name
        self.score = score 

    def display_state(self ):
        print("Name : " , self.name)
        print("Score : " , self.score)
    
    def update_score(self , new_score):
        self.score = new_score

    def save_state(self ):
        return PlayerMemento(self.name , self.score)

    def undo (self , memento):
        self.name = memento.name
        self.score = memento.score


if __name__ == "__main__":
    player1 = Player("ibrahim" , 0)

    player1.update_score(50)
    player1.display_state()

    saved = player1.save_state()

    player1.update_score(60)
    player1.display_state()
    


    player1.undo(saved)
    player1.display_state()





