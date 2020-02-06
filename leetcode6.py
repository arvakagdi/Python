def reverse(x):
    strn = ''
    if(x >= -2**31 and x<= 2**31-1):
        newz = 0
        a = []
        z = str(x)
        newz = list(z)

        if(x<0 and x>= -2**31):
            a = newz[0]
            newz = newz[len(newz)-1:0:-1]
            for i in newz:
                strn+=i
            strn = str(a) +strn

        else:    
            newz = newz[::-1]
            for i in newz:
                strn+=i

        return(int(strn))
    else:
        return 0

print(reverse(-123))


