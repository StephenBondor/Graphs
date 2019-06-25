"""
Simple graph implementation
"""

import queue


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def bft(self, start):
        visited = set()
        q = queue.Queue()
        q.put(start)
        while q.qsize() >= 1:
            v = q.get()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.vertices[v]:
                    if next_vert not in visited:
                        q.put(next_vert)

    def bfs(self, start, target):
        queue = [[start]]
        visited = []
        if start == target:
            print("same same")
            return target

        while queue:
            path = queue.pop(0)
            v = path[-1]
            if v not in visited:
                for next_vert in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.append(new_path)
                    if next_vert == target:
                        print("shortest path:", new_path)
                        return new_path
                visited.append(v)
        print("no path")
        return None

    def dft(self, start):
        visited = []
        s = [start]
        while len(s) > 0:
            v = s.pop()
            print("item: ", [v])
            visited.append(v)
            for next_vert in self.vertices[v]:
                if next_vert not in visited and next_vert not in s:
                    s.append(next_vert)

    def dfs(self, start, target):
        queue = [[start]]
        visited = []
        if start == target:
            print("same same")
            return target

        while queue:
            path = queue.pop()
            v = path[-1]
            if v not in visited:
                for next_vert in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.append(new_path)
                    if next_vert == target:
                        print("One of many paths:", new_path)
                        return new_path
                visited.append(v)
        print("no path")
        return None

    def dft_r(self, start, visited=None):
        if visited == None:
            visited = set()
        print(start)
        visited.add(start)
        for next_vert in self.vertices[start]:
            if next_vert not in visited:
                self.dft_r(next_vert, visited)

    # def dfs_r(self, start, target, path=None):
    #     if path == None:
    #         path = []
    #     path += [start]
    #     print(start)
    #     for next_vert in self.vertices[start]:
    #         if next_vert not in path:
    #             self.dfs_r(next_vert, path)
    #     return path


	#     def bfs(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing the shortest path from
    #     starting_vertex to destination_vertex in
    #     breath-first order.
    #     """
    #     # Create an empty set to store visited nodes
    #     visited = set()
    #     # Create an empty Queue and enqueue A PATH TO the starting vertex
    #     q = Queue()
    #     q.enqueue( [starting_vertex] )
    #     # While the queue is not empty...
    #     while q.size() > 0:
    #         # Dequeue the first PATH
    #         path = q.dequeue()
    #         # GRAB THE VERTEX FROM THE END OF THE PATH
    #         v = path[-1]
    #         # IF VERTEX == TARGET, RETURN PATH
    #         if v == destination_vertex:
    #             return path
    #         # If that vertex has not been visited...
    #         if v not in visited:
    #             # Mark it as visited
    #             visited.add(v)
    #             # Then add A PATH TO all of its neighbors to the back of the queue
    #             for neighbor in self.vertices[v]:
    #                 # Copy the path
    #                 path_copy = list(path)
    #                 # Append neighbor to the back of the copy
    #                 path_copy.append(neighbor)
    #                 # Enqueue copy
    #                 q.enqueue(path_copy)



    # def dfs(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.
    #     """
    #     # Create an empty set to store visited nodes
    #     visited = set()
    #     # Create an empty Stack and push A PATH TO the starting vertex
    #     s = Stack()
    #     s.push( [starting_vertex] )
    #     # While the stack is not empty...
    #     while s.size() > 0:
    #         # Pop the first PATH
    #         path = s.pop()
    #         # GRAB THE VERTEX FROM THE END OF THE PATH
    #         v = path[-1]
    #         # IF VERTEX == TARGET, RETURN PATH
    #         if v == destination_vertex:
    #             return path
    #         # If that vertex has not been visited...
    #         if v not in visited:
    #             # Mark it as visited
    #             visited.add(v)
    #             # Then add A PATH TO all of its neighbors to the top of the stack
    #             for neighbor in self.vertices[v]:
    #                 # Copy the path
    #                 path_copy = list(path)
    #                 # Append neighbor to the back of the copy
    #                 path_copy.append(neighbor)
    #                 # Enqueue copy
    #                 s.push(path_copy)

# 	"""
# Simple graph implementation
# """
# from util import Stack, Queue  # These may come in handy


# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""

#     def __init__(self):
#         self.vertices = dict()

#     def add_vertex(self, vertex):
#         """
#         Add a vertex to the graph.
#         """
#         if vertex not in self.vertices:
#             self.vertices[vertex] = set()

#     def add_edge(self, v1, v2):
#         """
#         Add a directed edge to the graph.
#         """
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             raise IndexError('These vertices do not exist')

#     def add_edge_u(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#             self.vertices[v2].add(v1)
#         else:
#             raise IndexError('These vertices do not exist')

