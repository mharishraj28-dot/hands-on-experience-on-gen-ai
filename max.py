num=[12,13,14,78,80]
print('sum of the list:\n')
sum=0

for i in num:
    sum=sum+i
print(sum)

print('max of the list:\n')

print(max(num))

# max=lst[i]
#for i in num:
#     if i>max:
#         max=i
#print(max)

print('min of the list:\n')
print(min(num))

# min=lst[i]
#for i in num:
#     if i<min:
#         min=i
#print(max)

print('count the elements:')
count=0
for i in num:
    if i%2 ==0:
        count+=1
print(count)

no=list(filter(lambda a: a%2==0,num))
print(num,no)

print('average of list:')
for i in num:
    sum=sum+i
avg=sum/len(num)
print(avg)
print('fact of a num:')
noe=int(input('enter the no:'))
fact=1
for i in range(1,noe+1):
    fact=fact*i
print(fact)
