count = 1
total = 0

amount=int(input("How many numbers would you like to average?:"))
for count in range (amount):
    number = int(input("Please enter a number to average{0}:".format(count))
    count = count + 1
    total = number + total
    average = total /amount
print(average)    
