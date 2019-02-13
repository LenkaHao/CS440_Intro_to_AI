# cs440 Programming Assignment 3
# Atropos Game Playing
# Jiatong Hao   U42186937
# Xianhui Li   U16207086
# April 25, 2018

import sys
import copy
# print to stderr for debugging purposes
# remove all debugging statements before submitting your code
msg = "Given board " + sys.argv[1] + "\n"
#sys.stderr.write(msg)

# A node of an n-ary tree that stores the static evaluators
class Node :
    def __init__(self, value):
        self.value = value
        self.child = []

#Function to print a tree
def printTree(root):
    if root is None:
        return 
    
    sys.stderr.write(str(root.value))
    sys.stderr.write(" ") # Seperator between levels
    queue = []
    for i in range(len(root.child)):
        sys.stderr.write(str(root.child[i].value) + " ")
        subQueue = []
        for j in range(len(root.child[i].child)):
            subQueue.append(root.child[i].child[j].value)
        queue.append(subQueue)
    sys.stderr.write(" ") # Seperator between levels
    for i in range(len(queue)):
        sys.stderr.write("||")
        for j in range(len(queue[i])):
            sys.stderr.write(str(queue[i][j])+ " ")

#covert move = [color, height, left, right] into move_str
def move_to_string(move):
    move_str = "(" + str(move[0]) + "," + str(move[1]) + "," + str(move[2]) + "," + str(move[3]) + ")"
    sys.stderr.write(move_str)
    return move_str


#convert move = [color, height, left, right] into position in board = [row1, row2, ...]
#returns a list: [row, col]
def move_to_boardpos(move):
    row = -move[1]-1
    col = move[2]
    board_pos = [row, col]
    return board_pos


#converts a board_pos to a move
#board_pos = [i, j]
def boardpos_to_move(board_pos, board):
    move = [0]
    move.append(len(board) - board_pos[0] - 1)
    move.append(board_pos[1])
    move.append(len(board[board_pos[0]]) - board_pos[1] - 1)
    return move


#if the last move is null, we need to go first
def goFirst(board):
    if (len(board) % 2 != 0):
        height = len(board) // 2
    else:
        height = len(board) // 2 - 1
    row_index = len(board) - height - 1
    width = len(board[row_index])
    left = width // 2
    right = width - left - 1
    move1 = [1, height, left, right]
    move2 = [2, height, left, right]
    move3 = [3, height, left, right]
    moves = []
    moves.append(move1)
    moves.append(move2)
    moves.append(move3)
    #our_possible_moves
    return moves

#get the color at a position defined by move[], color is an int
def color_at_boardpos(board, move):
    board_pos = move_to_boardpos(move)
    color = board[board_pos[0]][board_pos[1]]
    return color


#find all empty spots on a board, returns a list of moves with color 0
def empty_spots(board):
    empty_spots = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            board_pos = [i, j]
            move = boardpos_to_move(board_pos, board)
            if color_at_boardpos(board, move) == 0:
                empty_spots.append(move)
    return empty_spots


#get the six neighbors of a move
def find_neighbors(board, move):
    topleft = [0, move[1]+1, move[2]-1, move[3]]
    topright = [0, move[1]+1, move[2], move[3]-1]
    left = [0, move[1], move[2]-1, move[3]+1]
    right = [0, move[1], move[2]+1, move[3]-1]
    if (move[1] == 1):
        bottomleft = [0, move[1]-1, move[2]-1, move[3]]
        bottomright = [0, move[1]-1, move[2], move[3]-1]
    else:
        bottomleft = [0, move[1]-1, move[2], move[3]+1]
        bottomright = [0, move[1]-1, move[2]+1, move[3]]

    all_neighbors = [topleft, topright, left, right, bottomleft, bottomright]
    return all_neighbors

#find all empty spot around a move
#neighbors is a list of list
def empty_neighbors(board, neighbors):
    empty_move = []
    for i in range(6):
        if color_at_boardpos(board, neighbors[i]) == 0:
            empty_move.append(neighbors[i])
        #sys.stderr.write("bottomright is empty")
    #sys.stderr.write(str(empty_move))
    return empty_move

