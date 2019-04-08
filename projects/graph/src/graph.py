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

    def bft(self, starting_vertex_id):
        visited = set()
        q = queue.Queue()
        q.put(starting_vertex_id)

        while q.qsize() >= 1:
            v = str(q.get())
            print(v)
            visited.add(v)
            for next_vert in self.vertices[v]:
                if next_vert not in visited:
                    q.put(next_vert)

    def dft(self, starting_vertex_id):
        visited = set()
        s = []
        s.append(str(starting_vertex_id))

        while len(s) > 0:
            v = str(s.pop())
            print(v)
            visited.add(v)
            for next_vert in self.vertices[v]:
                if next_vert not in visited:
                    s.append(next_vert)

    def dft_r(self, starting_vertex_id, visited=None):
        if visited == None:
            visited = set()
        print(starting_vertex_id)
        visited.add(str(starting_vertex_id))
        for next_vert in self.vertices[str(starting_vertex_id)]:
            if next_vert not in visited:
                self.dft_r(next_vert, visited)

# BFS returning shortest path:
    # Instead of storing each vertex in the queue, store the PATH to that vertex
    # When you dequeue, look at the last node
    # When you enqueue, copy the path and append the neighbor node and enqueue the new path
