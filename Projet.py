from tkinter import*

#Mes classes
class Pion:
    def __init__(self, joueur, coordonne):
        self.joueur = joueur
        self.coordone = coordonne
class Jeu:
    def __init__(self, fenetre, dimension= 10, nb_poins=5):
        self.fenetre = fenetre
        self.dimension = dimension
        self.nb_poins = nb_poins
        self.joueurs = ['Player1', 'Player2']
        self.current_player = 0
        self.poinJoueur1 = []
        self.poinJoueur2 = []
        self.plateau = [[' ' for _ in range(dimension)] for _ in range(dimension)]
        
        self.canvas = Canvas(self.fenetre, width=50*self.dimension, height=50*self.dimension)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.click_handler)

        self.plateau_jeu()
        self.affiche_CurrentPlayer()
    #Afficher le Joueur courant
    def affiche_CurrentPlayer(self):
        textAffiche = f"{self.joueurs[self.current_player]}"
        self.fenetre.title(textAffiche)
        
    #Afficher le plateau
    def plateau_jeu(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.canvas.create_rectangle(j*50, i*50, (j+1)*50, (i+1)*50, outline="black")
                if (i, j) in self.poinJoueur1:
                    self.canvas.create_oval(j*50+10, i*50+10, (j+1)*50-10, (i+1)*50-10, outline='blue', width=2)
                elif (i, j) in self.poinJoueur2:
                    self.canvas.create_oval(j*50+10, i*50+10, (j+1)*50-10, (i+1)*50-10, outline='red', width=2)
                if self.plateau[i][j] == 'X':
                    self.marquer_case(i, j)
                      
    def click_handler(self, event):
        row, col = event.y // 50, event.x // 50
        if self.plateau[row][col] == ' ':
            if self.current_player == 0:
                self.choose_case(row, col, self.poinJoueur1)
            else:
                self.choose_case(row, col, self.poinJoueur2)
        self.current_player = (self.current_player + 1) % 2
        self.affiche_CurrentPlayer()

                
    def choose_case(self, row, col, joueur_poins):
        if joueur_poins:
            last_row, last_col = joueur_poins[-1]
            self.plateau[last_row][last_col] = 'X'
            self.marquer_case(last_row, last_col)
        joueur_poins.append((row, col))
        self.plateau[row][col] = 'O'
        self.plateau_jeu()
        
    def marquer_case(self, row, col):
        color = 'blue' if self.current_player == 0 else 'red'
        self.canvas.create_line(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, fill=color, width=2)
        self.canvas.create_line(col*50+10, (row+1)*50-10, (col+1)*50-10, row*50+10, fill=color, width=2)

        
def main():
    fenetre = Tk()
    fenetre.title("Jeu Python")
    dimension = 10
    nb_poins = 5
    game = Jeu(fenetre, dimension, nb_poins)
    
    fenetre.mainloop()
    
if __name__ =="__main__":
    main()