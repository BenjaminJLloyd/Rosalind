input_filename = 'input.txt'
output_filename = 'output.txt'

# Use 'with' to automatically handle closing the files
with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
    # Initialize a counter for the line number, starting at 1
    line_number = 1

    # Loop through each line in the input file
    for line in infile:

        # Check if the current line number is even
        if line_number % 2 == 0:
            # If it is, write that line to the output file
            outfile.write(line)

        # Increment the line number for the next loop
        line_number += 1