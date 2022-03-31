# No importing
# Read the text file 'mbox-short.txt' line by line
# Parse the 'From' like and use .split() to get the email adress of the person who sent the line (usually second word in line)
# Print a count at the end (i.e, "There were 27 lines in the file with From as the first word.")
# HINT: DO NOT USE 'From:'
# Use: 'From' only

print('Scanning mbox-short.txt...')
print('Done!')
print('')

n = 0
emailscript = []
emailist = []
emails = []

# epath = 'D:/mbox-short.txt'                                                   # USB path / Home path
epath = 'I:/Testing/mbox-short.txt'                                             # School path
emailscript = open(epath, 'r')                                                  # Opens path to mbox-short.txt for reading
emailscript = emailscript.readlines()                                           # Reads lines

emailscript = " ".join(emailscript)                                             # Makes script into string so the program can read it
emailscript = emailscript.split(' ')                                            # Splits it into list for searching (one entry per word)

length = len(emailscript)                                                       # Taking length for while loop
search = 'From'                                                                 # Variable for while loop - Searching for string 'From'
count = emailscript.count(search)                                               # Takes note of how many 'From's there are (Mostly for debug but output in final result)

emailist.append(1)                                                              # Wouldn't work with my while loop or if statement logic so I manusally appended it

while n < length:                                                               # Loops until all the words are checked
    if search == emailscript[n]:                                                # Search for 'From'
        emailist.append(n + 1)                                                  # If 'From' is found append the item next in the list to a different list (for tracking position)
        n = n + 1                                                               # Increments counter to check next item in list
    else:
        n = n + 1                                                               # Increments counter even if false to keep loop from getting stuck
        pass

print(emailist)                                                                 # emailist is a list with the stored locations of every email

for x in emailist:                                                              # Takes numbers from emailist and uses those to grab the emails from emailscript
    emails.append(emailscript[x])                                               # Final output list of all the emails

print(emails)
print('')
print(f"The word '{search}' is present in the document {count + 1} times!")     # NEW WAY TO FORMAT MESSAGES!!! 
                                                                                # +1 added to account for manually parsed email

input('-Press Enter to Exit-')                                                  # Prevents the program from closing prematurely