import random


class MapGraph:
    def __init__(self, currentRoom):  # populate what is known
        self.connections, self.connections[currentRoom.id] = {}, {}
        for out in currentRoom.getExits():
            self.connections[currentRoom.id][out] = '?'

    def flip(self, direction):  # Flip a direction
        complement = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
        return complement[direction]

    def populate_known_areas(self, room, direction_moved, previous_room):
        if room.id not in self.connections:  # populate new dict.'s
            self.connections[room.id] = {}

        for out in room.getExits():  # find and populate neighbors
            if out not in self.connections[room.id].keys():
                self.connections[room.id][out] = '?'

        for out in previous_room.getExits():  # replace '?' with known numbers
            if out == direction_moved:
                self.connections[previous_room.id][out] = room.id
                self.connections[room.id][self.flip(
                    direction_moved)] = previous_room.id

    def path_to_next_q(self, room):  # Path like ['n', 'n'] to the closest ?
        visited, queue = [], [[{room.id: None}]]
        while queue:
            path = queue.pop(random.choice([0, len(queue)-1]))  # bfs or dfs
            address = list(path[-1].keys())[0]
            if address not in visited:
                for news in self.connections[address]:
                    new_path = list(path)
                    new_path.append({self.connections[address][news]: news})
                    queue.append(new_path)
                    if self.connections[address][news] == '?':
                        return [list(step.values())[0] for step in new_path[1:]]
                visited.append(address)
        return False  # no '?'s left


def traverse_all(player):
    path, rooms = [], MapGraph(player.currentRoom)
    s_path = rooms.path_to_next_q(player.currentRoom)
    while s_path:  # Master app loop, while ? exist
        for step in s_path:
            previous_room = player.currentRoom
            player.travel(step)
            rooms.populate_known_areas(player.currentRoom, step, previous_room)
        path = path + s_path
        s_path = rooms.path_to_next_q(player.currentRoom)
    return path
