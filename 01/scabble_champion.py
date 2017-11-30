import scrabble_point_template

max_point_so_far = 0
champion = ""


def calculate_point(line):
    total_point = 0
    for char in line:
        index = ord(char.lower()) - 97
        if (index > -1 and index < 28):
            total_point += scrabble_point_template.points[index]
    return total_point


with open("dictionary.txt", "r") as dictionary:
    for line in dictionary:
        point = calculate_point(line.replace("\n", ""))
        if point > max_point_so_far:
            champion = line
print("Champion is {0}".format(champion))
