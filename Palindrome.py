def isPalindrome(s):
    def toChars(s) :
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz' :
                letters = letters + c 
        return letters

    def isPal(s) :
        if len(s) <= 1 :
            return True
        else :
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))   

n = input('Enter string: ')
print(isPalindrome(n))