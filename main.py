import time

class Graph:
    # Defining constructor for class Graph
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges_list = []

    # Function to add edges to the Graph
    def add_link(self, vertex1, vertex2, weight):
        self.edges_list.append([vertex1, vertex2, weight])

    # Find function to check if adding a link between 
    # two vertices creates a cycle in the MST or not
    # Finds the set to which element belongs
    def find_set(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_set(parent, parent[i])

    # Union function to add the link between 2 vertices 
    # if it does not create a cycle in the MST
    # by merging the 2 disjoint sets x and y by rank
    def perform_union(self, parent, rank, x, y):
        root_x = self.find_set(parent, x)
        root_y = self.find_set(parent, y)

        # Logic to add smaller rank tree to root of higher rank tree
        # If ranks are same, set one as the root and increase its rank by one
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    # Applying Kruskal algorithm to find MST
    def kruskal_mst(self):
        mst_result = []    
        i, e = 0, 0

        # Sorts edges in ascending order of their weights
        self.edges_list = sorted(self.edges_list, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.num_vertices):
            parent.append(node)
            rank.append(0)

        # If number of edges in MST is less than V-1,
        # pick the smallest edge and increment the index
        while e < self.num_vertices - 1:
            u, v, w = self.edges_list[i]
            i += 1
            x = self.find_set(parent, u)
            y = self.find_set(parent, v)

            # If adding the edge doesn't create a cycle, then
            # Include it in the result and increment the index 
            # of result for next edge or discard the edge
            if x != y:
                e += 1
                mst_result.append([u, v, w])
                self.perform_union(parent, rank, x, y)

        for u, v, weight in mst_result:
            print(f"{u} - {v}: {weight}")

# input graph 1: V=4 and E=6
# print("Graph with V=4 and E=6")
# net = Graph(4)
# net.add_link(0, 1, 2)
# net.add_link(0, 3, 7)
# net.add_link(0, 2, 5)
# net.add_link(1, 3, 3)
# net.add_link(1, 2, 1)
# net.add_link(2, 3, 4)

# input graph 2: V=6 and E=9
# print("Graph with V=6 and E=9")
# net = Graph(6)
# net.add_link(0, 1, 3)
# net.add_link(0, 3, 2)
# net.add_link(0, 2, 5)
# net.add_link(1, 2, 1)
# net.add_link(1, 3, 4)
# net.add_link(2, 3, 6)
# net.add_link(2, 4, 7)
# net.add_link(4, 5, 9)
# net.add_link(3, 4, 8)

# input graph 3: V=8 and E=12
# print("Graph with V=8 and E=12")
# net = Graph(8)
# net.add_link(0, 2, 19)
# net.add_link(0, 1, 14)
# net.add_link(0, 3, 17)
# net.add_link(2, 1, 12)
# net.add_link(2, 3, 15)
# net.add_link(1, 3, 18)
# net.add_link(2, 5, 10)
# net.add_link(3, 5, 16)
# net.add_link(4, 6, 11)
# net.add_link(6, 7, 13)
# net.add_link(6, 5, 8)
# net.add_link(5, 7, 9)

# input graph 4: V=10 and E=15
# print("Graph with V=10 and E=15")
# net = Graph(10)
# net.add_link(0, 1, 3)
# net.add_link(0, 2, 4)
# net.add_link(1, 2, 2)
# net.add_link(1, 3, 18)
# net.add_link(1, 4, 6)
# net.add_link(2, 4, 20)
# net.add_link(4, 6, 16)
# net.add_link(3, 6, 8)
# net.add_link(3, 5, 11)
# net.add_link(6, 8, 13)
# net.add_link(5, 8, 10)
# net.add_link(5, 7, 14)
# net.add_link(7, 9, 21)
# net.add_link(8, 9, 1)
# net.add_link(7, 8, 12)

# input graph 5: V=12 and E=18
# print("Graph with V=12 and E=18")
# net = Graph(12)
# net.add_link(0, 1, 11)
# net.add_link(0, 2, 8)
# net.add_link(1, 2, 20)
# net.add_link(1, 3, 9)
# net.add_link(2, 3, 12)
# net.add_link(3, 4, 13)
# net.add_link(3, 5, 10)
# net.add_link(4, 5, 3)
# net.add_link(4, 6, 7)
# net.add_link(5, 10, 17)
# net.add_link(10, 11, 4)
# net.add_link(5, 11, 22)
# net.add_link(5, 6, 14)
# net.add_link(6, 8, 6)
# net.add_link(6, 7, 15)
# net.add_link(7, 8, 21)
# net.add_link(7, 9, 5)
# net.add_link(9, 5, 16)

# input graph 6: V=14 and E=21
# print("Graph with V=14 and E=21")
# net = Graph(14)
# net.add_link(0, 5, 16)
# net.add_link(0, 1, 17)
# net.add_link(0, 3, 31)
# net.add_link(1, 2, 22)
# net.add_link(1, 4, 21)
# net.add_link(4, 2, 30)
# net.add_link(2, 7, 15)
# net.add_link(4, 7, 18)
# net.add_link(4, 6, 25)
# net.add_link(3, 6, 13)
# net.add_link(7, 9, 27)
# net.add_link(7, 12, 23)
# net.add_link(9, 12, 11)
# net.add_link(9, 11, 28)
# net.add_link(6, 11, 12)
# net.add_link(6, 8, 29)
# net.add_link(6, 5, 20)
# net.add_link(5, 10, 14)
# net.add_link(10, 13, 19)
# net.add_link(11, 13, 24)
# net.add_link(8, 13, 26)

# input graph 7: V=16 and E=24
# print("Graph with V=16 and E=24")
# net = Graph(16)
# net.add_link(0, 3, 10)
# net.add_link(0, 1, 16)
# net.add_link(0, 2, 14)
# net.add_link(3, 1, 4)
# net.add_link(3, 6, 15)
# net.add_link(2, 5, 9)
# net.add_link(5, 6, 3)
# net.add_link(6, 7, 12)
# net.add_link(4, 7, 5)
# net.add_link(7, 10, 18)
# net.add_link(10, 9, 2)
# net.add_link(6, 9, 17)
# net.add_link(9, 8, 20)
# net.add_link(5, 8, 8)
# net.add_link(8, 11, 24)
# net.add_link(11, 12, 1)
# net.add_link(9, 12, 19)
# net.add_link(10, 13, 6)
# net.add_link(13, 15, 22)
# net.add_link(12, 15, 13)
# net.add_link(12, 14, 7)
# net.add_link(14, 15, 21)
# net.add_link(11, 14, 23)
# net.add_link(1, 4, 11)

# input graph 8: V=18 and E=27
# print("Graph with V=18 and E=27")
# net = Graph(18)
# net.add_link(0, 1, 9)
# net.add_link(0, 4, 4)
# net.add_link(0, 5, 19)
# net.add_link(4, 8, 3)
# net.add_link(4, 9, 18)
# net.add_link(8, 12, 2)
# net.add_link(8, 13, 17)
# net.add_link(8, 5, 7)
# net.add_link(12, 9, 6)
# net.add_link(12, 17, 16)
# net.add_link(12, 16, 1)
# net.add_link(16, 13, 5)
# net.add_link(4, 1, 8)
# net.add_link(17, 14, 15)
# net.add_link(13, 10, 23)
# net.add_link(9, 14, 25)
# net.add_link(9, 6, 21)
# net.add_link(11, 14, 22)
# net.add_link(5, 10, 24)
# net.add_link(1, 2, 10)
# net.add_link(2, 3, 11)
# net.add_link(2, 7, 26)
# net.add_link(3, 7, 12)
# net.add_link(3, 6, 20)
# net.add_link(7, 11, 13)
# net.add_link(11, 15, 14)
# net.add_link(10, 15, 27)

# input graph 9: V=20 and E=30
# print("Graph with V=20 and E=30")
# net = Graph(20)
# net.add_link(0, 1, 4)
# net.add_link(0, 4, 5)
# net.add_link(0, 7, 3)
# net.add_link(4, 7, 6)
# net.add_link(7, 14, 2)
# net.add_link(7, 11, 8)
# net.add_link(11, 14, 7)
# net.add_link(14, 18, 1)
# net.add_link(18, 15, 9)
# net.add_link(15, 12, 11)
# net.add_link(12, 8, 12)
# net.add_link(12, 16, 25)
# net.add_link(8, 5, 13)
# net.add_link(8, 9, 22)
# net.add_link(5, 1, 14)
# net.add_link(5, 2, 17)
# net.add_link(1, 2, 15)
# net.add_link(2, 3, 16)
# net.add_link(5, 6, 18)
# net.add_link(3, 6, 19)
# net.add_link(6, 10, 20)
# net.add_link(6, 9, 21)
# net.add_link(10, 13, 24)
# net.add_link(9, 13, 23)
# net.add_link(13, 16, 26)
# net.add_link(13, 17, 27)
# net.add_link(16, 17, 28)
# net.add_link(19, 16, 30)
# net.add_link(19, 17, 29)
# net.add_link(19, 15, 10)

# Function call for running Kruskal's algorithm 
# Running the algorithm 10 times and taking the 
# average of 10 results to obtain consistent result
# Capturing time taken in nanoseconds
total_time = 0
iterations = 10
while iterations > 0:
    start_time_ns = time.time_ns()
    net.kruskal_mst()
    end_time_ns = time.time_ns()
    elapsed_time_ns = end_time_ns - start_time_ns
    if elapsed_time_ns == 0:
        continue
    total_time += elapsed_time_ns
    iterations -= 1

average_time_taken = total_time / 10
print("Time Taken: ", average_time_taken)
