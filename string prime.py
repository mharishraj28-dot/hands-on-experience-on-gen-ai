print('prime no:/n')
n=int(input('enter the no'))
if n<=1:
    print('not prime')
else:
    for i in range(2,n):
        if n%i==0:
            print('not prime')
            break
        else:
            print('prime')
s=input('enter the string:')
rev=" "
for i in s:
    rev=i+rev
print(rev)

si=input('enter the string')
rev= ""
for i in si:
    rev=i+rev

if si==rev:
    print('it is a palindrome')
else:
    print('not a palindrome')

ni=[1,2,3,3,4,1,2,4,5]
new=[]
for i in ni:
    if i not in new:
        new.append(i)
print(new)

ne=[11,12,13,14,15]
first=ne[0]
second=ne[0]
for i in ne:
    if i>first:
        first=i
    elif i>second and i!=first:
        second=i
            
print(first)
print(second)
