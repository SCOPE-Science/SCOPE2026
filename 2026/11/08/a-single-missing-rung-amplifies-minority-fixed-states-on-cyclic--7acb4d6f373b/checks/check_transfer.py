"""Exact integer transfer proof checks for one-rung-defective cubic ladders.
Standard Python only. Usage: python3 checks/check_transfer.py
"""
from itertools import product
N=16

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def add(A,B,a=1,b=1):
    return [[a*A[i][j]+b*B[i][j] for j in range(N)] for i in range(N)]
def trace(A):return sum(A[i][i] for i in range(N))
I=[[int(i==j) for j in range(N)] for i in range(N)]
Z=[[0]*N for _ in range(N)]
T=[[0]*N for _ in range(N)]
B=[[0]*N for _ in range(N)]
D=[[0]*N for _ in range(N)]

def local(a,b,c,missing=False):
    for row in (0,1):
        bit=(b>>row)&1
        opposite=int(bit!=((a>>row)&1))+int(bit!=((c>>row)&1))
        if not missing:opposite+=int(bit!=((b>>(1-row))&1))
        if opposite<(1 if missing else 2):return False
    return True

def flip(t):return ((t&1)<<1)|((t>>1)&1)
for a,b,c in product(range(4),repeat=3):
    i,j=4*a+b,4*b+c
    T[i][j]=int(local(a,b,c))
    B[i][j]=int(local(a,b,c,True))
for a,b in product(range(4),repeat=2):D[4*a+b][4*flip(a)+flip(b)]=1
assert sum(map(sum,T))==20 and sum(map(sum,B))==36
powers=[I]
for _ in range(33):powers.append(matmul(powers[-1],T))
# Exact matrix identity: T^2 (T^2 - T - I)(T^6 - I) = 0.
factor=matmul(matmul(powers[2],add(add(powers[2],T,1,-1),I,1,-1)),add(powers[6],I,1,-1))
assert factor==Z

def fib(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a
circ=[6,-3,1,4,-1,-1]
twist=[-2,3,3,-4,5,1]
for n in range(3,31):
    for d in (0,1):
        val=trace(matmul(powers[n-1],matmul(B,D if d else I)))
        predicted=3*fib(n)+(twist if d else circ)[n%6]
        assert val==predicted,(n,d,val,predicted)
    if n<=18:
        print(f'n={n:2d} circle={3*fib(n)+circ[n%6]:6d} mobius={3*fib(n)+twist[n%6]:6d} OK')
print('PASS exact matrix annihilator; all formula values n=3..30; recurrence order eight')
