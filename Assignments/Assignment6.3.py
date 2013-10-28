'''
Assignment 6 Part 3
'''



# Enter a range by the user

while True:
    first = int(input("Entet the first number in your range (integer): "))
    if first > 0:
        break
    print("Sorry, please enter a positive number.")

while True:
    second = int(input("Entet the second number in your range (integer): "))
    if second > 0 and second > first :
        break
    print("Sorry, please enter a positive number larger than your first number.")



# Def: test if it is prime
# Input: the user's number
def isPrime(x):
    # Process: if the number cannot be
    # divided by any other number than itself
    if (x == 2):
        judge2 = True
    else:
        # To judge whether it is a prime
        n = 2
        while(n < x):
            if (x%n == 0):
                return False
            n += 1
            return True


# Main function
for n in range(first, second):
  if isPrime(n):
      print(n, "is a prime number.")
while True:
    ans = input("Would you like to analyze another range? (yes/no): ")

    if (ans == "no"):
        break
    while True:
        first = int(input("Entet the first number in your range (integer): "))
        if first > 0:
            break
        print("Sorry, please enter a positive number.")

    while True:
        second = int(input("Entet the second number in your range (integer): "))
        if second > 0 and second > first :
            break
        print("Sorry, please enter a positive number larger than your first number.")

    for n in range(first, second):
      if isPrime(n):
          print(n, "is a prime number.")

    
      
