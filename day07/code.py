class BeamSearch:
    def __init__(self, data):
        self.data = data
        self.start_index = self.get_starting_point(data)
        self.beam_positions = [(1, self.start_index)]
        self.numbers_splitted = 0
        self.spliter_used = []
    
    def __str__(self):
        display_data = [list(row) for row in self.data]
        for row, col in self.beam_positions:
            display_data[row][col] = "|"
        return "\n".join("".join(row) for row in display_data)

    def get_starting_point(self, data):
        for i in range(len(data[0])):
            if data[0][i] == 'S':
                return i
        return -1
    
    def add_beam_if_possible(self, row, col):
        new_beam = (row, col)
        if (row < 0 or row >= len(self.data) or
            col < 0 or col >= len(self.data[0])):
            return
        if new_beam not in self.beam_positions:
            self.beam_positions.append(new_beam)
    
    def moving_beams(self):
        for beam in self.beam_positions:
            row, col = beam
            if row + 1 >= len(self.data):
                self.beam_positions.remove(beam)
                continue
            down_cell = self.data[row + 1][col]
            if down_cell == "^":
                if beam not in self.spliter_used:
                    self.numbers_splitted += 1
                    self.spliter_used.append(beam)
                self.beam_positions.remove(beam)
                self.add_beam_if_possible(row, col - 1)
                self.add_beam_if_possible(row, col + 1)
            else:
                self.beam_positions.remove(beam)
                self.add_beam_if_possible(row + 1, col)

    def move_loop(self):
        while self.beam_positions:
            self.moving_beams()
        return self.numbers_splitted
    
    def write_cleaned_map(self):
        cleaned_map = [["."] * len(self.data[0]) for _ in range(len(self.data))]
        cleaned_map[0][self.start_index] = "S"
        for row, col in self.spliter_used:
            cleaned_map[row][col] = "^"
        content = "\n".join("".join(row) for row in cleaned_map)
        with open("cleaned_map.txt", "w") as file:
            file.write(content)

from collections import defaultdict

def count_timelines(grid):
    rows = len(grid)
    cols = len(grid[0])
    start_col = grid[0].index("S")
    dp = defaultdict(int)
    dp[(0, start_col)] = 1
    finished = 0

    for row in range(rows):
        next_dp = defaultdict(int)
        for (r, c), ways in dp.items():
            if r != row:
                continue
            if r + 1 >= rows:
                finished += ways
                continue
            cell = grid[r][c]
            if cell == "^":
                if c - 1 >= 0:
                    next_dp[(r + 1, c - 1)] += ways
                if c + 1 < cols:
                    next_dp[(r + 1, c + 1)] += ways
            else:
                next_dp[(r + 1, c)] += ways

        dp = next_dp
    return finished + sum(dp.values())

def main():
    with open("input.txt", "r") as file:
        data = [line.strip() for line in file.readlines()]
    beam_search = BeamSearch(data)
    result = beam_search.move_loop()
    print(result)
    with open("input.txt") as f:
        grid = [line.rstrip("\n") for line in f]
    timelines = count_timelines(grid)
    print(timelines)

if __name__ == "__main__":
    main()


            