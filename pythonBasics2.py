# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
      #converting the integer into the list of digits
        n = list(str(n))
        #declaring a dictionary for keeping the count
        d ={}
        #loop to initialize all multiples of three in the dict as 0
        d[3] = d[6] = d[9] = 0

        #loop to iterate over list and count the frequencies of multiples of three
        for i in n:
                j = int(i)
                if j%3 == 0 and j!=0:
                        d[j] = d[j] + 1

        #last step is to iterate over the dict and find out digit with max freq
        maximum = -1
        index = -1
        for k,v in d.items():
                if v > maximum :
                        maximum = v
                        index = k

        #and returning the number finally
        return index



# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
        s = list(s)
        l = len(s)
        cnt = 1
        #declaring the dictionary to keep track of frequencies
        d ={}

        #counting frequency of every char
        for i in range(0,l-1):
                if(s[i] != s[i+1]):
                      if((s[i] in d) and d[s[i]] > cnt ):
                             continue
                      else:
                             d[s[i]] = cnt
                             cnt = 1
                else:
                      cnt = cnt + 1

        d[s[l-1]] = cnt

        #finding the maximum frequency
        maximum = -1
        for k,v in d.items():
                if v > maximum :
                        maximum = v

        #adding the chars to the list with max frequency
        lst = []
        for k,v in d.items():
                if v == maximum :
                        lst.append(k)

        return lst

# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
    i = 0
    j = len(s)-1
    while i <= j:
        if s[i] == ' ':
            i += 1
            continue
        if s[j] == ' ':
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
        return True
