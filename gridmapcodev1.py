import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import random

# Generate 100 sample points clustered around specific centers
def generate_clustered_points(num_points, cluster_centers, spread=5):
    data = []
    for _ in range(num_points):
        center = random.choice(cluster_centers)
        x = int(np.clip(np.random.normal(center[0], spread), 0, 100))
        y = int(np.clip(np.random.normal(center[1], spread), 0, 100))
        data.append([x, y])
    return data

# Define cluster centers
cluster_centers = [
    [30, 30],
    [70, 70],
    [50, 20],
    [20, 80]
]

# Generate data
data = generate_clustered_points(100, cluster_centers)

# Setup figure and axis
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_aspect('equal')

# Grid lines
ax.set_xticks(np.arange(0, 101, 5))
ax.set_yticks(np.arange(0, 101, 5))
ax.grid(True, linestyle='--', color='lightgray', linewidth=0.5)

# Store circles
circles = []
CLICK_RADIUS = 4

def get_color_by_radius(radius):
    if radius <= 2:
        return 'blue'
    elif radius <= 5:
        return 'green'
    elif radius <= 8:
        return 'yellow'
    else:
        return 'red'

def grow_or_create_circle(x, y):
    for circle in circles:
        cx, cy = circle.center
        dist = np.hypot(cx - x, cy - y)
        if dist < CLICK_RADIUS:
            new_radius = circle.get_radius() + 1
            circle.set_radius(new_radius)
            circle.set_color(get_color_by_radius(new_radius))
            return
    new_circle = Circle((x, y), radius=1, color=get_color_by_radius(1), alpha=0.6)
    circles.append(new_circle)
    ax.add_patch(new_circle)

# Process all points
for point in data:
    grow_or_create_circle(point[0], point[1])

# Show the plot
plt.show()
