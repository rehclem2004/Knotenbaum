from random import randint, choice


class Node:
    def __init__(self, name, i):
        self.name = name
        self.connections = {}
        self.index = i

    def create_connections(self, node, value):
        self.connections[node] = value

    def __repr__(self):  # shows name instead of class and memory address
        return self.name


class Connections:
    def __init__(self):
        self.nodes = []
        self.paths = []
        self.default = []
        self.index = 0
        self.visited = set
        self.start = object
        self.end = object
        self.current_node = object

    def add_node(self, node):
        self.nodes.append(node)

    def set_default(self, s, e):
        self.start = s
        self.end = e
        self.current_node = s
        self.visited = {s}

    def get_random_node(self):
        return choice(self.nodes)

    def connect_nodes(self):
        for connect_node in self.nodes:
            num_connections = randint(1, 4)
            for i in range(num_connections):
                connection_node = choice(self.nodes)
                if connection_node != connect_node and connection_node not in connect_node.connections:
                    value = randint(1, 10)
                    connect_node.create_connections(connection_node, value)
                    connection_node.create_connections(connect_node, value)

    def check_end(self, con):  # check algorithm, if at end point
        cost = 0
        if con == self.end:
            cost += int(self.current_node.connections[self.end])
            self.paths.append({self.end: cost})
            self.index += 1
            return True
        else:
            self.visited.add(con)
            return False

    def get_path(self):  # Should be the algorithm, not finished
        while len(self.visited) < len(self.nodes):
            for connect in self.current_node.connections.keys():
                check = self.check_end(connect)
                if not check:
                    current_node = connect


tree = Connections()
for i in range(100):
    node = Node(f"Node {i}", i)
    tree.add_node(node)
tree.connect_nodes()

for i in range(len(tree.nodes)):
    print(tree.nodes[i].name)
    # print(tree.nodes[i].connections.keys())
    # print(tree.nodes[i].connections.values())
    print(tree.nodes[i].connections, "\n")

start_node = tree.get_random_node()
end_node = tree.get_random_node()
while end_node == start_node:
    end_node = tree.get_random_node()
tree.set_default(start_node, end_node)

print(start_node.name)
print(end_node.name)

tree.get_path()
print("Test:", tree.paths)
