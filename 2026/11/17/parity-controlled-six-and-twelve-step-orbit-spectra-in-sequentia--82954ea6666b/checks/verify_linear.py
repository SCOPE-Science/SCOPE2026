"""Independent matrix-row construction and exact GF(2) rank verification."""
from functools import reduce
from operator import xor

def matrix_columns(k):
    n=2*k+1
    rows=[1<<i for i in range(n)]
    for i in range(n):
        if i==0:
            neigh=range(1,n)
        else:
            j=1+2*((i-1)//2)
            neigh=(0,j+1 if i==j else j)
        rows[i]^=reduce(xor,(rows[j] for j in neigh),0)
    return [sum((((rows[i]>>j)&1)<<i) for i in range(n)) for j in range(n)]

def multiply(a,b):
    n=len(a)
    return [reduce(xor,(a[i] for i in range(n) if (b[j]>>i)&1),0) for j in range(n)]

def rank(cols):
    pivots={}
    for col in cols:
        x=col
        while x:
            p=x.bit_length()-1
            if p in pivots:x^=pivots[p]
            else:pivots[p]=x;break
    return len(pivots)

def predicted_dim(k,t):
    if k%2==0:
        return 1 if t%3 else (2*k+1 if t%2==0 else 2*k-1)
    e=1 if t%2 else (2 if t%4 else 3)
    return e+2*(k-1)*(t%3==0)

def main():
    for k in range(1,41):
        n=2*k+1
        A=matrix_columns(k)
        identity=[1<<i for i in range(n)]
        for t in (1,2,3,4,5,6,9,12,15,18,20,24):
            B=identity
            for _ in range(t):B=multiply(A,B)
            dim=n-rank([B[i]^identity[i] for i in range(n)])
            assert dim==predicted_dim(k,t),(k,t,dim,predicted_dim(k,t))
        order=6 if k%2==0 else (4 if k==1 else 12)
        B=identity
        for _ in range(order):B=multiply(A,B)
        assert B==identity
        if order>1:
            B=identity
            for _ in range(order//2): B=multiply(A,B)
            assert B!=identity
        print('k=%d matrix-rank-profile PASS exact-order=%d'%(k,order))
    print('MATRIX PASS')
if __name__=='__main__':main()
