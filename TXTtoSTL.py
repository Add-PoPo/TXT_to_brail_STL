import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the dimensions of the box in mm
width = 250
height = 250
depth = 1

# Define the vertices of the box
r = [0, width]  # Range for x and y coordinates
X, Y = np.meshgrid(r, r)

# Define the 6 faces of the box
vertices = [
    [[0, 0, 0], [width, 0, 0], [width, height, 0], [0, height, 0]],  # Bottom face
    [[0, 0, depth], [width, 0, depth], [width, height, depth], [0, height, depth]],  # Top face
    [[0, 0, 0], [0, 0, depth], [0, height, depth], [0, height, 0]],  # Front face
    [[width, 0, 0], [width, 0, depth], [width, height, depth], [width, height, 0]],  # Back face
    [[0, height, 0], [width, height, 0], [width, height, depth], [0, height, depth]],  # Top face
    [[0, 0, 0], [width, 0, 0], [width, 0, depth], [0, 0, depth]]  # Bottom face
]

# Create a Poly3D collection
box = Poly3DCollection(vertices, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25)

# Create a new figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Add the box to the plot
ax.add_collection3d(box)

# Set limits and labels
ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('Z (mm)')
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_zlim(0, depth)

# Show the plot
plt.show()