from math import sqrt

class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"Box({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return self.__str__()

class Circuit:
    def __init__(self, file_data):
        self.file_data = file_data
        self.boxes = []
        self.connections = []
        for line in self.file_data:
            line = line.strip()
            self.create_box(line)

    def create_box(self, string):
        splitted = string.split(',')
        x = int(splitted[0])
        y = int(splitted[1])
        z = int(splitted[2])
        box = Box(x, y, z)
        self.boxes.append(box)
    
    def create_shortest_straight_line_junction(self, nb_to_create):
        distances = []
        circuits = [[box] for box in self.boxes]
        passed = set()
        for i in range(len(self.boxes)):
            for j in range(i + 1, len(self.boxes)):
                if (i, j) in passed or (j, i) in passed:
                    continue
                passed.add((i, j))
                box1 = self.boxes[i]
                box2 = self.boxes[j]
                distance = sqrt((box1.x - box2.x) ** 2 + (box1.y - box2.y) ** 2 + (box1.z - box2.z) ** 2)
                distances.append((distance, (box1, box2)))
        distances.sort(key=lambda x: x[0])
        for k in range(min(nb_to_create, len(distances))):
            self.connections.append(distances[k][1])
            box1, box2 = distances[k][1]
            box1_circuit = [circuit for circuit in circuits if box1 in circuit][0]
            box2_circuit = [circuit for circuit in circuits if box2 in circuit][0]
            if box1_circuit and box2_circuit and box1_circuit != box2_circuit:
                circuits.remove(box1_circuit)
                circuits.remove(box2_circuit)
                new_circuit = box1_circuit + box2_circuit
                circuits.append(new_circuit)
        self.circuits = circuits

    def get_size_of_largest_3_Circuit(self):
        size = 1
        self.circuits.sort(key=lambda x: len(x), reverse=True)
        for circuit in self.circuits[:3]:
            size *= len(circuit)
        return size
    
    def get_one_large_circuit_cable_length(self):
        distances = []
        circuits = [[box] for box in self.boxes]
        passed = set()
        for i in range(len(self.boxes)):
            for j in range(i + 1, len(self.boxes)):
                if (i, j) in passed or (j, i) in passed:
                    continue
                passed.add((i, j))
                box1 = self.boxes[i]
                box2 = self.boxes[j]
                distance = sqrt((box1.x - box2.x) ** 2 + (box1.y - box2.y) ** 2 + (box1.z - box2.z) ** 2)
                distances.append((distance, (box1, box2)))
        distances.sort(key=lambda x: x[0])
        k = 0
        while len(circuits) > 2:
            self.connections.append(distances[k][1])
            box1, box2 = distances[k][1]
            box1_circuit = [circuit for circuit in circuits if box1 in circuit][0]
            box2_circuit = [circuit for circuit in circuits if box2 in circuit][0]
            if box1_circuit and box2_circuit and box1_circuit != box2_circuit:
                circuits.remove(box1_circuit)
                circuits.remove(box2_circuit)
                new_circuit = box1_circuit + box2_circuit
                circuits.append(new_circuit)
            k += 1
        self.circuits = circuits

    def get_shortest_connection_between_two_circuits(self, circuit1, circuit2):
        min_distance = float('inf')
        boxes = []
        for box1 in circuit1:
            for box2 in circuit2:
                distance = sqrt((box1.x - box2.x) ** 2 + (box1.y - box2.y) ** 2 + (box1.z - box2.z) ** 2)
                if distance < min_distance:
                    min_distance = distance
                    boxes = (box1, box2)
        return (boxes[0].x * boxes[1].x)

def main():
    with open("input.txt", "r") as file:
        file_data = file.readlines()
    circuit = Circuit(file_data)
    # circuit.create_shortest_straight_line_junction(1000)
    # size = circuit.get_size_of_largest_3_Circuit()
    # print("Size of largest 3-Circuit:", size)
    circuit.get_one_large_circuit_cable_length()
    result = circuit.get_shortest_connection_between_two_circuits(circuit.circuits[0], circuit.circuits[1])
    print("Result of shortest connection between two circuits:", result)

if __name__ == "__main__":
    main()