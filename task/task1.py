mas=[1, 2,3,4,5,6,7,8,9]
p=1
s=0
for i in mas:
    p*=i
    s+=i
print(p,s)

#2вариант решения
mas=[1, 2,3,4,5,6,7,8,9]
p=1
s=0
for i in range(len(mas)):
   p*=mas[i]
   s+=mas[i]
print(p,s)
