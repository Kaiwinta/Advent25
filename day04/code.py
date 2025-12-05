def is_a_roll(rool_map, i, j):
    if i < 0 or j < 0 or i >= len(rool_map) or j >= len(rool_map[i]):
        return False
    value = rool_map[i][j] == 1
    return value

proximity_positions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

removed_rolls = []

def compute_accessible_rolls(rool_map, is_pt_2=False):
    valid_rolls = 0
    for i in range(len(rool_map)):
        for j in range(len(rool_map[i])):
            if not is_a_roll(rool_map, i, j):
                continue
            nearby_rolls = 0
            for di, dj in proximity_positions:
                if is_a_roll(rool_map, i + di, j + dj):
                    nearby_rolls += 1
            if nearby_rolls < 4:
                valid_rolls += 1
                if is_pt_2:
                    removed_rolls.append((i, j))
    return valid_rolls

def get_rool_count(rool_map):
    return compute_accessible_rolls(rool_map)

def get_rool_count_pt_2(rool_map):
    total_rolls = 0
    nb_rolls = compute_accessible_rolls(rool_map, is_pt_2=True)
    total_rolls += nb_rolls
    while nb_rolls > 0:
        for i, j in removed_rolls:
            rool_map[i][j] = 0
        removed_rolls.clear()
        nb_rolls = compute_accessible_rolls(rool_map, is_pt_2=True)
        total_rolls += nb_rolls
    return total_rolls


def main():
    with open("input.txt", "r") as file:
        data = file.readlines()
    rool_map = [line.strip() for line in data]
    for i, line in enumerate(rool_map):
        rool_map[i] = [0 if char == "." else 1 for char in line]
    print(get_rool_count_pt_2(rool_map))

if __name__ == "__main__":
    main()