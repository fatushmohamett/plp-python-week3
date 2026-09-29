
count = 1
total = 0

# BUG: < was changed to <= so that 5 is included.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: total is an integer, so str(total) is needed when joining it to text.
print("Sum of 1 to 5 is: " + str(total))

# BUG: The original print/loop structure had an indentation problem. The print statement is now outside the loop.
