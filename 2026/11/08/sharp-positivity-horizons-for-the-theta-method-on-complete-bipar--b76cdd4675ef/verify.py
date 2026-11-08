"""Exact rational replay for the theta-method positivity frontier on complete bipartite graphs.

Run: python verify.py
Only Python's standard library is required.
"""
from fractions import Fraction as F
from math import isqrt


def inverse(a):
    n=len(a)
    b=[[F(a[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot=next((i for i in range(k,n) if b[i][k]),None)
        assert pivot is not None
        b[k],b[pivot]=b[pivot],b[k]
        d=b[k][k]
        b[k]=[v/d for v in b[k]]
        for i in range(n):
            if i==k: continue
            d=b[i][k]
            if d:
                b[i]=[x-d*y for x,y in zip(b[i],b[k])]
    return [row[n:] for row in b]


def matrices(p,q,theta,h):
    n=p+q; t=theta*h
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(p):
        for j in range(p,n):
            L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
    R=inverse([[F(i==j)+t*L[i][j] for j in range(n)] for i in range(n)])
    T=[[R[i][j]/theta - (1-theta)/theta*F(i==j) for j in range(n)] for i in range(n)]
    return R,T


def block_resolvent(p,q,t,i,j):
    n=p+q
    x=F(1,n)
    if i<p and j<p:
        x+= (F(i==j)-F(1,p))/(1+q*t)
        x+= F(q,p*n)/(1+n*t)
    elif i>=p and j>=p:
        x+= (F(i==j)-F(1,q))/(1+p*t)
        x+= F(p,q*n)/(1+n*t)
    else:
        x-= F(1,n)/(1+n*t)
    return x


def polynomial(p,q,theta,h):
    m=min(p,q);M=max(p,q);n=m+M;t=theta*h
    return theta+(m*theta+M*(2*theta-1))*t -M*((n-1)-n*theta)*t*t


def test():
    count=0
    thetas=[F(1,6),F(1,3),F(1,2),F(2,3),F(3,4),F(7,8),F(1)]
    steps=[F(0),F(1,10),F(1,2),F(1),F(2),F(5),F(20)]
    for p in range(1,6):
      for q in range(1,6):
       if p+q<3:continue
       for theta in thetas:
        for h in steps:
         R,T=matrices(p,q,theta,h)
         n=p+q;t=theta*h
         assert all(R[i][j]==block_resolvent(p,q,t,i,j) for i in range(n) for j in range(n))
         assert all(sum(T[i])==1 for i in range(n))
         assert all(T[i][j]>0 for i in range(n) for j in range(n) if i!=j and h>0)
         predicted=theta>=F(n-1,n) or polynomial(p,q,theta,h)>=0
         actual=all(v>=0 for row in T for v in row)
         assert actual==predicted, (p,q,theta,h)
         if h>0:
             min_diag=min(T[i][i] for i in range(n))
             if p<q:assert all(T[i][i]==min_diag for i in range(p))
             if q<p:assert all(T[i][i]==min_diag for i in range(p,n))
         count+=1
    # Explicit Euler endpoint and strict balance comparison, exactly.
    for n in range(3,40):
      for m in range(1,n//2+1):
       M=n-m
       assert F(1,M)>0
       for h in [F(1,n),F(2,n),F(4,n),F(8,n)]:
        p,q=m,M
        assert (h<=F(1,M)) == (1-M*h>=0)
       for theta in [F(1,4),F(1,2),F(3,4)]:
        if theta>=F(n-1,n):continue
        for t in [F(1,5*n),F(1,n),F(1),F(2)]:
         old=theta+(m*theta+M*(2*theta-1))*t-M*((n-1)-n*theta)*t*t
         if m<n//2:
          mp=m+1;Mp=M-1
          new=theta+(mp*theta+Mp*(2*theta-1))*t-Mp*((n-1)-n*theta)*t*t
          assert new>old
    # Check the Crank-Nicolson n=4 examples with exact threshold signs.
    assert polynomial(1,3,F(1,2),F(1))==0
    assert polynomial(2,2,F(1,2),F(1))>0
    assert polynomial(2,2,F(1,2),F(2))<0
    print('VERIFY_OK',count,'full exact-rational matrix cases; endpoint, ordering and boundary checks')

if __name__=='__main__':test()
