def process_cosf_values(file_path):
    cosf_values = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Extract the `cosf` value
            parts = line.split(',')
            for part in parts:
                if 'cosf' in part:
                    cosf_value = float(part.split(':')[1])
                    # Multiply by 10000 and format as a four-digit integer
                    formatted_value = int(cosf_value * 10000)
                    # cosf_values.append(f'{formatted_value:04d}')
                    cosf_values.append(f'{formatted_value}')
    
    # Print the values as a comma-separated list
    print(','.join(cosf_values))

# Call the function with the path to abs.txt
process_cosf_values('abc.txt')
