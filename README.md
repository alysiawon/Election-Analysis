# election-analysis

## Overview of Project
The purpose of this project is to automate the election audit process using Python. In this specific project, the Colorado Board of Elections team requested an election audit of the recent local congressional election. The following tasks are required to be fulfilled:

1. The total number of votes cast
2. The complete list of candidates who received votes
3. The total number of votes each candidate received
4. The percentage of votes each candidate won
5. The winner of the election based on popular vote
6. The voter turnout of each county
7. The percentage of votes from each county out of the total count
8. The county with the highest turnout 

## Election-Audit Results

The data preparation utilizes Python to perform calculations by creating lists and dictionaries, decision statements, and using repetition statements to iterate through the lists and dictionaries. This helped to automate the process and print the statements into a Text Editor file. Insight are generated on the <a href="PyPoll_Challenge.py">PyPoll Script</a>. 

The final results are printed in the <a href="Analysis/election_analysis.txt">PyPoll Text Editor File</a>. 

<img src="Resources/Election_Audit_Results.png" width="400">

**Candidate Results**
- The total number of votes casted in this congressional election was 369,711 votes.
- The breakdown of the number of votes and the percentage of the total votes each candidate received are:
    - Charles Caper Stockham: 85,213 (23.0%)
    - Diana DeGette: 272,892 (73.8%)
    - Raymon Anthony Doane: 11,606 (3.1%)
- The candidate who won the election was Diana DeGette with 272,892 votes and a winning percentage of 73.8%.

**County Results**
- The breakdown of the number of votes and the percentage of total votes of each county in the precinct are:
    - Jefferson: 38,855 (10.5%)
    - Denver: 306,055 (82.8%)
    - Arapahoe 24,801 (6.7%)
- The county with the largest number of votes was Denver with 306,055 votes, which is 82.8% of the total votes. 

## Election-Audit Summary

**Business Proposal**

The Elections Commission can use this script for future election. If the dataset is set up similarly and the Elections Commission would like to produce the same results (candidate and county results), then this code is already set up to do so. 

**Modifications**

In order to fully optimize this script, the two modifications I recommend are: 

1. Automate the Python Script to Run Daily

    A suggestion could be to add a Python script to allow the votes to be calculated daily. During an election, there are multiple forms of receiving ballots, for example, mail-in ballots, punch cards or direct recording electronics, with various counting methods from hand counting, maching counting or computer counting. Each method has a different process time and procedure. With adding an automated script to update daily, we can give live results to the general public. 

2. Print a Graph

    Another suggestion could be printing a bar chart in Python to visualize the election results. Election results normally involve a large volumes of votes and can be hard for people to conceptualize how much someone is winning by or losing by. By creating a bar chart, we can directly compare the winners and losers by the number of votes or percentage of votes. We can also use this to compare the counties and other metrics. 