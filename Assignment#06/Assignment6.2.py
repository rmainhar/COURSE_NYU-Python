'''
Assignment 6 Part 2
'''


# Enter an integer between 1 and 100,000
while True:
    number = int(input("Enter a number: "))
    if number >= 1 and number <= 100000:
        break
    print("Sorry, the number shoule be within 1 and 100000.")

# Def: test if the number is even
# Input: the number
def isEven(x):
    # Process: judge if is an even
    if (x%2 == 0):
        return True
    else:
        return False

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
# is even?            
if(isEven(number)):
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")
    
# is prime? 
if(isPrime(number)):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")

while True:
      ans = input("Would you like to enter another number? (yes/no): ")
      if (ans == 'no'):
          break
      while True:
        number = int(input("Enter a number: "))
        if number >= 1 and number <= 100000:
            break
        print("Sorry, the number shoule be within 1 and 100000.")
      if(isEven(number)):
        print(number, "is an even number.")
      else:
        print(number, "is an odd number.")
      if(isPrime(number)):
        print(number, "is a prime number")
      else:
        print(number, "is not a prime number")











      
