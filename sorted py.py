s1=input('enter the no:')
s2=input('enter the no:')
if sorted(s1)==sorted(s2):
    print('it is sorted')
else:
    print('NOT SOTRED')

n=input('enter the string:')
count=0
for i in n.lower():
    if i in 'aeiou':
        count+=1
print(count)

lst = [10, 15, 20, 25, 30, 35]
odd = []

for i in lst:
    if i % 2 != 0:
        odd.append(i)

print("Original List:", lst)
print("Odd Numbers:", odd)

lst = [1, 2, 3, 4, 5]
rev = []

for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])

print("Original List:", lst)
print("Reversed List:", rev)

lst = [1, 2, 3]
num = ""

for i in lst:
    num += str(i)

print("Single Integer =", int(num))
