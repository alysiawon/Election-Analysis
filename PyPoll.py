# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

     # Write some data to the file.
     txt_file.write("Counties in the Election\n")

     txt_file.write("-----------------------\n")

     txt_file.write("Arapahoe\nDenver\nJefferson")

# Close the file
txt_file.close()

# 1. The total number of votes casted
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winnier of the election based on popular vote