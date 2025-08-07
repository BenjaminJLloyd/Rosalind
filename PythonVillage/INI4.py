a = 4568
b = 9115

count = 0

for num in range(a, b+1):
    if num % 2 != 0:
        count = count + num

print(count)
