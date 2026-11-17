"""Finite, independent checks of stated H-description, facet rank, inball LP, diameter and volume.
Requires numpy and scipy. Finite checks corroborate but do not replace proofs.
"""
import itertools
import math
from collections import Counter
from fractions import Fraction
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import linprog


def points(k,n):
    cube=list(itertools.product((0,1),repeat=k))
    simp=[(0,)*k]+[tuple(int(i==j) for i in range(k)) for j in range(k)]
    lower=(tuple(sum(blocks,()))+(0,) for blocks in itertools.product(*([cube]*n+[simp]*n)))
    upper=(tuple(sum(blocks,()))+(1,) for blocks in itertools.product(*([simp]*n+[cube]*n)))
    return np.array(list(lower)+list(upper),dtype=float)

def hrep(k,n):
    dim=2*n*k+1
    rows=[]
    # a.x<=b
    for i in range(dim-1):
        a=np.zeros(dim);a[i]=-1
        rows.append((a,0.,f'lower_{i}'))
    for i in range(2*n):
        for mask in range(1,1<<k):
            a=np.zeros(dim)
            ss=[j for j in range(k) if mask&(1<<j)]
            for j in ss:a[i*k+j]=1
            if i<n:
                a[-1]=len(ss)-1;b=len(ss)
            else:
                a[-1]=-(len(ss)-1);b=1
            rows.append((a,float(b),f'block_{i}_subset_{mask}'))
    z=np.zeros(dim);z[-1]=-1;rows.append((z,0.,'t_lower'))
    z=np.zeros(dim);z[-1]=1;rows.append((z,1.,'t_upper'))
    return rows

def poly_mul(a,b):
    z=[Fraction(0)]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):z[i+j]+=c*d
    return z

def poly_pow(a,n):
    out=[Fraction(1)]
    for _ in range(n):out=poly_mul(out,a)
    return out

def vpoly(k):
    from math import comb,factorial
    a=[Fraction(0)]*(k+1)
    for j in range(k+1):
        # binom(k,j)*(1-t)^(k-j)*t^j/j!
        for h in range(k-j+1):
            a[h+j]+=Fraction(comb(k,j)*comb(k-j,h)*((-1)**h),factorial(j))
    return a

def vol_exact(k,n):
    a=vpoly(k)
    b=[Fraction(0)]*(k+1)
    from math import comb
    for i,c in enumerate(a):
        for j in range(i+1):b[j]+=c*comb(i,j)*((-1)**j)
    p=poly_pow(poly_mul(a,b),n)
    return sum(c/Fraction(i+1) for i,c in enumerate(p))

checks=0
for k,n in [(2,1),(2,2),(3,1),(3,2),(4,1)]:
    V=points(k,n); rows=hrep(k,n);d=2*n*k+1
    assert V.shape[0]==2*(2**k*(k+1))**n;checks+=1
    assert np.linalg.matrix_rank(V[1:]-V[0])==d;checks+=1
    assert len(rows)==2*n*(k+2**k-1)+2;checks+=1
    A=np.array([r[0] for r in rows]);b=np.array([r[1] for r in rows]);norms=np.linalg.norm(A,axis=1)
    assert np.max(V@A.T-b)<1e-9;checks+=len(V)*len(rows)
    # Each proposed inequality has enough tight, affinely independent vertices to be a facet.
    for i,(a,b0,name) in enumerate(rows):
        T=V[np.abs(V@a-b0)<1e-9]
        assert T.shape[0]>=d and np.linalg.matrix_rank(T[1:]-T[0])==d-1,(k,n,name)
        checks+=1
    # Independent LP, with the radius an additional variable.
    obj=np.zeros(d+1);obj[-1]=-1
    lp=linprog(obj,A_ub=np.column_stack((A,norms)),b_ub=b,
               bounds=[(None,None)]*(d+1), method='highs')
    assert lp.success,lp.message
    R=(k+1)/(2*(k+math.sqrt(k*k-k+1)))
    assert abs(lp.x[-1]-R)<1e-8,(k,n,lp.x[-1],R)
    center=np.array([R]*(d-1)+[0.5])
    assert np.max(np.abs(lp.x[:d]-center))<1e-7,(k,n,lp.x)
    slacks=(b-A@center)/norms
    assert abs(min(slacks)-R)<1e-9
    assert sum(abs(z-R)<1e-9 for z in slacks)==2*n*(k+1)
    checks+=4
    # Complement counts: only different-layer pairs can realize full Boolean-cube diameter.
    seen={tuple(row.astype(int)) for row in V}
    complement=[row for row in seen if tuple(1-v for v in row) in seen]
    assert len(complement)//2==(k+1)**(2*n)
    checks+=len(seen)
    # Independent Qhull facet count for modest sizes.
    if n==1:
        hull=ConvexHull(V)
        uh=np.unique(np.round(hull.equations,7),axis=0)
        assert len(uh)==len(rows),(k,len(uh),len(rows))
        actual=vol_exact(k,1)
        assert abs(hull.volume-float(actual))<3e-8,(k,float(actual),hull.volume)
        checks+=2
    print('OK k=',k,'n=',n,'dim=',d,'facets=',len(rows),'inradius=',format(R,'.12g'),'diam_pairs=',(k+1)**(2*n))

assert vol_exact(2,1)==Fraction(27,40)
assert vol_exact(3,1)==Fraction(953,2520)
assert vol_exact(4,1)==Fraction(2579,13440)
checks+=3
for k in range(2,20):
    vals=[(s+1)/(2*(s+math.sqrt(s*s-s+1))) for s in range(1,k+1)]
    assert all(vals[j]>vals[j+1] for j in range(len(vals)-1))
    checks+=1
print('ALL PASSED:',checks,'independent finite checks')
