def isPalindrome(s):
    
    rev = ''.join(reversed(s))
 
    # Checking if both string are
    # equal or not
    if (s == rev):
        return True
    return False
 
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes,it is a palindrome")
else:
    print("No,not a palindrome")