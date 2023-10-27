#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# take list of names and put it into a python list
with open('./Input/Names/invited_names.txt') as names_file:
    names_list = names_file.readlines()
    print("names_list = ", names_list)

# use readlines() to make each line of the letter a list
with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_lines = letter_file.readlines()
    print("letter_lines = ",letter_lines)

# take starting_letter and strip the [name] part of the text and isolate it using the strip() function
# loop through all names in the list (for loop) and replace [name] with an element of the list
txt = letter_lines[0]
for names in names_list:
    replaced_name = txt.replace('[name],\n', f'{names}')
    letter_lines[0] = replaced_name
    file = open(f'./Output/ReadyToSend/{names}.txt', 'w')
    for lines in letter_lines:
        file.write(lines)
    file.close()


