"""
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
 Convert the extracted value to a floating point number and print it out.
"""

text = "X-DSPAM-Confidence:    0.8475"

my_pos = text.find(":")
my_slice = text[my_pos+1:].strip()
my_slice = float(my_slice)
print my_slice
