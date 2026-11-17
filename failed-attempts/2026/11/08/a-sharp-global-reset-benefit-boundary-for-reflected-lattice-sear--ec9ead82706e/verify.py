"""Exact, independent finite checks for a reflecting-path reset theorem.
Run: python3 verify.py. No nonstandard packages are needed.
"""
from fractions import Fraction as Q


def solve(a,b):
    n=len(b); a=[list(map(Q,row))+[Q(rhs)] for row,rhs in zip(a,b)]
    for k in range(n):
        j=next(j for j in range(k,n) if a[j][k])
        a[k],a[j]=a[j],a[k]
        c=a[k][k];a[k]=[v/c for v in a[k]]
        for i in range(n):
            if i!=k:
                c=a[i][k]
                if c:a[i]=[a[i][j]-c*a[k][j] for j in range(n+1)]
    return [a[i][-1] for i in range(n)]


def expected_time(n,k,r):
    # transient states 1,...,n; absorption at 0; at n a forced inward step.
    # each step resets to k with probability r, and otherwise follows SRW.
    P=[[Q(0) for j in range(n)] for i in range(n)]
    for i in range(1,n+1):
        moves=[(i-1,Q(1,2)),(i+1,Q(1,2))] if i<n else [(n-1,Q(1))]
        for j,p in moves:
            if j:P[i-1][j-1]+=(1-r)*p
        P[i-1][k-1]+=r
    A=[[int(i==j)-P[i][j] for j in range(n)] for i in range(n)]
    return solve(A,[Q(1)]*n)[k-1]


def cheb(n,x):
    if n==0:return Q(1)
    a,b=Q(1),x
    for j in range(2,n+1):a,b=b,2*x*b-a
    return b


def coefficients(n):
    prev=[1];cur=[1,1]
    if n==0:return prev
    if n==1:return cur
    for j in range(2,n+1):
        nxt=[0]*(j+1)
        for i,t in enumerate(cur):nxt[i]+=2*t;nxt[i+1]+=2*t
        for i,t in enumerate(prev):nxt[i]-=t
        prev,cur=cur,nxt
    return cur

checks=0
for n in range(1,19):
    for k in range(1,n+1):
        a=n-k; m=n*n-a*a; delta=5*a*a-n*n-5
        cN=coefficients(n);cA=coefficients(a)
        def C(c,j):return c[j] if 0<=j<len(c) else 0
        co=[C(cN,j)-C(cA,j)+C(cN,j-1)-(m+1)*C(cA,j-1) for j in range(n+2)]
        assert co[0]==co[1]==0
        assert 6*co[2]==m*(n*n+5-5*a*a)
        if delta<=0:assert all(v>=0 for v in co)
        else:assert co[2]<0
        checks+=4
        assert expected_time(n,k,Q(0))==m;checks+=1
        for r in (Q(1,11),Q(1,4),Q(3,5)):
            x=1/(1-r)
            formula=(cheb(n,x)/cheb(a,x)-1)/r
            independent=expected_time(n,k,r)
            assert formula==independent,(n,k,r,formula,independent)
            if delta<=0:assert independent>m,(n,k,r,m,independent)
            checks+=2
print('VERIFY_OK',checks,'exact assertions')
