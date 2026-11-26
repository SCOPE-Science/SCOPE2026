"""Exact finite-field Kalman tests for a matched-weight complete bipartite network.
This is corroboration of, not a substitute for, the analytical PBH argument.
"""
from itertools import combinations

def mat(n,a,b):
    d=(n-1)*a+b
    A=[[0]*(2*n) for _ in range(2*n)]
    for i in range(2*n):A[i][i]=d
    for i in range(n):
        for j in range(n):
            A[i][n+j]=A[n+j][i]=-(b if i==j else a)
    return A

def rank_mod(columns,p=1000003):
    basis={}
    for col in columns:
        v=[int(x)%p for x in col]
        for pivot,w in sorted(basis.items()):
            f=v[pivot]
            if f:
                v=[(x-f*y)%p for x,y in zip(v,w)]
        j=next((i for i,x in enumerate(v) if x),None)
        if j is not None:
            z=pow(v[j],-1,p)
            v=[(z*x)%p for x in v]
            # Maintain reduced pivot columns even if a new pivot is earlier.
            for old,w in list(basis.items()):
                f=w[j]
                if f:
                    basis[old]=[(x-f*y)%p for x,y in zip(w,v)]
            basis[j]=v
    return len(basis)

def rank_kalman(L,T):
    N=len(L)
    if not T:return 0
    cur=[[int(i==j) for i in range(N)] for j in T]
    cols=[]
    for _ in range(N):
        cols+=cur
        if rank_mod(cols)==N:return N
        cur=[[sum(L[i][j]*v[j] for j in range(N))%1000003 for i in range(N)] for v in cur]
    return rank_mod(cols)

def predicted(n,b,a,T):
    S=set(T)
    if b==a:
        return sum(i in S for i in range(n))>=n-1 and sum(n+i in S for i in range(n))>=n-1
    return sum((i in S) or (n+i in S) for i in range(n))>=n-1

def verify():
    checks=0
    for n in (3,4):
        for a,b in ((1,0),(1,1),(1,2),(2,1),(2,3)):
            L=mat(n,a,b)
            for mask in range(1<<(2*n)):
                T=[i for i in range(2*n) if mask>>i &1]
                got=(rank_kalman(L,T)==2*n)
                expected=predicted(n,b,a,T)
                assert got==expected,(n,a,b,T,got,expected)
                checks+=1
    import random
    R=random.Random(960104)
    for n in (5,6,7):
        for a,b in ((1,0),(1,1),(1,2),(3,1)):
            L=mat(n,a,b)
            masks=[R.getrandbits(2*n) for _ in range(28)]
            masks+= [(1<<n)-1, (1<<(2*n))-1, 0]
            for mask in masks:
                T=[i for i in range(2*n) if mask>>i &1]
                assert (rank_kalman(L,T)==2*n)==predicted(n,b,a,T),(n,a,b,T)
                checks+=1
    # Independently tally optimal actuator placements and generating polynomials.
    for n in range(3,8):
        for a,b in ((1,0),(1,1),(1,2)):
            counts=[0]*(2*n+1)
            for mask in range(1<<(2*n)):
                T=[i for i in range(2*n) if mask>>i &1]
                if predicted(n,b,a,T):counts[len(T)]+=1
            from math import comb
            # Coefficients of q(z)^n+n q(z)^(n-1), q(z)=2z+z^2.
            if b!=a:
                for k in range(2*n+1):
                    c1=comb(n,k-n)*2**(2*n-k) if n<=k<=2*n else 0
                    c2=n*comb(n-1,k-n+1)*2**(2*n-2-k) if n-1<=k<=2*n-2 else 0
                    assert counts[k]==c1+c2,(n,a,b,k,counts[k],c1+c2)
                    checks+=1
                assert counts[n-1]==n*2**(n-1)
            else:
                for k in range(2*n+1):
                    expected={2*n-2:n*n,2*n-1:2*n,2*n:1}.get(k,0)
                    assert counts[k]==expected,(n,a,b,k,counts[k],expected)
                    checks+=1
                assert counts[2*n-2]==n*n
            # Independent subset sum versus the closed reliability law, exactly.
            from fractions import Fraction
            for p in (Fraction(1,3),Fraction(2,3)):
                lhs=sum(counts[k]*p**k*(1-p)**(2*n-k) for k in range(2*n+1))
                if b!=a:
                    q=p*(2-p)
                    rhs=q**n+n*(1-p)**2*q**(n-1)
                else:
                    rhs=(p**n+n*(1-p)*p**(n-1))**2
                assert lhs==rhs,(n,a,b,p,lhs,rhs)
                checks+=1
    return checks

if __name__=='__main__':print('VERIFY_OK',verify(),'checks')
