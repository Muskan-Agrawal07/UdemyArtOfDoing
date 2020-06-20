print("Welcome to the Factor generator program.\n\n")
num=int(input("Enter a number to determine it's factors"))
factors=[]
n=1
while bool(n<=num):
    if num%n==0:
        factors.append(n)
    n+=1
for i in factors:
        print (i)
for i in range(int(len(factors)/2)):
    print(factors[i]," * ",factors[-i-1]," = ",num)
   
