'''n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')
print(n)'''

#count of no of factors of n

'''n=int(input())
count=0
for i in range(1,n//2+1):
    if n%i==0:
        count+=1
print(count+1)'''

#check whether n is prime or not
'''n=int(input())
count=0
for i in range(1,n//2+1):
    if n%i==0:
        count+=1
print("Prime" if count==0 else "Not Prime")'''

#print all the prime numbers between 1 and n
'''start=int(input())
end=int(input())
for i in range(start,end+1):
    count=0
    for j in range(1,i//2+1):
        if i%j==0:
            count+=1
    if count==0:
        print(i,end=' ')'''

#read a nuumber from user and display factorial of a number
'''n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)'''

#GCD of two numbers
'''a=int(input())
b=int(input())
gcd=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
print(gcd)'''

#