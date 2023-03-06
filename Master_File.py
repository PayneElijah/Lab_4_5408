import datetime


#time conversion from std. to military
def to_military_time(time):
    military_time = time.strftime("%H:%M")
    return military_time

#Print military time
current_time = datetime.datetime.now()
military_time = to_military_time(current_time)
print("Current time in military format: " + military_time)


## takes in user input for calculations
num = int(input("Enter a number to check if it is prime: "))

#if the number is greater than 1 it will check if the number has a remainder of 0
if num > 1:
    for i in range(2, int(num/2)+1):
        if(num % i) == 0:
            print(num, "is not a prime number")
            break
    #if the number surpasses the for loop, the number is resulted as prime
    else:
        print(num, "is a prime number")
#if the number is less than or equal to 1 it is not prime
else:
    print(num, "is not prime")