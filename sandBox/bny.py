def  find_numbers(digit, start, end):
    digit = int(input("Enter a number that you want to look for: "))
    start = int(input("Enter a starting range: "))
    end = (int(input("please enter an ending number: ")))
    first_list = range(start, end + 1)
    for x in first_list:
        print (x)
        

find_numbers(0,0,0)