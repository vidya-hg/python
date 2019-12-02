import re
file_name = input("Enter input file:")
if len(file_name) <= 1: file_name = "sample_file.txt"
fh = open(file_name)
result_list = list()
for line in fh:
    lx = line.rstrip()
    ly = re.findall('[0-9]+', lx)
    if len(ly) > 0 :
        for num in ly: result_list.append(num)
for i in range(len(result_list)):
    result_list[i] = int(result_list[i])
total_sum = sum(result_list)
print(total_sum)
