numbers = [12, 34, 7, 56, 89, 23, 54, 78, 91, 4] # the list of 10 ingegers

def print_list():
    print("the list of numbers is:", numbers) # function to print the list

def print_sum():
    total =sum(numbers)
    print("the sum of all elements is:", total) #function to print the sum

def print_largest():
    largest =max(numbers)
    print("the largest number of all elements is:", largest) #function to print the largest
    

def print_reverse():
    print("The list in reverse order is:", numbers[::-1])


def print_smallest(): #function to print the smallest number
    smallest = min(numbers)
    print("the smallest element in the list is:", smallest)
    
    

def main():
    print_list()
    print_sum()
    print_largest()
    print_reverse()

if __name__ == "__main__":
    main()
    
