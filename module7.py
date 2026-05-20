class MachineNetwork:
    def __init__(self):
        # key = machine, value = list of connected machines
        self.machine_links = {}

    def add_machine(self, machine):
        # add machine if it does not exist
        if machine not in self.machine_links:
            self.machine_links[machine] = []

    def add_link(self, m1, m2):
        # add machines if missing
        self.add_machine(m1)
        self.add_machine(m2)

        # add link in both directions
        if m2 not in self.machine_links[m1]:
            self.machine_links[m1].append(m2)

        if m1 not in self.machine_links[m2]:
            self.machine_links[m2].append(m1)

    def print_network(self):
        # print all machines and their links
        print("Machine Network:")
        for machine in self.machine_links:
            print(f"{machine} -> {self.machine_links[machine]}")

    def print_connected_machines(self, machine):
        # print machines directly connected to machine
        if machine in self.machine_links:
            print(f"Machines connected to {machine}:")
            print(self.machine_links[machine])
        else:
            print("Machine not found.")

    def bfs(self, start):
        # Breadth-First Search
        if start not in self.machine_links:
            print("Machine not found.")
            return []

        visited = []
        queue = [start]

        while queue:
            current = queue.pop(0)

            if current not in visited:
                visited.append(current)

                for neighbor in self.machine_links[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return visited

    def dfs(self, start):
        # Depth-First Search
        if start not in self.machine_links:
            print("Machine not found.")
            return []

        visited = []
        stack = [start]

        while stack:
            current = stack.pop()

            if current not in visited:
                visited.append(current)

                for neighbor in reversed(self.machine_links[current]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return visited


# Testing the code:
network = MachineNetwork()

network.add_link("Machine_A", "Machine_B")
network.add_link("Machine_A", "Machine_C")
network.add_link("Machine_B", "Machine_D")
network.add_link("Machine_C", "Machine_D")
network.add_link("Machine_C", "Machine_E")

network.print_network()
print()

network.print_connected_machines("Machine_C")
print()

print("BFS from Machine_A:", network.bfs("Machine_A"))
print("DFS from Machine_A:", network.dfs("Machine_A"))
