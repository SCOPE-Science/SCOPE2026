#!/usr/bin/env python3
"""Fixed binary adjacency-power checker for one-edge-defective complete subdivisions."""
from itertools import combinations

def xor_rank(rows):
    pivots = {}
    for v in rows:
        z=v
        while z:
            i=z.bit_length()-1
            if i in pivots: z ^= pivots[i]
            else:
                pivots[i]=z
                break
    return len(pivots)

def multiply(A,B):
    out=[]
    for row in A:
        z=0
        while row:
            bit=row & -row
            z ^= B[bit.bit_length()-1]
            row-=bit
        out.append(z)
    return out

def adjacency(n):
    E=list(combinations(range(n),2)); N=n+len(E)
    A=[0]*N
    for k,(a,b) in enumerate(E):
        for u in (a,b):
            if (a,b)==(0,1) and u==0: continue
            A[u] ^= 1<<(n+k)
            A[n+k] ^= 1<<u
    return A

def expected(n,t):
    N=n*(n+1)//2
    if n%2:
        return N if t==0 else 2*n
    vals=[N,2*n,n+3,6,5,4,3,2]
    return vals[t] if t<8 else 2

def check():
    for n in range(3,35):
        A=adjacency(n); N=len(A)
        cur=[1<<i for i in range(N)]
        saved={}
        for t in range(17):
            actual=xor_rank(cur)
            assert actual==expected(n,t),(n,t,actual,expected(n,t))
            if t in (1,2,7,8,9,14,15,16): saved[t]=cur
            cur=multiply(cur,A)
        if n%2:
            dims={1:n-3,2:2*(n-3),7:n,14:2*n}
            assert saved[15]==saved[1],n
            assert saved[8]!=saved[1],n
            assert saved[15]!=saved[8],n
        else:
            dims={1:1,2:2,7:1,14:2}
            assert saved[9]==saved[7],n
            assert saved[8]!=saved[7],n
        for t,dim in dims.items():
            plus_identity=[row^(1<<i) for i,row in enumerate(saved[t])]
            assert N-xor_rank(plus_identity)==dim,(n,t,N-xor_rank(plus_identity),dim)
        print('matrix n=%d vertices=%d ranks, periodic fixed spaces and iterate identities PASS'%(n,N))
    print('ALL_MATRIX_CHECKS_PASS')
if __name__=='__main__':check()
