class RangeClass:
    def __init__(self, range_str):
        start_str, end_str = range_str.split('-')
        self.start = int(start_str)
        self.end = int(end_str)
        self.invalid_ids = []
        if (start_str[0] == "0"):
            self.invalid_ids.append(self.start)
        if (end_str[0] == "0"):
            self.invalid_ids.append(self.end)


    def get_invalid_ids(self):
        for i in range(self.start, self.end + 1):
            if not is_valid_id_pt_2(i):
                self.invalid_ids.append(i)
        return sum(self.invalid_ids)

def is_valid_id(id_num):
    string_version = str(id_num)
    for i in range(1, len(string_version)):
        if string_version[:i] == string_version[i:]:
            return False
    return True

def is_valid_id_pt_2(id_num):
    string_version = str(id_num)
    length = len(string_version)
    for i in range(1, length):
        token = string_version[:i]
        token_length = len(token)
        occurences = string_version.count(token)
        if occurences * token_length == length:
            return False
    return True


def main():
    with open("input.txt", "r") as file:
        lines = file.read()
    total_score = 0
    ranges = lines.split(",")
    for range in ranges:
        range_instance = RangeClass(range.strip())
        total_score += range_instance.get_invalid_ids()
    print(total_score)

    print(is_valid_id(11))
    print(is_valid_id(22))

if __name__ == "__main__":
    main()