#change the color into move[0] 
def draw_on_board(board, move):
    next_board = copy.deepcopy(board)
    #get board_position
    board_pos = move_to_boardpos(move)
    next_board[board_pos[0]][board_pos[1]] = move[0]
    return next_board

#check if this move will cause to lose the game
def will_lose(board, move):
    #get the color of neighbors of move
    current_color = color_at_boardpos(board, move)
    neighbors = find_neighbors(board, move)
    colors = []
    for i in range(6):
        color = color_at_boardpos(board, neighbors[i])
        colors.append(color)
    #sys.stderr.write("\n colors: " + str(colors))
    #check each triangle
    #upper-left triangle
    lose = False
    if (colors[0] != 0) and (colors[2] != 0):
        if (colors[0] != colors[2]) and (colors[0] != current_color) and (colors[2] != current_color):
            lose = True
            return lose
    #upper-right triangle
    if (colors[1] != 0) and (colors[3] != 0):
        if (colors[1] != colors[3]) and (colors[1] != current_color) and (colors[3] != current_color):
            lose = True
            return lose
    #lower-left triangle
    if (colors[2] != 0) and (colors[4] != 0):
        if (colors[2] != colors[4]) and (colors[2] != current_color) and (colors[4] != current_color):
            lose = True
            return lose
    #lower-right triangle
    if (colors[3] != 0) and (colors[5] != 0):
        if (colors[3] != colors[5]) and (colors[3] != current_color) and (colors[5] != current_color):
            lose = True
            return lose
    #upper triangle
    if (colors[0] != 0) and (colors[1] != 0):
        if (colors[0] != colors[1]) and (colors[0] != current_color) and (colors[1] != current_color):
            lose = True
            return lose
    #lower triangle
    if (colors[4] != 0) and (colors[5] != 0):
        if (colors[4] != colors[5]) and (colors[4] != current_color) and (colors[5] != current_color):
            lose = True
            return lose
    return lose

#count the number of different colored neighboring pairs
def different_color_pair(board, move):
    neighbors = find_neighbors(board, move)
    count = 0
    colors = []
    for i in range(6):
        color = color_at_boardpos(board, neighbors[i])
        colors.append(color)
    if (colors[0] != 0) and (colors[1] != 0) and (colors[0] != colors[1]):
        count += 1
    if (colors[1] != 0) and (colors[3] != 0) and (colors[1] != colors[3]):
        count += 1
    if (colors[3] != 0) and (colors[5] != 0) and (colors[3] != colors[5]):
        count += 1
    if (colors[5] != 0) and (colors[4] != 0) and (colors[5] != colors[4]):
        count += 1
    if (colors[4] != 0) and (colors[2] != 0) and (colors[4] != colors[2]):
        count += 1
    if (colors[2] != 0) and (colors[0] != 0) and (colors[2] != colors[0]):
        count += 1
    return count * 2

#count how many neighbors has the same color as the opponent's move
def same_color_neighbor(board, move):
    #get the color of all neighbors
    neighbors = find_neighbors(board, move)
    count = 0
    colors = []
    for i in range(6):
        color = color_at_boardpos(board, neighbors[i])
        colors.append(color)
    for i in range(6):
        if colors[i] != 0:
            if (move[0] == colors[i]):
                count -= 1
    return count


#assign scores to this move according to its surroundings
#since we are looking two steps away, the static evalution is always for the opponent's situation
def static_eval(board, move):
    #if the opponent will lose, high score
    score = 0
    if (will_lose(board, move)):
        score += 10

    #if there are few empty places, high score
    neighbors = find_neighbors(board, move)
    if len(empty_neighbors(board, neighbors))<2:
            score += 10

    #if there are so many empty places, high score
    if len(empty_neighbors(board, neighbors))>4:
            score += 10

    #if different color pairs for the opponent, high score
    different_pairs = different_color_pair(board, move)
    score += different_pairs
    
    #if opponent's move has the same color as its neighbor, low score
    score += same_color_neighbor(board, move)
    return score

