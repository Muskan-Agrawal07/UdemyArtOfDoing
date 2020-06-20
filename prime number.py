print("Welcome to the prime number program.\n\n")
print("Enter 1 to check if a no. is prime or not. ")
print("Enter 2 to find out the prime no.s in a given range. ")

running=True
while running:
    choice=int(input("Enter your choice(1/2). "))
    if choice==1:
        num1=int(input("Enter the number. "))
        non_num1=[1,num1]
        i=2
        if num1%i != 0 and i not in non_num1:
            print(num1,"is a prime number.")
            i+=1
        else:
            print(num1,"is not a prime number")
    elif choice==2:
        lower_range=int(input("Enter the lower range "))
        upper_range=int(input("Enter the upper range "))
        
        primes=[]
        for num in range(lower_range,upper_range+1):
            if num>1:
              for i in range(2,num):
                if (num%i)!=0 and i!=num:
                  primes.append(num)
        for prime in primes:
                print(prime)
            
    else:
        print("This is not a valid choice.")
    again=str(input("Would you like to run the program again?(y/n) ")).lower().strip()
    if again != "y":
        break
    else:
        continue
    
            
