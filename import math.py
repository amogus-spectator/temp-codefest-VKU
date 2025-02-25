import numpy as np

class Rare:
    def __init__(self, v_i, w_i, a_i, b_i, p_i):
        self.v_i = v_i
        self.w_i = w_i
        self.a_i = a_i
        self.b_i = b_i
        self.p_i = p_i

    def a_i_check(self):
        if self.a_i > 0:
            return 1
        else:
            return 0

    def value(self):
        return self.v_i * self.p_i - self.a_i * self.p_i * self.p_i + self.b_i * self.a_i_check()

class Player:
    def __init__(self,  max_weight, rare_amount_heatmap, rare_list:list[Rare],rare_value_round_turn:list):
        self.rare_amount_heatmap = rare_amount_heatmap
        self.max_weight = max_weight
        self.rare_list = rare_list
        self.rare_value_round_turn = rare_value_round_turn
        
    def increase_amount(self, index):
        self.rare_amount_heatmap[index] += 1

def processInput(org_input):
    result = [int(substring.strip()) for substring in org_input.split(' ')]
    return result

def optimizer(player: Player):
    weight = 0
    value = 0
    for rare in player.rare_list:
        player.rare_value_round_turn.append(rare.value())
    player.rare_value_round_turn.sort(key=lambda x: x, reverse=True)
    for rare in player.rare_value_round_turn:
        for rare2 in player.rare_list:
            if rare == rare2.value():
                if weight + rare2.w_i <= player.max_weight:
                    weight += rare2.w_i
                    value += rare2.value()
                    player.increase_amount(player.rare_list.index(rare2))
    return value

def main():
    raw1 = input()
    raw_data = processInput(raw1)
    n = raw_data[0]
    w = raw_data[1]
    rares = []
    for _ in range(n):
        raw_rare = input()
        rare_data = processInput(raw_rare)
        rares.append(Rare(*rare_data))
    
    player = Player(n, w, rares)
    max_value = optimizer(player)
    print(max_value)

main()