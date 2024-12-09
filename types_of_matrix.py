n = 6
res = []
#----------------------> diagonal matrix
diag = [1 , 2 ,3]
for i in range(len(diag)):
    res.append([0]*(len(diag)))
    res[i][i] = diag[i]
#---------------------> eye matrix
for i in range(n):
    res.append([0]*(n))
    res[i][i] = 1
#-------------------> ones matrix
dim = [3 ,6 ]
for row in range(dim[0]+1):
    res.append([1]*dim[1])
#-------------------> identity matrix
for i in range(n):
    res.append([1]*(n))
#-------------------> zeros matrix
for i in range(n):
    res.append([0]*(n))
#--------------------> arange
arange = [1 , 5 , 0.1] 
#start , end , step
a = arange[0]
res = [a]
while True:
    if a+arange[2] < arange[1]:
        a+=arange[2]
        res.append(a)
    else:
        break
#------------------> reahape
data = list(range(1 , 26))
reshap = [5 , 5]
res = []
if len(data) == reshap[0]*reshap[1]:
    counter = 0
    for i in range(reshap[0]):
        res.append([])
        for x in range(reshap[1]):
            res[i].append(data[counter])
            counter+=1
"""
for i in res:
    print(i)
"""
