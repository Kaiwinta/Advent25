from collections import deque

class ButtonListV2:
    def __init__(self, input_line: str):
        parts = input_line.split()

        self.buttons = []
        for p in parts:
            if p.startswith('('):
                indices = list(map(int, p[1:-1].split(',')))
                self.buttons.append(indices)

        target_str = parts[-1][1:-1]
        self.target = tuple(map(int, target_str.split(',')))
        self.N = len(self.target)

        self.button_vectors = []
        for b in self.buttons:
            vec = [0] * self.N
            for i in b:
                vec[i] = 1
            self.button_vectors.append(tuple(vec))


def min_presses_v2(machine: ButtonListV2) -> int:
    start = tuple(0 for _ in range(machine.N))
    target = machine.target

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        state, dist = queue.popleft()

        if state == target:
            return dist

        for vec in machine.button_vectors:
            next_state = tuple(state[i] + vec[i] for i in range(machine.N))
            if any(next_state[i] > target[i] for i in range(machine.N)):
                continue
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, dist + 1))

    raise ValueError("Target unreachable")


class ButtonList: 
    def __init__(self, input_line: str):
        parts = input_line.split()

        diagram = parts[0][1:-1]
        self.target = 0
        for i, ch in enumerate(diagram):
            if ch == '#':
                self.target |= (1 << i)

        self.buttons = []
        for p in parts[1:]:
            if p.startswith('('):
                indices = p[1:-1].split(',')
                mask = 0
                for idx in indices:
                    mask |= (1 << int(idx))
                self.buttons.append(mask)


def min_presses(machine: ButtonList) -> int:
    buttons = machine.buttons
    target = machine.target
    B = len(buttons)
    best = float('inf')

    for subset in range(1 << B):
        state = 0
        presses = 0

        for i in range(B):
            if subset & (1 << i):
                state ^= buttons[i]
                presses += 1
                if presses >= best:
                    break
        if state == target:
            best = min(best, presses)
    return best


def main():
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    machines = [ButtonList(line) for line in lines]
    machines_v2 = [ButtonListV2(line) for line in lines]

    total = 0
    for machine in machines:
        total += min_presses(machine)
    total_v2 = 0
    for machine in machines_v2:
        total_v2 += min_presses_v2(machine)
    print("Total Part 1:", total)
    print("Total Part 2:", total_v2) 

if __name__ == "__main__":
    main()
