#!/usr/bin/env python3
"""Independent finite LP and exact inequality checks for parking-polytope asymmetry."""
import itertools
from fractions import Fraction
from math import isclose
from scipy.optimize import linprog

def case(b):
    n=len(b)
    S=list(itertools.accumulate(b)); A=sum(S); T=A-n; B=S[-1]-1
    assert T>0
    s=Fraction(n*B,T); t=Fraction(S[-1]*T+n*B,T+n*B)
    assert t == (s+S[-1])/(1+s)
    U={k:sum(S[-k:]) for k in range(1,n+1)}
    # Exact support checks, including all n coordinates and 2^n-1 subset constraints.
    for mask in range(1,1<<n):
        k=mask.bit_count()
        assert (s+1)*k*t <= s*U[k]+k
        for h in range(n):
            if mask&(1<<h):
                assert (s+1)*t>=s+S[-1]
    # Independent LP of transformed containment inequalities for every facet.
    Aub=[]; bb=[]
    # -y_i+s <= -S_n
    for i in range(n):
        a=[0.]*(n+1); a[i]=-1.;a[-1]=1.;Aub.append(a);bb.append(-S[-1])
    for mask in range(1,1<<n):
        k=mask.bit_count();a=[float(bool(mask>>i&1)) for i in range(n)]+[-float(U[k])]
        Aub.append(a);bb.append(k)
    sol=linprog([0.]*n+[1.],A_ub=Aub,b_ub=bb,bounds=[(None,None)]*n+[(1.,None)],method='highs')
    assert sol.success,(b,sol.message)
    assert isclose(sol.fun,float(s),rel_tol=1e-9,abs_tol=1e-9),(b,sol.fun,s)
    for i in range(n): assert isclose(sol.x[i]/(1.+sol.fun),float(t),rel_tol=1e-9,abs_tol=1e-9),(b,i,sol.x)
    return s

if __name__=='__main__':
    cnt=0;values=[]
    for n in range(2,6):
        for b in itertools.product(range(1,4),repeat=n):
            val=case(b);values.append((n,b,val));cnt+=1
    # Exact classical values and example.
    for n in range(2,9): assert case((1,)*n)==2
    for n in range(2,8):
        for t in (10,100,1000):
            b=(t,)+(1,)*(n-1)
            assert Fraction(1)<case(b)<Fraction(n)
            b=(2,)+(1,)*(n-2)+(t,)
            assert Fraction(1)<case(b)<Fraction(n)
    print('PARKING_ASYMMETRY_CHECKS_PASSED',cnt,7,30)
