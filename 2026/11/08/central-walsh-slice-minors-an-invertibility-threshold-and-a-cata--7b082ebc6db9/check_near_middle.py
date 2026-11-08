#!/usr/bin/env python3
"""Independent finite checks for signed Walsh matrices on central Johnson slices."""
from itertools import combinations
from math import comb
import numpy as np

def catalyst(h):
    return comb(2*h,h)//(h+1)

def coefficients(k,a):
    assert a in (0,1,2)
    result=[]
    for j in range(k+1):
        m=k-j
        val=sum((-1)**t *comb(m,t)*comb(a,m-2*t) for t in range(m//2+1) if 0<=m-2*t<=a)
        if a==0:
            exp=0 if m%2 else (-1)**(m//2)*comb(m,m//2)
        elif a==1:
            exp=(-1)**(m//2)*comb(m,m//2)
        else:
            exp=(-1)**(m//2)*(catalyst(m//2) if m%2==0 else 2*comb(m,m//2))
        assert val==exp,(k,a,j,val,exp)
        result.append((-2)**j*exp)
    return result

def check(k,a):
    n=2*k+a
    sets=[sum(1<<t for t in S) for S in combinations(range(n),k)]
    H=np.array([[(-1)**((u&v).bit_count()) for v in sets] for u in sets],dtype=np.float64)
    computed=np.linalg.eigvalsh(H)
    eigen=coefficients(k,a)
    expected=np.array(sorted(sum(([z]*(comb(n,j)-(comb(n,j-1) if j else 0)) for j,z in enumerate(eigen)),[])),dtype=float)
    assert len(computed)==len(expected)
    assert np.max(abs(computed-expected))<1.e-7,(k,a,np.max(abs(computed-expected)))
    if a==0:
        assert sum(x!=0 for x in expected)==comb(n,k)//2
    else:
        h=k//2
        cond= (2**k/comb(k,k//2)) if a==1 else 4**h/catalyst(h)
        nonzero=np.abs(computed)
        actual=nonzero.max()/nonzero.min()
        assert abs(actual/cond-1)<1.e-9,(k,a,cond,actual)
    return (n,k,a,len(sets),round(float(np.min(computed)),5),round(float(np.max(computed)),5))

if __name__=='__main__':
    checked=[]
    for k in range(1,5):
        for a in (0,1,2):
            checked.append(check(k,a))
    # Additional arithmetic-only check across much larger parameters.
    for k in range(1,150):
        for a in (0,1,2):
            spec=coefficients(k,a)
            if a>0: assert all(z for z in spec)
            else: assert sum((comb(2*k,j)-(comb(2*k,j-1) if j else 0)) for j,z in enumerate(spec) if z==0)==comb(2*k,k)//2
    print('NEAR_MIDDLE_WALSH_SPECTRUM_PASS', 'numeric_matrices=',len(checked),'symbolic_parameters=',149*3, 'largest_dimension=',max(x[3] for x in checked))
    for x in checked: print(*x)
