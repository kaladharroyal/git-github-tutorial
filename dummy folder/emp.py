try:
    # Read a number from a file
    with open('number.txt', 'r') as f:#opening file in read mode 
        text = f.read() #reading data
    number = int(text) #convering data into integer
    result = 100 / number #dividing 100 by number
    print(f"Result: {result}")
except FileNotFoundError:
    print("Could not find number.txt")
except ValueError:# checks the value 
    print("File doesn't contain a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("program execution completed.")