"""
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail
 messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
  The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they
  appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop
  to find the most prolific committer.
"""

name = raw_input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

my_dict = {}

for line in handle:
    line = line.strip()
    if line.startswith("From:"):
        my_key = line.split()[1]
        my_dict[my_key] = my_dict.get(my_key, 0) + 1

max_count = 0
max_name = None

for k, v in my_dict.items():
    if v > max_count:
        max_count, max_name = v, k

print max_name, max_count


