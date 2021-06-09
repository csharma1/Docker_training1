def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

# check if the number of terms is valid
num = int(input("Enter a number to Find Fib sequence : "))
if num <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   fib=[]
   for i in range(num):
       fib.append(recur_fibo(i))
print (fib)
