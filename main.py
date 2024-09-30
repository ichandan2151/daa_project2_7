import time

class Network:
    # Defining constructor for class Network
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges_list = []

    # Function to add edges to the network
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
    # by merging the 2 disjoint sets a and b by rank
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

# input graph with V=4 and E=6
print("Network with V=4 and E=6")
net = Network(4)
net.add_link(0, 1, 2)
net.add_link(0, 3, 7)
net.add_link(0, 2, 5)
net.add_link(1, 3, 3)
net.add_link(1, 2, 1)
net.add_link(2, 3, 4)


# input graph 2: V=6 and E=9
# print("Graph with V=6 and E=9")
# g = Graph(6)
# g.add_edge(0, 1, 3)
# g.add_edge(0, 3, 2)
# g.add_edge(0, 2, 5)
# g.add_edge(1, 2, 1)
# g.add_edge(1, 3, 4)
# g.add_edge(2, 3, 6)
# g.add_edge(2, 4, 7)
# g.add_edge(4, 5, 9)
# g.add_edge(3, 4, 8)


#input graph 3: V=8 and E=12
# print("Graph with V=8 and E=12")
# g = Graph(8)
# g.add_edge(0, 2, 19)
# g.add_edge(0, 1, 14)
# g.add_edge(0, 3, 17)
# g.add_edge(2, 1, 12)
# g.add_edge(2, 3, 15)
# g.add_edge(1, 3, 18)
# g.add_edge(2, 5, 10)
# g.add_edge(3, 5, 16)
# g.add_edge(4, 6, 11)
# g.add_edge(6, 7, 13)
# g.add_edge(6, 5, 8)
# g.add_edge(5, 7, 9)


#input graph 4: V=10 and E=15
# print("Graph with V=10 and E=15")
# g = Graph(10)
# g.add_edge(0, 1, 3)
# g.add_edge(0, 2, 4)
# g.add_edge(1, 2, 2)
# g.add_edge(1, 3, 18)
# g.add_edge(1, 4, 6)
# g.add_edge(2, 4, 20)
# g.add_edge(4, 6, 16)
# g.add_edge(3, 6, 8)
# g.add_edge(3, 5, 11)
# g.add_edge(6, 8, 13)
# g.add_edge(5, 8, 10)
# g.add_edge(5, 7, 14)
# g.add_edge(7, 9, 21)
# g.add_edge(8, 9, 1)
# g.add_edge(7, 8, 12)

# input graph 5: V=12 and E=18
# print("Graph with V=12 and E=18")
# g = Graph(12)
# g.add_edge(0, 1, 11)
# g.add_edge(0, 2, 8)
# g.add_edge(1, 2, 20)
# g.add_edge(1, 3, 9)
# g.add_edge(2, 3, 12)
# g.add_edge(3, 4, 13)
# g.add_edge(3, 5, 10)
# g.add_edge(4, 5, 3)
# g.add_edge(4, 6, 7)
# g.add_edge(5, 10, 17)
# g.add_edge(10, 11, 4)
# g.add_edge(5, 11, 22)
# g.add_edge(5, 6, 14)
# g.add_edge(6, 8, 6)
# g.add_edge(6, 7, 15)
# g.add_edge(7, 8, 21)
# g.add_edge(7, 9, 5)
# g.add_edge(9, 5, 16)


# input graph 6: V=14 and E=21
# print("Graph with V=14 and E=21")
# g = Graph(14)
# g.add_edge(0, 5, 16)
# g.add_edge(0, 1, 17)
# g.add_edge(0, 3, 31)
# g.add_edge(1, 2, 22)
# g.add_edge(1, 4, 21)
# g.add_edge(4, 2, 30)
# g.add_edge(2, 7, 15)
# g.add_edge(4, 7, 18)
# g.add_edge(4, 6, 25)
# g.add_edge(3, 6, 13)
# g.add_edge(7, 9, 27)
# g.add_edge(7, 12, 23)
# g.add_edge(9, 12, 11)
# g.add_edge(9, 11, 28)
# g.add_edge(6, 11, 12)
# g.add_edge(6, 8, 29)
# g.add_edge(6, 5, 20)
# g.add_edge(5, 10, 14)
# g.add_edge(10, 13, 19)
# g.add_edge(11, 13, 24)
# g.add_edge(8, 13, 26)


