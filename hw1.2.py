"""
 solution_1..py -- Writing CSV rows with selected columns.

 Author: Alvaro Dominguez (alvarodmz12@gmail.com)
 Last Revised: 06/11/2023
 
"""
#testcomment for push 
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--source', required=True)
parser.add_argument('--target', required=True)
parser.add_argument('--columns', required=True)
parser.add_argument('--value', required=True)
args = parser.parse_args()

columns = args.columns
source_file = args.source
target_file =  args.target
value = args.value


open_handle = open(source_file)
write_handle = open(target_file, "w", newline="")

reader=csv.reader(open_handle)
writer=csv.writer(write_handle)
header=next(reader)
writer.writerow(header)

index = header.index(columns)

for row in reader:
    if row[index] == value:
        writer.writerow(row)
        
write_handle.close()
open_handle.close()