
n = int(input("input: "))
total = 0
n_to_1 = 1
n_to_2 = 0
if n == 0:
    total = n_to_2

elif n == 1:
    total = n_to_1
    
else:
    for i in range(1,n):
        total = n_to_2 + n_to_1
        n_to_2 = n_to_1
        n_to_1 = total
print(total)
