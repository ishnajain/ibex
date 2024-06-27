import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def parse_log_file(file_path):
    groups = []
    step_ds = []
    cosfs = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            if 'group' in line and 'step_d' in line and 'cosf' in line:
                parts = line.split(',')
                group = int(parts[0].split(':')[1].strip())
                step_d = float(parts[1].split(':')[1].strip())
                cosf = float(parts[2].split(':')[1].strip())
                
                groups.append(group)
                step_ds.append(step_d)
                cosfs.append(cosf)
                
    return groups, step_ds, cosfs

def plot_3d_scatter(groups, step_ds, cosfs):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    sc = ax.scatter(step_ds, groups, cosfs, c=cosfs, cmap='coolwarm', s=100)
    plt.colorbar(sc, label='cosf')

    ax.set_xlabel('step_d')
    ax.set_ylabel('group')
    ax.set_zlabel('cosf')
    ax.set_title('3D Scatter Plot of step_d, group, and cosf values')

    plt.show()

# Path to the log file
log_file_path = 'ibex_simple_system.log'

# Parse the log file to get data
groups, step_ds, cosfs = parse_log_file(log_file_path)

# Plot the data
plot_3d_scatter(groups, step_ds, cosfs)
