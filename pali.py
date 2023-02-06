def isPalindrome(s):
    return s == s[::-1]

s = input ("Enter the String: ")
ans = isPalindrome(s)

if ans:
	print(s+" is Palindrome")
else:
	print(s+"is not a Palindrome")
