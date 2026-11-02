"""Exact-rational structure checks and independent small LP cross-checks for transportation centers."""
from fractions import Fraction as F
from itertools import product
import random


def theorem(r,c):
    assert len(r)>=2 and len(c)>=2 and all(t>0 for t in r+c) and sum(r)==sum(c)
    U=[[min(a,b) for b in c] for a in r]
    beta=max([sum(row)/a for row,a in zip(U,r)]+[sum(U[i][j] for i in range(len(r)))/b for j,b in enumerate(c)])
    L=[[v/beta for v in row] for row in U]
    R=[a-sum(row) for a,row in zip(r,L)]
    C=[b-sum(L[i][j] for i in range(len(r))) for j,b in enumerate(c)]
    assert beta>=2 and all(t>=0 for t in R+C) and sum(R)==sum(C)
    ri=[i for i,v in enumerate(R) if v>0]
    ci=[j for j,v in enumerate(C) if v>0]
    d=(len(ri)-1)*(len(ci)-1) if sum(R)>0 else 0
    if sum(R):
        center=[[L[i][j]+R[i]*C[j]/sum(R) for j in range(len(c))] for i in range(len(r))]
    else:
        center=L
    assert all(sum(row)==a for row,a in zip(center,r))
    assert all(sum(center[i][j] for i in range(len(r)))==b for j,b in enumerate(c))
    assert all(beta*center[i][j]>=U[i][j] for i in range(len(r)) for j in range(len(c)))
    minrow=min(r);mincol=min(c)
    betashort=max(sum(min(F(1),b/minrow) for b in c),sum(min(F(1),a/mincol) for a in r))
    assert beta==betashort
    return beta, d, U, center, R, C


def test_independent_lp(r,c,beta):
    import numpy as np
    from scipy.optimize import linprog
    m,n=len(r),len(c)
    eq=[];rhs=[]
    for i in range(m):
        row=[0.]*(m*n+1)
        for j in range(n):row[i*n+j]=1.
        row[-1]=-float(r[i]);eq.append(row);rhs.append(0.)
    for j in range(n):
        row=[0.]*(m*n+1)
        for i in range(m):row[i*n+j]=1.
        row[-1]=-float(c[j]);eq.append(row);rhs.append(0.)
    U=[min(a,b) for a in r for b in c]
    obj=[0.]*(m*n)+[1.]
    sol=linprog(obj,A_eq=eq,b_eq=rhs,bounds=[(float(u),None) for u in U]+[(0,None)],method='highs')
    assert sol.success, sol.message
    assert abs(sol.x[-1]-float(beta))<1e-8,(r,c,sol.x[-1],beta)
    # Also optimize each coordinate on the original transportation polytope.
    eq2=[];rhs2=[]
    for i in range(m):
        row=[0.]*(m*n)
        for j in range(n):row[i*n+j]=1.
        eq2.append(row);rhs2.append(float(r[i]))
    for j in range(n):
        row=[0.]*(m*n)
        for i in range(m):row[i*n+j]=1.
        eq2.append(row);rhs2.append(float(c[j]))
    for i,j in product(range(m),range(n)):
        o=[0.]*(m*n);o[i*n+j]=-1.
        v=linprog(o,A_eq=eq2,b_eq=rhs2,bounds=(0,None),method='highs')
        assert v.success and abs(-v.fun-float(U[i*n+j]))<1e-8


def main():
    rng=random.Random(20261010)
    count=0
    for m,n in product(range(2,6),range(2,6)):
        for k in range(40):
            r=[F(rng.randrange(1,24)) for _ in range(m)]
            w=[F(rng.randrange(1,24)) for _ in range(n)]
            c=[sum(r)*t/sum(w) for t in w]
            beta,d,_,_,_,_=theorem(r,c)
            if m<=4 and n<=4 and k<5: test_independent_lp(r,c,beta)
            count+=1
    for n in range(2,10):
        r=[F(1)]*n;c=[F(1)]*n
        beta,d,*_=theorem(r,c)
        assert beta==n and d==0
    print(f'PASS exact rational instances={count+8}; independent LP instances={9*5}; Birkhoff checks=8')

if __name__=='__main__':main()
