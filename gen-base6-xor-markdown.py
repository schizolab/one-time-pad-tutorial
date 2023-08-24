table = [[' ', '0', '1', '2', '3', '4', '5']]

first_row = [0]  
for i in range(0,6):
  first_row.append(0 ^ i)
table.append(first_row)

for i in range(1,6):
  row = [i]
  for j in range(0,6):
    row.append(i ^ j) # XOR
  table.append(row)

with open('xor-lut.md', 'w') as f:
  
  # write table header
  f.write('| | | | | | | |\n')

  # Write header separator 
  f.write('| --- | --- | --- | --- | --- | --- | --- |\n')

  for row in table:
    f.write('| ' + ' | '.join(str(x) for x in row) + ' |\n')