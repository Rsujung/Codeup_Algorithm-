n = input()
c = int(n, 16)
for i in range(1,16):
    print(n,'*','%X'%i,'=%X'%(c*i),sep='')