# input graph 7: V=16 and E=24
# print("Graph with V=16 and E=24")
# g = Graph(16)
# g.add_edge(0, 3, 10)
# g.add_edge(0, 1, 16)
# g.add_edge(0, 2, 14)
# g.add_edge(3, 1, 4)
# g.add_edge(3, 6, 15)
# g.add_edge(2, 5, 9)
# g.add_edge(5, 6, 3)
# g.add_edge(6, 7, 12)
# g.add_edge(4, 7, 5)
# g.add_edge(7, 10, 18)
# g.add_edge(10, 9, 2)
# g.add_edge(6, 9, 17)
# g.add_edge(9, 8, 20)
# g.add_edge(5, 8, 8)
# g.add_edge(8, 11, 24)
# g.add_edge(11, 12, 1)
# g.add_edge(9, 12, 19)
# g.add_edge(10, 13, 6)
# g.add_edge(13, 15, 22)
# g.add_edge(12, 15, 13)
# g.add_edge(12, 14, 7)
# g.add_edge(14, 15, 21)
# g.add_edge(11, 14, 23)
# g.add_edge(1, 4, 11)


# input graph 8: V=18 and E=27
# print("Graph with V=18 and E=27")
# g = Graph(18)
# g.add_edge(0, 1, 9)
# g.add_edge(0, 4, 4)
# g.add_edge(0, 5, 19)
# g.add_edge(4, 8, 3)
# g.add_edge(4, 9, 18)
# g.add_edge(8, 12, 2)
# g.add_edge(8, 13, 17)
# g.add_edge(8, 5, 7)
# g.add_edge(12, 9, 6)
# g.add_edge(12, 17, 16)
# g.add_edge(12, 16,1)
# g.add_edge(16, 13, 5)
# g.add_edge(4, 1, 8)
# g.add_edge(17, 14, 15)
# g.add_edge(13, 10, 23)
# g.add_edge(9, 14, 25)
# g.add_edge(9, 6, 21)
# g.add_edge(11, 14, 22)
# g.add_edge(5, 10, 24)
# g.add_edge(1, 2, 10)
# g.add_edge(2, 3, 11)
# g.add_edge(2, 7, 26)
# g.add_edge(3, 7, 12)
# g.add_edge(3, 6, 20)
# g.add_edge(7, 11, 13)
# g.add_edge(11, 15, 14)
# g.add_edge(10, 15, 27)


# input graph 9: V=20 and E=30
# print("Graph with V=20 and E=30")
# g = Graph(20)
# g.add_edge(0, 1, 4)
# g.add_edge(0, 4, 5)
# g.add_edge(0, 7, 3)
# g.add_edge(4, 7, 6)
# g.add_edge(7, 14, 2)
# g.add_edge(7, 11, 8)
# g.add_edge(11, 14, 7)
# g.add_edge(14, 18, 1)
# g.add_edge(18, 15, 9)
# g.add_edge(15, 12, 11)
# g.add_edge(12, 8, 12)
# g.add_edge(12, 16, 25)
# g.add_edge(8, 5, 13)
# g.add_edge(8, 9, 22)
# g.add_edge(5, 1, 14)
# g.add_edge(5, 2, 17)
# g.add_edge(1, 2, 15)
# g.add_edge(2, 3, 16)
# g.add_edge(5, 6, 18)
# g.add_edge(3, 6, 19)
# g.add_edge(6, 10, 20)
# g.add_edge(6, 9, 21)
# g.add_edge(10, 13, 24)
# g.add_edge(9, 13, 23)
# g.add_edge(13, 16, 26)
# g.add_edge(13, 17, 27)
# g.add_edge(16, 17, 28)
# g.add_edge(19, 16, 30)
# g.add_edge(19, 17, 29)
# g.add_edge(19, 15, 10)


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
