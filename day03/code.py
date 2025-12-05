values = [int(x) for x in range(10)]


class Batteries:
    def __init__(self, line):
        self.line = line.strip()

    def compute(self):
        part_one = self.line[:-1]
        part_one_values = [values[int(x)] for x in part_one]
        part_one_max = max(part_one_values)
        part_one_max_index = part_one_values.index(part_one_max)
        part_two = self.line[part_one_max_index + 1 :]
        part_two_values = [values[int(x)] for x in part_two]
        part_two_max = max(part_two_values)
        result = part_one_max * 10 + part_two_max
        return result
    
    def compute_pt_2(self):
        joltage = 0
        max_index = 0
        for i in range(12):
            string_part = self.line[max(i, max_index):len(self.line) - 11 + i]
            print_string = max(i, max_index) * " " + string_part
            print(print_string)
            part_values = [values[int(x)] for x in string_part]
            part_max = max(part_values)
            part_max_index = part_values.index(part_max)
            max_index = part_max_index + max(i, max_index) + 1
            joltage = joltage * 10 + part_max
        return joltage


def main():
    with open("input.txt", "r") as file:
        data = file.readlines()
    result = 0
    for line in data:
        battery = Batteries(line)
        result += battery.compute_pt_2()
    print(result)

if __name__ == "__main__":
    main()