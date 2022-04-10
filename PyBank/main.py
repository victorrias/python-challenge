import os
import csv
import pandas as pd
budget_data_path = '/Users/victoriasandoval/python-challenge/PyBank/Resources/budget_data.csv'
budget_data_df = pd.read_csv(budget_data_path)
budget_data_df.head()
Total_Number_of_Months = budget_data_df.shape[0]
Total_Number_of_Months
Total = budget_data_df["Profit/Losses"].sum()
Total
budget_data_df = budget_data_df.astype({"Profit/Losses":float})
budget_data_df.head()
budget_data_df["monthly_variances"]=budget_data_df["Profit/Losses"].diff()
budget_data_df.fillna(0)
budget_data_df["monthly_variances"].head()
budget_data_df.describe()
Average_Change = budget_data_df["monthly_variances"].mean()
Average_Change
Greatest_Increase_in_Profits = budget_data_df["monthly_variances"].max()
Greatest_Increase_in_Profits
Greatest_Increase_in_Profits_Month = budget_data_df.loc[budget_data_df["monthly_variances"].idxmax()]["Date"]
Greatest_Increase_in_Profits_Month
Greatest_Decrease_in_Profits = budget_data_df["monthly_variances"].min()
Greatest_Decrease_in_Profits
Greatest_Decrease_in_Profits_Month = budget_data_df.loc[budget_data_df["monthly_variances"].idxmin()]["Date"]
Greatest_Decrease_in_Profits_Month
Analysis =(
f"Financial Analysis\n"
f"-------------------------\n"
f"Total Months: {Total_Number_of_Months}\n"
f"Total: {Total}\n"
f"Average Change: {Average_Change}\n"
f"Greatest Increase in Profits: {Greatest_Increase_in_Profits_Month, Greatest_Increase_in_Profits, }\n"
f"Greatest Decrease in Profits: { Greatest_Decrease_in_Profits_Month, Greatest_Decrease_in_Profits}"
)
print(Analysis)
with open("/Users/victoriasandoval/python-challenge/PyBank/analysis/PyBank_Analysis.txt", 'w') as open_text_file:
    open_text_file.write(Analysis)