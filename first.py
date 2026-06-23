'''x=int(input("enter the number "))
y=int(input("enter the number "))

if (x%2==0):
    print("even")
else:
    print("odd")
if (x>0):
    print("positive")
else:
    print("negative")
if (x>y):
    print("x is greater ")
else:
    print("y is greater")
    


a=input("enter color")
if a=='red':
    print("stop ")
elif a=='yellow':
    print("slow down")
elif a=='green':
    print("proceed with caution")
else:
    print("blinded")
    print("traffic light malfunction !")


fruits=["apple","banana","cherry"]
for i in fruits:
    print(i)

    


count=1
while count<=1:
    print(f"countis{count}")
count+=1


sum=0
for i in range (11):
    sum+=i
print(sum)


num=5 ;fact=1
for i in range(1,num+1):
    fact*=i
print(fact)


numbers=[45,67,98,23,76]
largest =numbers[0]
for num in numbers :
    if num>largest :
        largest=num
print(largest)
'''

fruits=['apple','banana','cherry']
fruits.append("orange")
print(fruits[0])