def best_average(node):
    best_average = -100
    index = -1
    for i in range(len(node.child)):
        level_sum = 0
        num_child = 0
        for j in range(len(node.child[i].child)):
            level_sum += node.child[i].child[j].value
            num_child += 1
        level_average = level_sum / num_child
        if level_average > best_average:
            best_average = level_average
            index = i
    return [best_average, index]

#Minimax with alpha-beta pruning
def minimax(node, depth, alpha, beta, isMaximizer):
    index = [-1, -1]
    if (depth == 0) or (node.child is None):
        return node.value
    if (isMaximizer):
        node.value = -1000
        for i in range(len(node.child)):
        #for aChild in node.child:
            next_value = minimax(node.child[i], depth-1, alpha, beta, False)[0]
            if (next_value > node.value):
                node.value = next_value
                index[0] = i
            alpha = max(alpha, node.value)
            if (beta <= alpha):
                break
        return [node.value, index]
    else:
        node.value = 1000
        for i in range(len(node.child)):
            node.value = min(node.value, minimax(node.child[i], depth-1, alpha, beta, True))
            beta = min(beta, node.value)
            if (beta <= alpha):
                break
        return [node.value, index]


our_possible_moves = []
next_boards = []
#parse the input string, i.e., argv[1]
#board = [row1, row2, ...], lastmove = [color, height, left, right]
#get board as a list from input
board_start = msg.find("[")
board_end = msg.find("L")
board_string = msg[board_start:board_end]
lastboard = []
for i in range(len(board_string)):
    if (board_string[i] == "["):
        board_row = []
    elif (board_string[i] == "]"):
        lastboard.append(board_row)
    else:
        board_row.append(int(board_string[i]))
#sys.stderr.write(str(board))
#get the last move of opponent
lastmove_start = msg.find("(")
#if the last move is null, we need to go first
if lastmove_start == -1:
    sys.stderr.write("We go first")
    our_possible_moves = goFirst(lastboard)
#get the last move of opponent as a list from input
else:
    lastmove_start += 1
    lastmove_string = msg[lastmove_start:-2]
    sys.stderr.write(lastmove_string)
    lastmove = [int(s) for s in lastmove_string.split(',')]

    #needs to look two steps forward, one for ourselves, one for the opponent

    #get all possible steps for ourselves
    #find all empty neighbors
    lastmove_empty_neighbors = empty_neighbors(lastboard, find_neighbors(lastboard, lastmove))
    #if there is any empty neighbors, we get all possible next steps
    if (len(lastmove_empty_neighbors) > 0):
        #sys.stderr.write("\n" + str(lastmove_empty_neighbors))
        for i in range(len(lastmove_empty_neighbors)):
            for j in range(3):
                our_possible_moves.append([j+1, lastmove_empty_neighbors[i][1], lastmove_empty_neighbors[i][2], lastmove_empty_neighbors[i][3]])
        #sys.stderr.write("our_possible_moves: " + str(our_possible_moves) + "\n")
    #find a empty spot to start over
    else:
        empty_spots = empty_spots(lastboard)
        for i in range(len(empty_spots)):
            for j in range(3):
                our_possible_moves.append([j+1, empty_spots[i][1], empty_spots[i][2], empty_spots[i][3]])

        sys.stderr.write("Need to pick a random spot")


#remove all moves that will lose in our_possible_moves
#record the board situation after that step
lose_move = []
lose_board = []
for i in range(len(our_possible_moves)):
    next_board = draw_on_board(lastboard, our_possible_moves[i])
    #sys.stderr.write(str(next_board))
    next_boards.append(next_board)
    if (will_lose(next_board, our_possible_moves[i])):
        lose_move.append(our_possible_moves[i])
        lose_board.append(next_board)
for i in range(len(lose_move)):
    #sys.stderr.write("remove: " + str(lose_move[i]))
    our_possible_moves.remove(lose_move[i])
    next_boards.remove(lose_board[i])
