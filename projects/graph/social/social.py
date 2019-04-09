import random


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(i)

        i = 0
        while i < numUsers*avgFriendships//2:
            if self.addFriendship(random.randint(1, numUsers), random.randint(1, numUsers)):
                i += 1

        # Create friendships
        # allConnections = []

        # for i in range(1, numUsers+1):
        #     for j in range(i+1, numUsers+1):
        #         allConnections.append([i, j])

        # random.shuffle(allConnections)

        # for i in range(0, numUsers*avgFriendships//2):
        #     self.addFriendship(allConnections[i][0], allConnections[i][1])

    def bfs(self, start, target):
        queue = [[start]]
        visited = []
        if start == target:
            return [target]

        while queue:
            path = queue.pop(0)
            v = path[-1]
            if v not in visited:
                for next_vert in self.friendships[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.append(new_path)
                    if next_vert == target:
                        return new_path
                visited.append(v)
        return None

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        for user in self.users:
            path = self.bfs(userID, user)
            if path is not None:
                visited[user] = path

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(100000, 5)
    print("all friendsships: ", sg.friendships)
    connections = sg.getAllSocialPaths(1)
    totalLength = 0
    # for path in connections.items():
    #     # print(path)
    #     totalLength = totalLength + len(path[1])

    # print("all connections for specific: ", connections)
