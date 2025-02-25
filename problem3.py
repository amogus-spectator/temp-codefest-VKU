class WhitePlayer:
    def __init__(self, color_set, points, a,b):
        self.color_set = color_set
        self.points = points
        self.a = a
        self.b = b
        
    def calculate_points(self, opponent_color_set):
        total_pts = 0
        for i in self.color_set:
            if i not in opponent_color_set:
                total_pts += self.b
        
    def element_check_opponent(self, element, opponent_color_set):
        if not element in opponent_color_set:
            return True
        else:
            return False
    
    def calculate_pick(self, color_from_board, opponent_color_set):
        total_pts = 0
        if self.element_check_opponent(color_from_board, opponent_color_set):
            total_pts += self.a + self.calculate_points(opponent_color_set)
        return total_pts
        
    def pick(self, board_pieces_list,color_from_board, opponent_color_set):
        self.color_set.add(color_from_board)
        self.points += self.calculate_pick(color_from_board, opponent_color_set)
        board_pieces_list.remove(color_from_board)
class BlackPlayer:
    def __init__(self, color_set):
        self.color_set= color_set
    
    def element_check_opponent(element, opponent_color_set):
        if not element in opponent_color_set:
            return True
        else:
            return False
    def calculate_pick(self,board_pieces_list, color_from_board, opponent_color_set, opponent:WhitePlayer):
        pts = 0
        clone = board_pieces_list.copy()
        clone.remove(color_from_board)
        pts -= white_turn_best(self, board_pieces_list, opponent_color_set)[0]
        
    def pick(self, color_from_board, opponent_color_set, board_pieces_list):
        self.color_set.add(color_from_board)
        board_pieces_list.remove(color_from_board)
def processInput(org_input):
    result = [int(substring.strip()) for substring in org_input.split(' ')]
    return result

def white_turn_best(player:WhitePlayer, board_pieces_list, opponent_color_set):
    heatmap = []
    for i in range(len(board_pieces_list)):
        if player.element_check_opponent(board_pieces_list[i], opponent_color_set):
            player.calculate_pick(board_pieces_list[i], opponent_color_set)
            heatmap.append(player.points)
    max_pts = max(heatmap, default=0)
    return max_pts

def black_turn_best(player:BlackPlayer, board_pieces_list, opponent_color_set, opponent:WhitePlayer):
    heatmap = []
    for i in range(len(board_pieces_list)):
        heatmap.append(player.calculate_pick(board_pieces_list, board_pieces_list[i], opponent_color_set, opponent))
    min_pts = min(heatmap,default=0)
    return min_pts
def main():
    raw = input()
    raw_data = processInput(raw)
    number_of_pieces = raw_data[0]
    a = raw_data[1]
    b = raw_data[2]
    raw = input()
    raw_data = processInput(raw)
    color_list = raw_data
    color_set = set(raw_data)
    distinct_colors = list(color_set)
    
    white_player = WhitePlayer(color_set, 0, a, b)
    black_player = BlackPlayer(color_set)
    
    for i in range(number_of_pieces):
        if i % 2 == 0:
            white_player.points += white_turn_best(white_player, color_list, black_player.color_set)
        else:
            black_turn_best(black_player, color_list, white_player.color_set, white_player)

    print(white_player.points)
    
main()