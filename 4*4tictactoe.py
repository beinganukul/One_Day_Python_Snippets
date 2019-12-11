import os
os.system("clear")

class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print("%s | %s | %s | %s" %(self.cells[1],self.cells[2],self.cells[3],self.cells[4]))
        print("--------------")
        print("%s | %s | %s | %s" %(self.cells[5],self.cells[6],self.cells[7],self.cells[8]))
        print("--------------")
        print("%s | %s | %s | %s" %(self.cells[9],self.cells[10],self.cells[11],self.cells[12]))
        print("--------------")
        print("%s | %s | %s | %s" %(self.cells[13],self.cells[14],self.cells[15],self.cells[16]))



    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player  
    def is_winner(self,player):
        for combo in [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16],[1,6,11,16],[4,7,10,13]]:
            result = True
            for cell_no in combo:
                if self.cells[cell_no] != player:
                    result = False    

            if result == True:
                return True        

    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells +=1
        if used_cells == 16:
            return True
        else:
            return False        

    def  reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

board = Board()

def print_header():
    print ("Welcome to TIC-TAC-TOE\n")

def refresh_screen():
    #clears screen
    os.system("clear")

    #print header
    print_header()

    #show the board
    board.display()

while True:
    refresh_screen()

    #>Get X input
    x_choice = int(input("\nX) Please choose 1-16.>"))

    #update board
    board.update_cell(x_choice, "X") 

    #refresh screen
    refresh_screen()

    #check for X win
    if board.is_winner("X"):
        print ("\nX wins.")
        play_again = input("Would you like to play again? (Y/N) >")
        if play_again == "Y":
            board.reset()
            continue
        else:
            break   

    #check for a tie
    if board.is_tie():
        print ("\nA Tie!!!")
        play_again = input("Would you like to play again? (Y/N) >")
        if play_again == "Y":
            board.reset()
            continue
        else:
            break    


    #check for O win
    if board.is_winner("O"):
        print ("\nO wins.")
        play_again = input("Would you like to play again? (Y/N) >")
        if play_again == "Y":
            board.reset()
            continue
        else:
            break    

    #check for a tie
    if board.is_tie():
        print ("\nA Tie!!!")
        play_again = input("Would you like to play again? (Y/N) >")
        if play_again == "Y":
            board.reset()
            continue
        else:
            break    


    #>Get O input
    o_choice = int(input("\nO) Please choose 1-16.>"))

    #update board
    board.update_cell(o_choice, "O") 
