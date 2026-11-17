#!/usr/bin/env python3
"""Exact checks for one-root deletion in complete-bipartite symmetric-edge polytopes.

Standard library is sufficient for the metric/finite-sum checks. Optional SciPy
checks compare exact normalized volumes against independently constructed hulls.
"""
from fractions import Fraction as F
from math import comb, factorial

def roots(p,q):
    n=p+q; out=[]
    for i in range(p):
        for j in range(p,n):
            u=[F(0)]*n;u[i]=F(1);u[j]=F(-1)
            out.append(tuple(u));out.append(tuple(-v for v in u))
    return out

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def mean(vectors):
    return tuple(sum(v[i] for v in vectors)/len(vectors) for i in range(len(vectors[0])))

def volume_numbers(p,q):
    m,k=p-1,q-1
    whole=F(2,factorial(m)*factorial(k))*sum(
        comb(m,i)**2*comb(k,j)**2*factorial(i+j)*factorial(m+k-i-j)
        for i in range(m+1) for j in range(k+1))
    cut=F(2,factorial(m-1)*factorial(k-1))*sum(
        comb(m-1,i)**2*comb(k-1,j)**2*factorial(i)*factorial(j)*factorial(m+k-2-i-j)
        for i in range(m) for j in range(k))
    return whole,cut

def exact_metric(p,q):
    n=p+q; vv=roots(p,q);v=vv[0]
    A=mean([vv[2*j] for j in range(1,q)])
    B=mean([vv[2*(i*q)] for i in range(1,p)])
    C=mean([vv[2*(i*q+j)+1] for i in range(1,p) for j in range(1,q)])
    if p*q<=2*n:
        den=p*q+4*n
        aa,bb,cc=F(q*(p+2),den),F(p*(q+2),den),F(2*n-p*q,den)
        assert aa>0 and bb>0 and cc>=0
        expected=F(4*n,den)
    else:
        den=2*p*q-n
        aa,bb,cc=F(p*(q-1),den),F(q*(p-1),den),F(0)
        expected=F(p*q,den)
    z=tuple(aa*A[i]+bb*B[i]+cc*C[i] for i in range(n))
    res=tuple(v[i]-z[i] for i in range(n))
    assert dot(res,res)==expected and aa+bb+cc==1
    # Exact first-order metric projection certificate against every other vertex.
    assert all(dot(res,tuple(w[i]-z[i] for i in range(n)))<=0 for w in vv[1:])
    return expected

def independent_hull_check():
    try:
        import numpy as np
        from scipy.spatial import ConvexHull
    except ImportError:
        return 0
    tests=0
    for p in range(2,5):
        for q in range(p,7):
            if p+q>9: continue
            vv=np.array(roots(p,q),dtype=float)
            d=p+q-1
            a=ConvexHull(vv[:,:-1]).volume
            b=ConvexHull(vv[1:,:-1]).volume
            w,c=volume_numbers(p,q)
            assert abs(a*factorial(d)-float(w))<1e-7
            assert abs((a-b)*factorial(d)-float(c))<1e-7
            tests+=1
    return tests

def main():
    checked=0
    for p in range(2,18):
        for q in range(2,18):
            exact_metric(p,q)
            w,c=volume_numbers(p,q)
            assert w>c>0 and w.denominator==c.denominator==1
            checked+=1
    for q in range(2,18):
        w,c=volume_numbers(2,q)
        assert w==(q+1)*2**q and c==2**(q-1)
    hulls=independent_hull_check()
    print(f'BICLIQUE_SIGNED_ROOT_DELETION_PASS exact_profiles={checked} independent_hulls={hulls} threshold=pq-2(p+q)')

if __name__=='__main__':main()
