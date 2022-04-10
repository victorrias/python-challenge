import os
import csv
import pandas as pd
election_data_path = '/Users/victoriasandoval/python-challenge/PyPoll/Resources/election_data.csv'
election_data_df = pd.read_csv(election_data_path)
election_data_df.head()
Total_Votes = election_data_df.shape[0]
Total_Votes
Votes_per_Candidate = election_data_df["Candidate"].value_counts()
Votes_per_Candidate
Votes_as_a_Percentage = election_data_df["Candidate"].value_counts(normalize=True)
Votes_as_a_Percentage
Winner = election_data_df["Candidate"].mode()
Winner
Analysis =(
f"Election Results\n"
f"-------------------------\n"
f"Total votes: {Total_Votes}\n"
f"-------------------------\n"
f"{Votes_as_a_Percentage}\n"
f"{Votes_per_Candidate}\n"
f"-------------------------\n"
f"Winner: {Winner}"
)
print(Analysis)
with open('/Users/victoriasandoval/python-challenge/PyPoll/analysis/PyPoll_Analysis.txt', 'w') as open_text_file:
    open_text_file.write(Analysis)