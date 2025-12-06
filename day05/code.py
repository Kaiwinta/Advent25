
class Refregirator:
    def __init__(self, fresh_part, ingredients_list):
        self.fresh_part = fresh_part
        self.ingredients_list = ingredients_list
        self.fresh_ranges = []

    def get_fresh_ranges(self):
        for part in self.fresh_part.splitlines():
            start, end = map(int, part.split('-'))
            self.fresh_ranges.append((start, end))
    
    def get_fresh_ingredients(self):
        self.get_fresh_ranges()
        fresh_ingredients_count = 0
        for ingredient in self.ingredients_list.splitlines():
            ingredient_id = int(ingredient.strip())
            if any(start <= ingredient_id <= end for start, end in self.fresh_ranges):
                fresh_ingredients_count += 1
        return fresh_ingredients_count

class Refregirator_pt_2:
    def __init__(self, fresh_part):
        self.fresh_part = fresh_part
        self.fresh_ranges = []

    def get_fresh_ranges(self):
        for part in self.fresh_part.splitlines():
            start, end = map(int, part.split('-'))
            self.fresh_ranges.append((start, end))

    def get_fresh_ingredients_count(self):
        self.get_fresh_ranges()
        self.fresh_ranges.sort()
        merged = []
        for start, end in self.fresh_ranges:
            if merged and start <= merged[-1][1] + 1:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
            else:
                merged.append((start, end))
        return sum(end - start + 1 for start, end in merged)


def main():
    with open("input.txt") as file:
        data = file.read().strip().split("\n\n")
    fresh_part = data[0]
    ingredients_list = data[1]
    Refregirator_obj = Refregirator(fresh_part, ingredients_list)
    fresh_ingredients = Refregirator_obj.get_fresh_ingredients()
    Refregirator_pt_2_obj = Refregirator_pt_2(fresh_part)
    fresh_ingredients_pt_2 = Refregirator_pt_2_obj.get_fresh_ingredients_count()
    print("Fresh ingredients count (Method 2):", fresh_ingredients_pt_2)
    print("Fresh ingredients count:", fresh_ingredients)

if __name__ == "__main__":
    main()
