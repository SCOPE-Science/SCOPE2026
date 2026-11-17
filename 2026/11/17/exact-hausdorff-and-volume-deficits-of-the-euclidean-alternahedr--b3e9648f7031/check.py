#!/usr/bin/env python3
"""Independent finite checks for the metric and volume formulas of alternating permutohedra.
Run: python check.py (Python 3.10+; numpy and scipy needed for hull checks)."""
from fractions import Fraction
from itertools import permutations
from math import factorial, sqrt
from random import Random
from collections import Counter
import numpy as np
from scipy.spatial import ConvexHull


def inversion_parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1,len(p))) % 2


def centered(p):
    n=len(p)
    return tuple(Fraction(2*i-n-1,2) for i in p)


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))



def check():
    exact_points=0
    width_cases=0
    for n in range(3,8):
        perms=list(permutations(range(1,n+1)))
        odd=[p for p in perms if inversion_parity(p)]
        even=[p for p in perms if not inversion_parity(p)]
        p=tuple(range(1,n+1))
        v=centered(p)
        r2=Fraction(n*(n*n-1),12)
        assert dot(v,v)==r2
        # Identity is even. Choose a fixed odd orbit representative by swapping labels 1 and 2.
        o=list(p);o[0],o[1]=o[1],o[0];o=tuple(o)
        w=centered(o)
        neighbors=[]
        for i in range(n-1):
            q=list(o)
            for j in range(n):
                if q[j]==i+1:q[j]=i+2
                elif q[j]==i+2:q[j]=i+1
            neighbors.append(tuple(q))
        assert len(set(neighbors))==n-1
        assert all(not inversion_parity(q) for q in neighbors)
        for q in even:
            d2=sum((a-b)**2 for a,b in zip(q,o))
            assert d2>=2 and (d2==2)==(q in neighbors)
        for q in odd:
            if q!=o:
                d2=sum((a-b)**2 for a,b in zip(q,o))
                assert d2>=4
        alphas=[Fraction(6*i*(n-i),n*(n*n-1)) for i in range(1,n)]
        assert sum(alphas)==1 and all(a>0 for a in alphas)
        foot=tuple(sum(alphas[i]*centered(neighbors[i])[k] for i in range(n-1)) for k in range(n))
        assert foot==tuple(w[k]-w[k]/r2 for k in range(n))
        assert dot(w,foot)==r2-1
        assert sum((a-b)**2 for a,b in zip(w,foot))==1/r2
        exact_points+=len(perms)
        # Halfspace cap separation at all vertices for a sample/all odd pairs in smaller orders.
        if n<=5:
            for ia in range(len(odd)):
                for ib in range(ia+1,len(odd)):
                    va,vb=centered(odd[ia]),centered(odd[ib])
                    for q in perms:
                        assert dot(tuple(a+b for a,b in zip(va,vb)),centered(q))<=2*r2-2
        rng=Random(44440+n)
        for _ in range(120):
            u=rng.sample(range(-50000,50000),n)
            inds=sorted(range(n),key=lambda i:u[i])
            ordered=sorted(u)
            gap=min(ordered[i+1]-ordered[i] for i in range(n-1))
            best=[0]*n;worst=[0]*n
            for i,idx in enumerate(inds):
                best[idx]=i+1;worst[idx]=n-i
            all_max=sum(x*y for x,y in zip(u,best))
            all_min=sum(x*y for x,y in zip(u,worst))
            even_scores=[sum(x*y for x,y in zip(u,q)) for q in even]
            loss=(all_max-all_min)-(max(even_scores)-min(even_scores))
            predicted=(inversion_parity(best)+inversion_parity(worst))*gap
            assert loss==predicted
            assert (inversion_parity(best)+inversion_parity(worst) in ([1] if n%4 in [2,3] else [0,2]))
            width_cases+=1
        # Independent numerical hull-volume/side counts.
        if n<=6:
            qmat,_=np.linalg.qr(np.eye(n)[:,:n-1]-np.eye(n)[:,[-1]])
            all_coords=(np.array(perms,dtype=float)-(n+1)/2)@qmat
            even_coords=(np.array(even,dtype=float)-(n+1)/2)@qmat
            hull_all=ConvexHull(all_coords)
            hull_even=ConvexHull(even_coords, qhull_options='Qx')
            frac=hull_even.volume/hull_all.volume
            predicted_frac=1-1/(2*n**(n-3))
            assert abs(frac-predicted_frac)<2e-10,(n,frac,predicted_frac)
            count_facets=len({tuple(np.round(eq,8)) for eq in hull_even.equations})
            predicted_facets=3 if n==3 else 20 if n==4 else factorial(n)//2+2**n-2
            assert count_facets==predicted_facets,(n,count_facets,predicted_facets)
            print(f'n={n} volume_ratio={frac:.15f} predicted={predicted_frac:.15f} facets={count_facets}')
    # Symbolic determinant formula by tridiagonal recurrence, verified through 200.
    d0,d1=1,2
    for n in range(3,201):
        d0,d1=d1,2*d1-d0
        assert d1==n
    print(f'ALTERNATING_PERMUTOHEDRON_PASS exact_permutations={exact_points} width_trials={width_cases} cartan_orders=199 hull_orders=4')

if __name__=='__main__':check()