#     def bft(self, starting_vertex):
#         """
#         Print each vertex in breadth-first order
#         beginning from starting_vertex.
#         """
#         visited = set()
#         queue = Queue()
#         queue.enqueue(starting_vertex)
#         while queue.size() > 0:
#             vertex = queue.dequeue()
#             if vertex not in visited:
#                 visited.add(vertex)
#                 print(vertex)
#                 for neighbor in self.vertices[vertex]:
#                     queue.enqueue(neighbor)

#     def dft(self, starting_vertex):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.
#         """
#         visited = set()
#         stack = Stack()
#         stack.push(starting_vertex)
#         while stack.size() > 0:
#             vertex = stack.pop()
#             if vertex not in visited:
#                 visited.add(vertex)
#                 print(vertex)
#                 for neighbor in self.vertices[vertex]:
#                     stack.push(neighbor)

#     def dft_recursive(self, starting_vertex, visited=False):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.
#         This should be done using recursion.
#         """
#         if not visited:
#             visited = set()

#         visited.add(starting_vertex)
#         print(starting_vertex)
#         for vertex in self.vertices[starting_vertex]:
#             self.dft_recursive(
#                 vertex, visited) if vertex not in visited else None

#     def bfs(self, starting_vertex, destination_vertex):
#         """
#         Return a list containing the shortest path from
#         starting_vertex to destination_vertex in
#         breath-first order.
#         """
#         if starting_vertex == destination_vertex:
#             return [starting_vertex]

#         visited = set()
#         queue = Queue()
#         queue.enqueue([starting_vertex])
#         while queue.size() > 0:
#             path = queue.dequeue()
#             vertex = path[-1]
#             if vertex not in visited:
#                 for neighbor in self.vertices[vertex]:
#                     path_new = path[:]
#                     path_new.append(neighbor)
#                     queue.enqueue(path_new)
#                     if neighbor == destination_vertex:
#                         return path_new
#                 visited.add(vertex)
#         return []

#     def dfs(self, starting_vertex, destination_vertex):
#         """
#         Return a list containing a path from
#         starting_vertex to destination_vertex in
#         depth-first order.
#         """
#         if starting_vertex == destination_vertex:
#             return [starting_vertex]

#         visited = set()
#         stack = Stack()
#         stack.push([starting_vertex])
#         while stack.size() > 0:
#             path = stack.pop()
#             vertex = path[-1]
#             if vertex not in visited:
#                 for neighbor in self.vertices[vertex]:
#                     path_new = path[:]
#                     path_new.append(neighbor)
#                     stack.push(path_new)
#                     if neighbor == destination_vertex:
#                         return path_new
#                 visited.add(vertex)
#         return []


# if __name__ == '__main__':
#     graph = Graph()  # Instantiate your graph
#     # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(3)
#     graph.add_vertex(4)
#     graph.add_vertex(5)
#     graph.add_vertex(6)
#     graph.add_vertex(7)
#     graph.add_edge(5, 3)
#     graph.add_edge(6, 3)
#     graph.add_edge(7, 1)
#     graph.add_edge(4, 7)
#     graph.add_edge(1, 2)
#     graph.add_edge(7, 6)
#     graph.add_edge(2, 4)
#     graph.add_edge(3, 5)
#     graph.add_edge(2, 3)
#     graph.add_edge(4, 6)

#     '''
#     Should print:
#         {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
#     '''
#     print(graph.vertices)

#     '''
#     Valid DFT paths:
#         1, 2, 3, 5, 4, 6, 7
#         1, 2, 3, 5, 4, 7, 6
#         1, 2, 4, 7, 6, 3, 5
#         1, 2, 4, 6, 3, 5, 7
#     '''
#     graph.dft(1)

#     '''
#     Valid BFT paths:
#         1, 2, 3, 4, 5, 6, 7
#         1, 2, 3, 4, 5, 7, 6
#         1, 2, 3, 4, 6, 7, 5
#         1, 2, 3, 4, 6, 5, 7
#         1, 2, 3, 4, 7, 6, 5
#         1, 2, 3, 4, 7, 5, 6
#         1, 2, 4, 3, 5, 6, 7
#         1, 2, 4, 3, 5, 7, 6
#         1, 2, 4, 3, 6, 7, 5
#         1, 2, 4, 3, 6, 5, 7
#         1, 2, 4, 3, 7, 6, 5
#         1, 2, 4, 3, 7, 5, 6
#     '''
#     graph.bft(1)

#     '''
#     Valid DFT recursive paths:
#         1, 2, 3, 5, 4, 6, 7
#         1, 2, 3, 5, 4, 7, 6
#         1, 2, 4, 7, 6, 3, 5
#         1, 2, 4, 6, 3, 5, 7
#     '''
#     graph.dft_recursive(1)

#     '''
#     Valid BFS path:
#         [1, 2, 4, 6]
#     '''
#     print(graph.bfs(1, 6))

#     '''
#     Valid DFS paths:
#         [1, 2, 4, 6]
#         [1, 2, 4, 7, 6]
#     '''
#     print(graph.dfs(1, 6))
