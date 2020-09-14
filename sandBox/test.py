def findall(L, value, start=0):
        i = start - 1
        try:
            i = L.index(value, i+1)
            yield i
        except ValueError:
            pass

for index in findall(L, value):
        print ("match at", i)

findall(1,2,3)