#for i in range(len(our_possible_moves)):
    #sys.stderr.write("our move " + str(i) + ": " + str(our_possible_moves[i]) + "\n")
    #sys.stderr.write("result board " + str(i) + ": " + str(next_boards[i]) + "\n")
#now our_possible_moves contains all possible moves for the next step

#get the possible moves of the opponent at the next, next step
#if not possible moves for ourselves, we lose, just pick a random position
if (len(our_possible_moves) == 0):
    sys.stderr.write("We lose :(")
    sys.stdout.write("(3,2,2,1)")
#get the possible moves of the opponent at the next, next step
#opponent_moves = [[moves[0], move[3], next_board]]
else: 
    all_possible_opponent = []
    for i in range(len(our_possible_moves)):
        ourmove_empty_neighbors = empty_neighbors(next_boards[i], find_neighbors(next_boards[i], our_possible_moves[i]))
        #if there are empty spots for the opponent, predict his moves
        if (len(ourmove_empty_neighbors) > 0):
            one_possible_opponent = []
            #get all possible moves of the opponent
            opponent_possible_moves = []
            opponent_boards = []
            for j in range(len(ourmove_empty_neighbors)):
                for k in range(3):
                    opponent_possible_moves.append([k+1, ourmove_empty_neighbors[j][1], ourmove_empty_neighbors[j][2], ourmove_empty_neighbors[j][3]])
            one_possible_opponent.append(opponent_possible_moves)
            #get the board situation after each possible moves of the opponent
            for j in range(len(opponent_possible_moves)):
                next_oppo_board = draw_on_board(next_boards[i], opponent_possible_moves[j])
                opponent_boards.append(next_oppo_board)
            one_possible_opponent.append(opponent_boards)
            #sys.stderr.write("one_possible_opponent for our move: " +  str(i) + str(one_possible_opponent) + "\n")
            all_possible_opponent.append(one_possible_opponent)
        #else it means that no empty neighbor for the opponent
        else:
            #sys.stderr.write("No possible moves for the opponent")
            all_possible_opponent.append(["no move"])
    #a move: all_possible_opponet[i][0][j] <-> a board: all_possible_opponent[i][1][j]


    #compute static score for each all_possible_opponent
    score_tree = Node(0)
    for i in range(len(all_possible_opponent)):
        score_tree.child.append(Node(0))
        #if the opponent has possible moves, evaluate the situation
        if (all_possible_opponent[i] != ["no move"]):
            for j in range(len(all_possible_opponent[i][0])):
                #sys.stderr.write("opponent possible move for our move " + str(i) + str(all_possible_opponent[i][0][j]) + "\n")
                #sys.stderr.write("opponent possible board for our move " + str(i) + str(all_possible_opponent[i][1][j]) + "\n")
                #after we move, if the opponent has only one possible move and that leads to losing, we take that step
                if (len(all_possible_opponent[i][0]) == 1) and will_lose(all_possible_opponent[i][1][0], all_possible_opponent[i][0][0]):
                    best_move = our_possible_moves[i]
                    best_move_string = move_to_string(best_move)
                    sys.stdout.write(best_move_string)
                else:
                    score = static_eval(all_possible_opponent[i][1][j], all_possible_opponent[i][0][j])
                    if (len(all_possible_opponent[i][0]) <= 3):
                        score += 3
                    score_tree.child[i].child.append(Node(score))
        #else means the opponent needs to finds an empty space, give a score of zero
        else:
            sys.stderr.write("no move")
            score = 0
            score_tree.child[i].child.append(Node(score))
    #printTree(score_tree)
    #best_outcome = [best_score, [index[0], index[1]]]
    best_outcome = minimax(score_tree, 2, -1000, +1000, True)
    best_move_index = best_outcome[1][0]
    #best_outcome = best_average(score_tree)
    #best_move_index = best_outcome[1]
    best_move = our_possible_moves[best_move_index]
    best_move_string = move_to_string(best_move)
    sys.stdout.write(best_move_string)


