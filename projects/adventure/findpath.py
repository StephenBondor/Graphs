from random import choices, choice, random


class MapGraph:
    def __init__(self, room):  # populate what is known in connections
        self.cxn, self.cxn[room.id] = {}, {}
        for out in sorted(room.getExits(), key=lambda _: random()):
            self.cxn[room.id][out] = '?'

    def populate_known_areas(self, room, move, previous_room):
        if room.id not in self.cxn:
            self.cxn[room.id] = {}  # create new room in connections
        for out in sorted(room.getExits(), key=lambda _: random()):
            if out not in self.cxn[room.id].keys():
                self.cxn[room.id][out] = '?'  # find and populate unknown exits
        for out in previous_room.getExits():
            if out == move:  # replace '?' with known numbers if we moved from there
                self.cxn[previous_room.id][out] = room.id
                self.cxn[room.id][{'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}[
                    move]] = previous_room.id  # add reverse direction to previous room

    def path_to_next_q(self, room):  # Path like ['n', 'n'] to the closest ?
        visited, arr = [], [[{room.id: None}]]
        while arr:  # randomly choose bfs or dfs by weight: [8, 2] respectively
            # path = arr.pop(choices([0, len(arr)-1], [8, 2])[0])
            path = arr.pop(0)
            address = list(path[-1].keys())[0]
            if address not in visited:
                for news in self.cxn[address]:
                    new_path = list(path)
                    new_path.append({self.cxn[address][news]: news})
                    arr.append(new_path)
                    if self.cxn[address][news] == '?':
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
