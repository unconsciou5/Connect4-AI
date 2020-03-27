import numpy as np

class game:
    ###
    ### Konstruktor für Game-Klasse
    ###
    def __init__(
            self,
            board_width=6,
            board_height=7
            ):
        self.board_width = board_width
        self.board_height = board_height
        self.board = np.zeros((board_height,board_width))
        print(self.board)
        print(" ")
        
    ###
    ### Zug Funktion
    ###
    def playeraction(
            self,
            player_id,
            column
            ):
        if (column >self.board_width):
            return False
        
        for i in reversed( range(self.board_height)):
            if self.board[i,column] == 0:
                self.board[i,column] = player_id
                return (True, self.check_win(player_id, x=column, y=i))

        return False
        
    ###
    ### Zeigt das Spielfeld an
    ###
    def display(self):
        print(self.board)
        print(" ")
    ###
    ### Prüft ob ein Zug zu einem Sieg geführt hat
    ###
    def check_win(
            self,
            player_id,
            x,
            y
            ):
        sum_x = 1
        sum_y = 1
        sum_dp = 1
        sum_dn = 1
        
        # row checking
        for ix in range(1,4):
            if (x+ix) > self.board_width-1:
                # print("out of board")
                break
            if self.board[y,x+ix] == player_id:
                sum_x +=1
            else: 
                # print("zero on the right")
                break
            
        for ix in range(1,4):
            if (x-ix) < 0:
                # print("out of board")
                break
            if self.board[y,x-ix] == player_id:
                sum_x +=1
            else: 
                # print("zero on the left")
                break
        if sum_x >= 4:
            return True
        
        # column checking
        for iy in range(1,4):
            if (y+iy) > self.board_height-1:
                # print("out of board")
                break
            if self.board[y+iy,x] == player_id:
                sum_y +=1
            else: 
                # print("zero on the bottom")
                break
            
        for iy in range(1,4):
            if (y-iy) < 0:
                # print("out of board")
                break
            if self.board[y-iy,x] == player_id:
                sum_y +=1
            else: 
                # print("zero on the top")
                break
        if sum_y >= 4:
            return True
        
        # pos diagonal checking
        # right
        for i in range(1,4):
            if (y-i) < 0 or (x+i) > self.board_width-1:
                # print("out of board dp right")
                break
            if self.board[y-i,x+i] == player_id:
                sum_dp +=1
            else: 
                # print("zero on the dp right")
                break
        # left
        for i in range(1,4):
            if (y+i) > self.board_height-1 or (x-i) < 0:
                # print("out of board dp left")
                break
            if self.board[y+i,x-i] == player_id:
                sum_dp +=1
            else: 
                # print("zero on the dp left")
                break
            
        if sum_dp >= 4:
            return True
        
        # neg diagonal checking
        # right
        for i in range(1,4):
            if (y+i) > self.board_height-1 or (x+i) > self.board_width-1:
                # print("out of board dn right")
                break
            if self.board[y+i,x+i] == player_id:
                sum_dn +=1
            else: 
                # print("zero on the dn right")
                break
        # left
        for i in range(1,4):
            if (y-i) < 0 or (x-i) < 0:
                # print("out of board dn left")
                break
            if self.board[y-i,x-i] == player_id:
                sum_dn +=1
            else: 
                # print("zero on the dn left")
                break

        if sum_dn >= 4:
            return True