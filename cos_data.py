import matplotlib.pyplot as plt

# Initialize lists to hold the values of i and cosf
i_values = []
cosf_values = []

# Read data from the log file
with open('ibex_simple_system.log', 'r') as file:
    for line in file:
        # Remove any leading/trailing whitespace
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Split the line by comma and ensure it has two parts
        parts = line.split(',')
        if len(parts) != 2:
            continue
        
        try:
            # Extract and convert the i and cosf values
            i_value = int(parts[0].split(':')[1].strip())
            cosf_value = float(parts[1].split(':')[1].strip())
            
            # Append values to the lists
            i_values.append(i_value)
            cosf_values.append(cosf_value)
        except (IndexError, ValueError):
            # Skip lines that don't match the expected format
            continue

# Create the plot
plt.plot(i_values, cosf_values, marker='o', linestyle='-')

# Add title and labels
plt.title('i vs cosf')
plt.xlabel('i')
plt.ylabel('cosf')

# Show the plot
plt.grid(True)
plt.show()
