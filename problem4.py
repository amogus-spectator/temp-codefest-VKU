import math

class Rare:
    def __init__(self, v_i, w_i, a_i, b_i):
        self.v_i = v_i
        self.w_i = w_i
        self.a_i = a_i
        self.b_i = b_i

    def a_i_check(self):
        if self.a_i > 0:
            return 1
        else:
            return 0

    def value(self):
        return self.v_i * self.p_i - self.a_i * self.p_i * self.p_i + self.b_i * self.a_i_check()

class Player:
    def __init__(self, rare_amounts, max_weight, rare_list):
        self.rare_list = rare_list
        self.rare_amounts = rare_amounts
        self.max_weight = max_weight

def processInput(org_input):
    result = [int(substring.strip()) for substring in org_input.split(' ')]
    return result

def optimizer(player: Player):
    player.rare_list.sort(key=lambda x: x.value() / x.w_i, reverse=True)
    weight = 0
    value = 0
    for rare in player.rare_list:
        if weight + rare.w_i <= player.max_weight:
            weight += rare.w_i
            value += rare.value()
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