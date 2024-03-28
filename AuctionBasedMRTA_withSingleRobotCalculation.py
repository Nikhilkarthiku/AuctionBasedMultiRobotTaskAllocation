'''
# Calculate bids for each robot
robots = ""
tasks = ""
for robot in robots:
    robot.bid = calculate_bid(robot, tasks)

# Maximum Bidder
winning_robot = max(robots, key=lambda robot: robot.bid)
winning_task = min(unallocated_tasks, key=lambda task: abs(task.location - winning_robot.location))
print(f"Task {winning_task.task_id} assigned to Robot {winning_robot.robot_id} with bid {winning_robot.bid}")

# Minimum Bidder (optional)
losing_robot = min(robots, key=lambda robot: robot.bid)
print(f"Robot {losing_robot.robot_id} submitted the lowest bid of {losing_robot.bid}")
'''

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


class Task:
    def __init__(self, task_id, location):
        self.task_id = task_id
        self.location = location


class Robot:
    def __init__(self, robot_id, location):
        self.robot_id = robot_id
        self.location = location
        self.assigned_task = None


# Define the confined space dimensions
space_width = 50
space_height = 20

# Define the number of robots and tasks
num_robots = 10
num_tasks = 20

# Generate random locations for robots and tasks within the confined space
robot_locations = np.random.randint(0, space_width, size=(num_robots, 2))  # Random (x, y) locations for robots
task_locations = np.random.randint(0, space_width, size=(num_tasks, 2))  # Random (x, y) locations for tasks

# Assign names to robots and tasks
robot_names = [f'R{i + 1}' for i in range(num_robots)]
task_names = [f'T{i + 1}' for i in range(num_tasks)]

# Assign tasks to available robots based on proximity
task_assignments = []
for task_id, task_location in enumerate(task_locations):
    distances = np.linalg.norm(robot_locations - task_location, axis=1)
    closest_robot_index = np.argmin(distances)
    task_assignments.append((task_location, closest_robot_index))

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, space_width)
ax.set_ylim(0, space_height)
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_title('Robot Task Allocation')

# Initialize empty lists to store robot and task objects
robots = []
tasks = []

# Initialize robot movement data
robot_movement_data = {}


# Function to update the animation frame
def update(frame):
    ax.clear()
    ax.scatter(robot_locations[:, 0], robot_locations[:, 1], color='blue', label='Robots', marker='s', s=100)
    ax.scatter(task_locations[:, 0], task_locations[:, 1], color='red', label='Tasks', marker='o', s=100)

    for task_location, robot_index in task_assignments:
        robot_location = robot_locations[robot_index]
        # Calculate the new robot position towards the task location
        dx = (task_location[0] - robot_location[0]) * frame / 100
        dy = (task_location[1] - robot_location[1]) * frame / 100
        ax.plot([robot_location[0], robot_location[0] + dx], [robot_location[1], robot_location[1] + dy], color='black')

        # Update robot movement data
        if robot_index not in robot_movement_data:
            robot_movement_data[robot_index] = {'x': [], 'y': []}
        robot_movement_data[robot_index]['x'].append(robot_location[0] + dx)
        robot_movement_data[robot_index]['y'].append(robot_location[1] + dy)

    for robot_index, robot_name in enumerate(robot_names):
        ax.text(robot_locations[robot_index][0], robot_locations[robot_index][1], robot_name, ha='center', va='center')

    for task_index, task_name in enumerate(task_names):
        ax.text(task_locations[task_index][0], task_locations[task_index][1], task_name, ha='center', va='center')


# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=10)

# Display the task allocation chart
plt.legend()
plt.grid(True)
plt.show()

# Display tasks assigned to robots
print("Tasks Assigned to Robots:")
for task_index, (task_location, robot_index) in enumerate(task_assignments):
    task_name = task_names[task_index]
    robot_name = robot_names[robot_index]
    print(f"Task {task_name} assigned to Robot {robot_name}")

# Display robot movement data
print("\nRobot Movement Data:")
for robot_index, movement_data in robot_movement_data.items():
    robot_name = robot_names[robot_index]
    print(f"Robot {robot_name} movement data:")
    for frame, (x, y) in enumerate(zip(movement_data['x'], movement_data['y'])):
        print(f"Frame {frame + 1}: X={x}, Y={y}")

def plot_tasks_and_robots(tasks, robots):
    tasks_x = [task.location for task in tasks]
    robots_x = [robot.location for robot in robots]
    tasks_y = [0 for _ in tasks]
    robots_y = [1 for _ in robots]

    plt.scatter(tasks_x, tasks_y, color='blue', label='Tasks', marker='o', s=100)
    plt.scatter(robots_x, robots_y, color='red', label='Robots', marker='s', s=100)
    plt.xlabel('Location')
    plt.ylabel('Type')
    plt.title('Robot Task Allocation')
    plt.yticks([0, 1], ['Tasks', 'Robots'])
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_bids(robots):
    robot_ids = [robot.robot_id for robot in robots]
    bids = [robot.bid for robot in robots]

    plt.bar(robot_ids, bids, color='green')
    plt.xlabel('Robot ID')
    plt.ylabel('Bid')
    plt.title('Bids Submitted by Robots')
    plt.xticks(robot_ids)
    plt.grid(True)
    plt.show()

def allocate_tasks(tasks, robots):
    unallocated_tasks = list(tasks)
    while unallocated_tasks:
        for robot in robots:
            robot.bid = calculate_bid(robot, unallocated_tasks)
        winning_robot = max(robots, key=lambda robot: robot.bid)
        winning_task = min(unallocated_tasks, key=lambda task: abs(task.location - winning_robot.location))
        winning_robot.assigned_task = winning_task
        unallocated_tasks.remove(winning_task)
        print(f"Task {winning_task.task_id} assigned to Robot {winning_robot.robot_id} with bid {winning_robot.bid}")

def calculate_bid(robot, tasks):
    nearest_task_distance = min(abs(task.location - robot.location) for task in tasks)
    return 1 / nearest_task_distance if nearest_task_distance != 0 else float('inf')

# Define tasks and robots
tasks = [Task(task_id=1, location=10), Task(task_id=2, location=20), Task(task_id=3, location=30)]
robots = [Robot(robot_id=1, location=5), Robot(robot_id=2, location=15)]

# Allocate tasks to robots using auction-based approach
allocate_tasks(tasks, robots)

# Plot bids submitted by robots
plot_bids(robots)

# Plot tasks and robots
plot_tasks_and_robots(tasks, robots)
for robot in robots:
    if robot.assigned_task:
        print(f"Robot {robot.robot_id} assigned Task {robot.assigned_task.task_id}")