import random
lst = [2]
for i in range(1, random.randint(5, 8)): lst.append(random.randint(lst[i-1], (lst[i-1]*2)-1))
if len(lst) % 2 == 0: med = (lst[(int((len(lst)-1)/2))] + lst[(int((len(lst)-1)/2))+1])/2
else: med = lst[(int((len(lst)-1)/2))]
#  I spent several hours on just trying to get the for loop to print in a fstring. I couldn't get it to work.
for i in range(len(lst)): print(lst[i], end=" ")
print(f"Sum: {sum(lst)}, Median: {med}, Average: {sum(lst)/len(lst)}")