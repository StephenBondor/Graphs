class MapRoom:
    def __init__(self, name):
        self.name = name


class TraversalGraph:
    def __init__(self, player):
        # Declarations
        self.rooms = {}
        self.connections = {}

        # populate initial values
        self.rooms[player.currentRoom.id] = MapRoom(player.currentRoom.id)
        self.connections[player.currentRoom.id] = {}

        # find current initial neighbors
        exits = player.currentRoom.getExits()
        if 'n' in exits:
            self.connections[player.currentRoom.id]['n'] = '?'
        if 's' in exits:
            self.connections[player.currentRoom.id]['s'] = '?'
        if 'e' in exits:
            self.connections[player.currentRoom.id]['e'] = '?'
        if 'w' in exits:
            self.connections[player.currentRoom.id]['w'] = '?'

    def populate_known_areas(self, player, direction_moved, previous_room):

        # populate new values
        if player.currentRoom.id not in self.rooms:
            self.rooms[player.currentRoom.id] = MapRoom(player.currentRoom.id)
        if player.currentRoom.id not in self.connections:
            self.connections[player.currentRoom.id] = {}

        # find and populate current initial neighbors
        exits = player.currentRoom.getExits()
        if 'n' in exits:
            if 'n' not in self.connections[player.currentRoom.id].keys():
                self.connections[player.currentRoom.id]['n'] = '?'
        if 's' in exits:
            if 's' not in self.connections[player.currentRoom.id].keys():
                self.connections[player.currentRoom.id]['s'] = '?'
        if 'e' in exits:
            if 'e' not in self.connections[player.currentRoom.id].keys():
                self.connections[player.currentRoom.id]['e'] = '?'
        if 'w' in exits:
            if 'w' not in self.connections[player.currentRoom.id].keys():
                self.connections[player.currentRoom.id]['w'] = '?'

        # fill in numbers on map
        old_exits = previous_room.getExits()
        if direction_moved == 'n' and 'n' in old_exits:
            self.connections[previous_room.id]['n'] = player.currentRoom.id
            self.connections[player.currentRoom.id]['s'] = previous_room.id
        if direction_moved == 's' and 's' in old_exits:
            self.connections[previous_room.id]['s'] = player.currentRoom.id
            self.connections[player.currentRoom.id]['n'] = previous_room.id
        if direction_moved == 'e' and 'e' in old_exits:
            self.connections[previous_room.id]['e'] = player.currentRoom.id
            self.connections[player.currentRoom.id]['w'] = previous_room.id
        if direction_moved == 'w' and 'w' in old_exits:
            self.connections[previous_room.id]['w'] = player.currentRoom.id
            self.connections[player.currentRoom.id]['e'] = previous_room.id

        # print(direction_moved, self.connections)

    def travel_to_next(self, player):
        # breadth first search
        # should return a path of instructions ['n', 'n', 'e'] for example
        # that the player can then use to travel
        queue = [[{player.currentRoom.id: None}]]
        print("queue: ", queue)
        visited = []
        print("visited: ", visited)

        while queue:
            path = queue.pop(0)
            print("  path: ", path, ", path[-1]:", path[-1])

            address = path[-1].keys()
            print("  address: ", address)

            if address not in visited:
                for next_vert in self.connections[address]:
                    print("    next_vert: ", next_vert)
                    new_path = list(path)
                    print("    new_path: ", new_path)
                    new_path.append({
                        self.connections[address][next_vert]: next_vert})
                    print("    new_path: ", new_path)
                    queue.append(new_path)
                    print("    queue: ", queue)
                    if self.connections[address][next_vert] == '?':
                        return new_path[1:]
                visited.append(address)
                print("  visited: ", visited)
        return -1

    # def addConnection(self, currentRoomID, adjacentRoomID, direction):
    #     """
    #     Creates a bi-directional connection betwen rooms
    #     """
    #     if currentRoomID == adjacentRoomID:
    #         print("WARNING: A room cannot be connected with itself")
    #         return False
    #     elif adjacentRoomID in self.connections[currentRoomID] or currentRoomID in self.connections[adjacentRoomID]:
    #         print("WARNING: Connection already exists")
    #         return False
    #     else:
    #         self.connections[currentRoomID].add(adjacentRoomID)
    #         self.connections[adjacentRoomID].add(currentRoomID)
    #         return True

    # def addRoom(self, name):
    #     """
    #     Create a new room with a sequential integer ID
    #     """
    #     self.rooms[self.lastID] = User(name)
    #     self.friendships[self.lastID] = set()


def TraverseAll(player):
    # initialize the stack
    known_rooms = TraversalGraph(player)
    path = []
    # find the closest place to travel to -- an unexplored '?'
    short_path = known_rooms.travel_to_next(
        player)  # returns a list of directions
    # travel there
    # path = ['s', 's', 'n', 'n', 'w', 'w', 'e',
    #         'e', 'n', 'n', 's', 's', 'e', 'e']

    # path = ['s', 's', 'n', 'n']

    # path = ['n', 'n']
    while short_path != -1:
        print("eventual path: ", short_path)
        # Re-Populate the TraversalGraph
        # Repeat
        i = 1
        for step in short_path:
            # print(i, "current position: ", player.currentRoom.id)
            i += 1
            previous_room = player.currentRoom
            player.travel(step)
            # print('position after move: ', player.currentRoom.id)
            known_rooms.populate_known_areas(player, step, previous_room)
            # print("_____")
        path = path + short_path
        short_path = known_rooms.travel_to_next(player)

    return path
