#!/usr/bin/env python3
"""Self-contained exhaustive checks for majority-rule transient census on rings."""
from collections import Counter

def step(x,n):
    y=0
    for i in range(n):
        a=(x>>((i-1)%n))&1
        b=(x>>i)&1
        c=(x>>((i+1)%n))&1
        y|=((a+b+c)>=2)<<i
    return y

def direct_entry(x,n):
    y=x
    for t in range(n+2):
        z=step(y,n)
        if z==y: return t,1
        if step(z,n)==y: return t,2
        y=z
    raise AssertionError('nonperiodic beyond proven limit')

def bond_prediction(x,n):
    b=[int(((x>>i)&1)==((x>>((i+1)%n))&1)) for i in range(n)]
    if not any(b):return 0,2
    ones=[i for i,v in enumerate(b) if v]
    gaps=[(ones[(j+1)%len(ones)]-ones[j]-1)%n for j in range(len(ones))]
    return max(g//2 for g in gaps),1

def trace_count(n,max_zero):
    s=2*(max_zero+1)
    M=[[0]*s for _ in range(s)]
    for k in range(max_zero+1):
        for parity in range(2):
            i=2*k+parity
            M[i][parity]+=1 # append a 1, reset run k to zero
            if k<max_zero:
                M[i][2*(k+1)+(parity^1)]+=1 # append a zero
    def matmul(A,B):
        out=[[0]*s for _ in range(s)]
        for i in range(s):
            for k,v in enumerate(A[i]):
                if v:
                    for j,w in enumerate(B[k]):
                        if w:out[i][j]+=v*w
        return out
    P=[[int(i==j) for j in range(s)] for i in range(s)]
    for _ in range(n):P=matmul(P,M)
    return sum(P[i][i] for i in range(s))

if __name__=='__main__':
    total=0
    for n in range(3,19):
        direct=Counter()
        for x in range(1<<n):
            d=direct_entry(x,n)
            assert d==bond_prediction(x,n),(n,x,d,bond_prediction(x,n))
            direct[d]+=1
        m=(n-1)//2
        assert sum(v for (t,p),v in direct.items() if t==m)==2*n,(n,direct)
        assert direct[(0,2)]==(2 if n%2==0 else 0),n
        for t in range(m+1):
            predicted=trace_count(n,2*t+1)+(2 if n%2==0 else 0)
            actual=sum(v for (s,p),v in direct.items() if s<=t)
            assert predicted==actual,(n,t,predicted,actual)
        print('n=%2d states=%6d max_time=%d maximizers=%d'%(n,2**n,m,2*n))
        total+=2**n
    print('VERIFY_OK total_initial_configurations=',total)
