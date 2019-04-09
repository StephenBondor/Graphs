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
