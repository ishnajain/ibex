import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

def parse_log_file(file_path):
    data = defaultdict(list)
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            if 'group' in line and 'step_d' in line and 'cosf' in line:
                parts = line.split(',')
                group = int(parts[0].split(':')[1].strip())
                step_d = float(parts[1].split(':')[1].strip())
                cosf = float(parts[2].split(':')[1].strip())
                
                data[step_d].append((group, cosf))
                
    return data

def plot_linear_graphs(data):
    plt.figure(figsize=(14, 8))
    
    for step_d, values in data.items():
        values.sort()  # Sort values by group
        groups = [v[0] for v in values]
        cosfs = [v[1] for v in values]
        
        plt.plot(groups, cosfs, label=f'step_d = {step_d}', marker='o')
    
    plt.xlabel('group')
    plt.ylabel('cosf')
    plt.title('Group vs. cosf for different step_d values')
    plt.legend()
    plt.grid(True)
    plt.show()

# Path to the log file
log_file_path = 'ibex_simple_system.log'

# Parse the log file to get data
data = parse_log_file(log_file_path)

# Plot the data
plot_linear_graphs(data)
