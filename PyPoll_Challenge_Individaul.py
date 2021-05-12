# Add dependencies
import csv
import os

# # Direct Path To File
# file_to_load = ('resource/election_results.csv')

# election_data = open(file_to_load,'r')

# with open(file_to_load,'r') as election_data:
#     print(election_data)

# election_data.close()

# # Indirect Path to File

# Add variable to load a file from a path
file_to_load = os.path.join("resources", "election_results.csv")

# with open(file_to_load) as election_data:
#     print(election_data)

# Write To A txt File
file_to_save = os.path.join("analysis", "election_analysis_individual.txt")
# open(file_to_save, "w")

# # Write on txt File with Open & Close Function
# outfile = open(file_to_save,"w")
# outfile.write = "Hello world"
# outfile.close()

# Write on txt File with With Function
with open(file_to_save,"w") as txt_file:
    txt_file.write("Hello World")