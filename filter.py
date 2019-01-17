# Filters output.csv based on the companies in blacklist. Saves the new file to filtered.csv
# 	Filter works by adding a 0 next to blacklisted companies and a 1 to non-blacklisted companies. Filter in excel.


# Append item to lst then return the new lst
def list_append(lst, item):
  lst.append(item)
  return lst

# Read input
with open('output.csv', 'r') as f:
	csv = [s.split(',') for s in f.read().split('\n')]

#Read in the blacklist, remove all duplicates, then save it back to the same file.
with open('blacklist', 'r+') as f:
	blacklist = set(f.read().split('\n'))
	f.seek(0)	
	f.write('\n'.join(blacklist))
	f.truncate()


# Get rid of trailing empties 
while (csv[-1][0] == ''):
	print("removed an empty line", csv[-1][0])
	csv = csv[:-1]

# Filter the csv based on column 3 (index 2), which is companies. Add 0 to the last column if it should be filtered out, 1 otherwise
filtered = [list_append(line, '0') if line[2] in blacklist else list_append(line, '1') for line in csv ]

#Add an empty row to the front for convenience 
filtered.insert(0, [''])#['ID', 'Job Name', 'Company', 'Office', 'Open Positions', 'Status', 'Location', 'Level', '#Applications', 'Deadline'])
out = '\n'.join([','.join(s) for s in filtered])

with open('filtered.csv', 'w') as f:
	f.write(out)