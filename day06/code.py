
class VerticalCalculator:
    def __init__(self, data, operations):
        self.data = data
        self.operations = operations

    def calculate_vertical_numbers(self):
        total = 0
        for col in range(len(self.data[0])):
            match self.operations[col]:
                case "+":
                    total += self._calculate_sum(col)
                case "*":
                    total += self._calculate_product(col)
        return total

    def _calculate_product(self, col):
        product = 1
        for row in self.data:
            product *= int(row[col])
        return product

    def _calculate_sum(self, col):
        return sum(int(row[col]) for row in self.data)

class VerticalCalculator_Part2(VerticalCalculator):
    def _calculate_product(self, col):
        string_values = [row[col] for row in self.data]
        values = []
        max_length = max(len(sv) for sv in string_values)
        for i in range(max_length):
            value = 0
            for sv in string_values:
                digit = None
                if i <= len(sv) - 1 and sv[i] != ' ':
                    digit = int(sv[i])
                if digit is not None:
                    value = value * 10 + digit
            values.append(value)
        product = 1
        for v in values:
            product *= v
        print(f"Column {col} values for product: {values}")
        print(f"Column {col} product: {product}")
        return product
    
    def _calculate_sum(self, col):
        string_values = [row[col] for row in self.data]
        values = []
        max_length = max(len(sv) for sv in string_values)
        for i in range(max_length):
            value = 0
            for sv in string_values:
                digit = None
                if i <= len(sv) - 1 and sv[i] != ' ':
                    digit = int(sv[i])
                if digit is not None:
                    value = value * 10 + digit
            values.append(value)
        print(f"Column {col} values for sum: {values}")
        print(f"Column {col} sum: {sum(values)}")
        return sum(values)

def cut_on_indexes(line, cutting_indexes):
    parts = []
    previous_index = 0
    for index in cutting_indexes:
        parts.append(line[previous_index:index])
        previous_index = index + 1
    parts.append(line[previous_index:])
    return parts

def get_vertical_cutting_indexes(raw):
    cutting_indexes = []
    for i in range(0, len(raw[0])):
        valid=True
        for line in raw:
            if line[i] != " ":
                valid = False
                break
        if valid:
            cutting_indexes.append(i)
    return cutting_indexes
        
             

def main():
    with open("input.txt", "r") as file:
        raw = [line.split("\n")[0] for line in file]
        vertical_cutting_indexes = get_vertical_cutting_indexes(raw)
        raw = [cut_on_indexes(line, vertical_cutting_indexes) for line in raw]

    # Last line is operations
    operations = [op.strip() for op in raw[-1]]
    numbers = raw[:-1]
    print(numbers)
    print(operations)

    # Align all rows to the same width
    calculator = VerticalCalculator_Part2(numbers, operations)
    sum_result = calculator.calculate_vertical_numbers()
    print("Vertical Sums:", sum_result)
    
if __name__ == "__main__":
    main()