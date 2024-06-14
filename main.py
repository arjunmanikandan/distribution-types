#To calculate whether the given dataset is a long-tail distribution or not
import sys
import pandas as pd
from itertools import takewhile,chain

def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df

#To calculate the pairs which have less than 30% drop and filter it.
# Takewhile breaks when condition is unsatisfied
def identify_head(people_wages,threshold_value):
    incomes = people_wages.copy()
    incomes.sort(reverse=True)
    bound_pairs = [[incomes[i],incomes[i+1],
    abs((incomes[i]-incomes[i+1])/(incomes[i])*100)] 
    for i in range(0,len(incomes)-1)]
    head_pairs = list(takewhile(lambda x: x[2] < threshold_value, bound_pairs))
    head_numbers = list(set(list(chain(*[[item[0],item[1]]for item in head_pairs]))))
    head_numbers.sort(reverse=True)
    return head_numbers

def process_input(salary_history,threshold_value,column_name):
    people_wages = salary_history[column_name].values.tolist()
    head_part = identify_head(people_wages,threshold_value)
    threshold_count = (threshold_value/100)*len(people_wages)
    final_outcome = True if len(head_part) <=int(threshold_count) else False
    return final_outcome

#Input:python3 main.py 30 wage.csv HOURLY_WAGE (30->ThresholdValue)
def main():
    threshold_value = int(sys.argv[1])
    file_name = sys.argv[2]
    column_name = sys.argv[3]
    salary_history = read_csv_file(file_name)
    is_long_tail_output = process_input(salary_history,threshold_value,column_name)
    print(is_long_tail_output) 

main()
