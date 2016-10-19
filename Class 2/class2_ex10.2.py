"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of
 the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a
 second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

name = raw_input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

my_dict = {}

for line in handle:
    if line.startswith("From "):
        line = line.strip().split()
        line = line[5].split(':')
        hour = line[0]
        my_dict[hour] = my_dict.get(hour, 0) + 1

# Create a list of tuples that can be sorted
my_list = []
for k, v in my_dict.items():
    my_list.append((k, v))

# Sort the list of tuples by their key
my_list.sort()
for k, v in my_list:
    print k, v
