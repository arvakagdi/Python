def lengthOfLongestSubstring(s):
    newtotal = 0
    newstr = ''
    for i in range(0,len(s)):
        if s[i] not in newstr:
            newstr = newstr + s[i]

        else:
            if(len(newstr) > newtotal):
                newtotal = len(newstr)
                n = newstr.find(s[i])
                newstr = newstr[n+1:]
                newstr = newstr + s[i]
            else:
                n = newstr.find(s[i])
                newstr = newstr[n+1:]
                newstr = newstr + s[i]

        if i == len(s)-1:
            if(len(newstr) > newtotal):
                newtotal = len(newstr)

    return (newtotal)

print(lengthOfLongestSubstring("jbpnbwwd"))
            
    
