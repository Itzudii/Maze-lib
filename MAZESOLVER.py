import random
import pygame
SCREEN_WEIGHT = 600
SCREEN_HEIGHT = 600

class MAZE():
    """
    MODULE V@ --> 
    #HUNT AND KILL ALGORITHM# FOR CREATING
    #BFS# FOR SOLVING

    SOME USEFULL FUNCTION ===>
    create_maze => FOR GET MAZE_MAP DATA IN (Dict) datatype

    solvemap(self,mapData) => para = mapData => (dict) => return (list of tuples) 
    solve puzzel 
    
    EXAMPLE \/
    from MAZESOLVER import MAZE
    maze = MAZE(10)
    data = maze.create_maze()
    result = maze.solvemap(data)
    print(result)

    output \/
    [(0, 0), (0, 1), (0, 1), (0, 2), (0, 3), (0, 4), (0, 4), (0, 5), (1, 5),(1, 6), (0, 6), (0, 7), (1, 7), (2, 7), (2, 8), 
    (2, 9), (3, 9), (3, 8), (4, 8), (5, 8), (5, 9), (3, 8), (3, 7), (4, 7), (5, 7), 
    (6, 7), (7, 7), (7, 6), (6, 6), (6, 5),(7, 5), (7, 4), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (9, 8)]

    """
    def __init__(self,column):
        self.col = column
        self.iscreate = False
        self.issolve = False
        self.fps = 0

        self.wall = 5
        self.Grid = (600-self.wall) // self.col

        self.screen = pygame.display.set_mode((SCREEN_WEIGHT, SCREEN_HEIGHT))
        pygame.display.set_caption("Basic Game")
        self.clock = pygame.time.Clock()

        self.data = {}
        for i in range(self.col):
            for j in range(self.col):       
                self.data[(i,j)] = {'right':1,'left':1,'up':1,'down':1} 

        self.visitedNodes = []
        self.keys = list(self.data.keys())
        self.unvisitedNodes  = [key for key in self.keys if key not in self.visitedNodes]
        self.cntNode = random.choice(self.unvisitedNodes)

        self.currentNode = (0,0)
        self.endNode = (self.col-1,self.col-1)
        self.lastnode = self.currentNode

        # self.visitedNodes = []
        self.lastnodes = [self.currentNode]
        self.routes = {}
        self.miniroad=[]
        self.iscomplete = False
        self.finalroute = []

    def is_unvisited_Nodes(self,Node):
        x,y = Node
        return [(x+dx,y+dy) for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)] if (x+dx,y+dy) in self.keys and (x+dx,y+dy) not in self.visitedNodes]  

    def inversedirection(self,string):
        data = {
            'right':'left',
            'left':'right',
            'up':'down',
            'down':'up'
        }
        return data[string]
    
    def isdirection(self,currentNode,newNode):
        try:
            x1,y1 = currentNode
            x2,y2 = newNode
            if y1 == y2:
                if x1 > x2:
                    return 'left'
                else:
                    return 'right'
            elif x1 == x2:
                if y1 < y2:
                    return 'down'
                else:
                    return 'up'
        except Exception as e:
            return None

    def create(self):
        if not self.iscreate:
            self.visitedNodes.append(self.cntNode)
            templist = self.is_unvisited_Nodes(self.cntNode)
            if templist:
                newNode = random.choice(templist)
                direction = self.isdirection(self.cntNode,newNode)
                self.data[self.cntNode][direction] = 0
                self.data[newNode][self.inversedirection(direction)] = 0
                self.cntNode = newNode
            else:
                self.unvisitedNodes  = [key for key in self.keys if key not in self.visitedNodes]
                if not self.unvisitedNodes:
                    # self.iscomplete = True
                    self.iscreate = True
                    self.visitedNodes = []
                else:
                    for Node in self.keys:   
                        if Node in self.visitedNodes:
                            have_unvistedNode = self.is_unvisited_Nodes(Node)
                            if len(have_unvistedNode) > 0:
                               self.cntNode = Node
                               break
    
    def create_maze(self):
        while not self.iscreate:
            self.create()
        return self.data
    
    def get_next_node(self,currentNode, data):
        tempdict = {'down':(0,1),'up':(0,-1),'left':(-1,0),'right':(1,0)}
        directions = [i for i in data[currentNode] if data[currentNode][i] == 0]
        nodes = []
        for direction in directions:
                dx,dy = tempdict[direction]
                x,y = currentNode
                nodes.append((dx+x,dy+y))
        return nodes

    def draw_wall(self):
        for x,y in self.keys:
            cell = pygame.Rect(x*(self.Grid)+self.wall,y*(self.Grid)+self.wall, self.Grid, self.Grid)
            for direction in self.data[(x,y)]:
                if self.data[(x,y)][direction] == 1:
                    if direction == 'right':
                        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(cell.x+cell.width,cell.y,self.wall,self.Grid))
                    elif direction == 'left':
                        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(cell.x-self.wall,cell.y,self.wall,self.Grid))
                    elif direction == 'up':
                        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(cell.x,cell.y-self.wall,self.Grid,self.wall))
                    elif direction == 'down':
                        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(cell.x,cell.y+cell.height,self.Grid,self.wall))
    
    def solvemap(self,mapData):
        while not self.issolve:
            self.data = mapData
            self.solve()
        
        return self.finalroute
        

    def solve(self):
        if self.currentNode == self.endNode:
            self.issolve = True
            for path in self.routes.values():
                for node in path:
                    self.finalroute.append(node)
            self.finalroute += self.miniroad
        self.visitedNodes.append(self.currentNode)
        self.miniroad.append(self.currentNode)
        
        nebours = self.get_next_node(self.currentNode,self.data) 
        if len(nebours) >= 3 and self.currentNode not in self.lastnodes :
            self.routes[self.lastnode] = self.miniroad
            self.miniroad = []
            self.lastnodes.append(self.currentNode)
            self.lastnode = self.lastnodes[-1]
    
        isdead = True    
        for node in nebours:
            if node not in self.visitedNodes :
                self.currentNode = node
                isdead = False
                break
    
        if isdead:
            self.miniroad = []
            if self.lastnode in self.routes:
                self.routes.pop(self.lastnode)
            if self.currentNode == self.lastnode and self.lastnodes.__len__() > 1:
                self.lastnodes.pop()
                self.lastnode = self.lastnodes[-1]
            self.currentNode = self.lastnode
    

    def draw_path(self):
        for path in self.routes.values():
            for node in path:
                x,y = node
                a = pygame.Rect(x*(self.Grid)+self.wall,y*(self.Grid)+self.wall, self.Grid, self.Grid)
                pygame.draw.rect(self.screen,'green',a)
        
        for node in self.miniroad:
            x,y = node
            a = pygame.Rect(x*(self.Grid)+self.wall,y*(self.Grid)+self.wall, self.Grid, self.Grid)
            pygame.draw.rect(self.screen,'red',a)

    def draw_final(self):
        for node in self.finalroute:
            x,y = node
            a = pygame.Rect(x*(self.Grid)+self.wall,y*(self.Grid)+self.wall, self.Grid, self.Grid)
            pygame.draw.rect(self.screen,'yellow',a)

                
    def run(self):
        while True:
            self.screen.fill((255, 255, 255)) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if not self.iscreate:
                self.create()
            elif self.iscreate and not self.issolve:
                self.solve()
                self.draw_path()
            elif self.issolve:
                self.draw_final()

            self.draw_wall()
            pygame.display.update()
            self.clock.tick(self.fps)

if __name__ == "__main__":
    pygame.init()
    maze = MAZE(20)
    maze.run()