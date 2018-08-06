numbers = (1, 2, 3, 4, 5, 6, 7)
num_sum = 0
count = 0
for x in numbers:
        num_sum = num_sum + x
        count = count + 1
        print(count)
        if count == 7:
                break

for x in range(4):
	if (x == 8):
		continue
		print(x)