## Read the file
with open("data.txt", 'r') as file:
    data = file.readlines()

col1 = list()
col2 = list()
sum: int = 0

for row in data:
    cols = row.split("   ")
    col1.append(int(cols[0]))
    col2.append(int(cols[1]))

col1.sort()
col2.sort()

for i, row_col1 in enumerate(col1):
    # First part
    # sum = sum + abs(col1[i]-col2[i])
    
    # second part
    count1: int = 0
    for row_col2 in col2:
        if row_col1 == row_col2:
            count1 += 1
    sum = sum + (row_col1 * count1)
    
print(sum)