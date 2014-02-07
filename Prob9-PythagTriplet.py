
for a in range(1,1000):
    for b in range(a+1, 1000):
        c = (a*a + b*b)**0.5
        if (a+b+c)==1000:
            if a<b and b<c:
                print str(a) + " " + str(b) + " " + str(c)
                print str(a*b*c)

                
