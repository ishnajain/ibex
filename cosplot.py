import matplotlib.pyplot as plt

# Initialize lists to hold the values of i and cosf
i_values = []
cosf_values = []

# Read data from the log file
with open('ibex_simple_system.log', 'r') as file:
    for line in file:
        # Extract the i and cosf values

        parts = line.split(',')
        if not line:
            continue
        i_value = int(parts[0].split(':')[1].strip())
        cosf_value = float(parts[1].split(':')[1].strip())
        
        # Append values to the lists
        i_values.append(i_value)
        cosf_values.append(cosf_value)

# Create the plot
plt.plot(i_values, cosf_values, marker='o', linestyle='-')

# Add title and labels
plt.title('i vs cosf')
plt.xlabel('i')
plt.ylabel('cosf')

# Show the plot
plt.grid(True)
plt.show()
