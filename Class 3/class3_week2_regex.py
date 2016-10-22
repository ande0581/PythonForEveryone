import re

#my_file = open('regex_sum_42.txt')
my_file = open('regex_sum_322505.txt').read()
all_numbers = []

"""
for line in my_file:
    results = re.findall('[0-9]+', line)
    if len(results) != 0:
        for result in results:
            all_numbers.append(int(result))
"""

results = re.findall('[0-9]+', my_file)
for result in results:
    all_numbers.append(int(result))


print "Numbers found:", len(all_numbers)
print "The Sum of all numbers:", sum(all_numbers)


