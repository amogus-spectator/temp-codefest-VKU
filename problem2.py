def processInput(org_input):
    result = [int(substring.strip()) for substring in org_input.split(' ')]
    return result


def splitList(original_list:list, start:int, end:int):
    new_list = []
    for i in range(start, end):
        new_list.append(original_list[i])
    return new_list
def main():
    org_input = input()
    data = processInput(org_input)
    total_length = data[0]
    partial_start = data[1]
    partial_end = data[2]
    
    org_next_input = input()
    org_variables = processInput(org_next_input)
    
    sublist = splitList(org_variables, partial_start-1, partial_end)
    multiplier = 1
    for i in range(len(sublist)):
        multiplier = multiplier*sublist[i]
    print(multiplier%10)

main()