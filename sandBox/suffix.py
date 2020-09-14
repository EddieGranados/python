#  python program to segregate suffix from a given array of strings
 
# lets take input from the user i.e list of words with suffix "s" and also with "S"

input_string = input("Enter words ending with 's' and without 's' : ")

test_list = input_string.split()

# now provide a letter suffix which you want to remove/segregate from the word

end_letter = "s"

# print original list

print("The original list is  : " + str(test_list))

# now using list comprehension + endswith ()

with_s = [x for x in test_list if x.endswith(end_letter)]

without_s = [x for x in test_list if x not in with_s]

# printing the result

print("The list without suffix 's' : "+str(without_s))
print("The list with suffix 's' : "+str(with_s))