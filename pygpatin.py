#PYGLATIN.PY#
#First letter goes at the end, followed by "ay"#
#E.g. "pig" becomes "igpay"#

inp = input("Enter a phrase here: ")
str_len = len(inp)
seq_number = 1
seq_list = []
while str_len != 1:
    seq_list.append(inp[seq_number])
    seq_number = seq_number + 1
    str_len = str_len - 1
seq_list.append(inp[0])
seq_list.append("ay")
seq_end = ''.join(seq_list)
print(seq_end)
