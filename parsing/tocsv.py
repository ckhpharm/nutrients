import csv


txt_file = r"final_result.txt"
csv_file = r"final_table.csv"

in_txt = csv.reader(open(txt_file, "r"), delimiter = ' ')
out_csv = csv.writer(open(csv_file, 'w'))

out_csv.writerows(in_txt)