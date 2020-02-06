def longestPalindrome(s):
    newstr = ''
    for i in range(0,len(s)):
        for j in range (len(s)-1, i, -1):
            if s[i] == s[j]:
                newstr = newstr + s[i]

    newstr = newstr + newstr[:1:-1]
    return(newstr)

s = 'jdhfdavadfdlksjdk'
print(longestPalindrome(s))