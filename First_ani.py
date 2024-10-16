from manim import *
import numpy as np

# Creating Node Structure
class TreeNode():
    # Constructor call for the value of node
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class TreeAnimation(Scene):
    
    # Writing the DFS code
    def dfs(self, Node, coord, k, TreeObjects):
        if Node is None:
            return
        # Drawing line and circle for the node
        line = Line(start=coord, end=coord + np.array([-.8 + k, -1, 0]))
        circle = Circle(radius=.2, stroke_width=2)
        TreeObjects.add(circle)
        
        # Positioning the circle to the correct location
        circle.move_to(coord)
        self.play(Create(circle))
        circle.set_fill(BLUE, 0.9)
        self.wait(.5)
        
        # Recurse to the left and right children
        if Node.left is not None:
            TreeObjects.add(line)
            self.play(Create(line))
            self.dfs(Node.left, coord + np.array([-.8 + k, -1, 0]), k + 0.23, TreeObjects)
        
        if Node.right is not None:
            lin1 = Line(start=coord, end=coord + np.array([.8 - k, -1, 0]))
            TreeObjects.add(lin1)
            self.play(Create(lin1))
            self.dfs(Node.right, coord + np.array([.8 - k, -1, 0]), k + 0.23, TreeObjects)

    def construct(self):

        # Creating the Tree
        lisNode = []
        for i in range(0, 7):
            Node = TreeNode(i)
            lisNode.append(Node)

        # Defining the tree structure
        lisNode[0].left = lisNode[1]
        lisNode[0].right = lisNode[2]
        lisNode[1].left = lisNode[3]
        lisNode[1].right = lisNode[4]
        lisNode[2].left = lisNode[5]
        lisNode[2].right = lisNode[6]

        # Setting the Initial Coordinate  
        initialcoord = np.array([0.00, 2.00, 0.00])
        
        # Intro for Animations
        intro = Text("Binary Tree", color=BLUE)
        intro.move_to(initialcoord + np.array([0, 1, 0]))
        
        self.play(Write(intro))
        self.wait(2)
        
        k = 0.01
        ending = Text("Explore the Code on My GitHub!", color=PURPLE)
        ending.move_to(intro.get_center())
        
        # Creating VGroup Object to store the objects of all Nodes
        TreeObjects = VGroup()
        
        # Calling the Dfs function 
        self.dfs(lisNode[0], initialcoord, k, TreeObjects)
        self.wait(1)
        
        self.play(FadeOut(TreeObjects))
        
        # Transform intro text to ending text
        self.play(Transform(intro, ending))
        self.wait(2)
