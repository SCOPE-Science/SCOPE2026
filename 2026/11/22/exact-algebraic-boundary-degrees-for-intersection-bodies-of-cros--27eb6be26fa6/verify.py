"""Finite consistency checks for the cross-polytope section-volume identity.

Requires Python 3, NumPy, SciPy and SymPy. The all-dimensional theorem
is established by the accompanying analytic proof, not by these tests.
"""
import itertools
import math
import numpy as np
import sympy as sp
from scipy.linalg import null_space
from scipy.spatial import ConvexHull


def exact_polynomials(n):
    a = sp.symbols('a0:'+str(n))
    pairs = list(itertools.combinations(range(n), 2))
    D = sp.prod(a[i]+a[j] for i, j in pairs)
    delta = sp.prod(a[i]-a[j] for i, j in pairs)
    # Alternating polynomial, cancelling the Vandermonde gives P.
    T = sum((-1)**i*a[i]**(2*n-3)*sp.prod(
          a[k]**2-a[l]**2 for k,l in pairs if i not in (k,l))
          for i in range(n))
    P = sp.cancel(T/delta)
    assert sp.denom(P) == 1
    assert sp.total_degree(P) == n*(n-1)//2-1
    assert sp.gcd(P,D) == 1
    return a, sp.expand(P), sp.expand(D)


def formula(a):
    n=len(a)
    aa=np.asarray(a, dtype=float)
    assert np.all(aa>0)
    assert np.min(abs(aa[:,None]-aa[None,:]+np.eye(n)*100))>1e-9
    total=sum(aa[i]**(2*n-3)/np.prod([aa[i]**2-aa[j]**2 for j in range(n) if j!=i]) for i in range(n))
    return 2**(n-1)/math.factorial(n-1)*total


def geometric_section_volume(u):
    """Reconstruct H ∩ B_1^n from intersections with opposite-side edges."""
    u=np.asarray(u,dtype=float)
    n=len(u)
    assert np.linalg.norm(u)>0
    u=u/np.linalg.norm(u)
    positive=[]; negative=[]
    for i in range(n):
        for s in [-1,1]:
            p=np.eye(n)[i]*s
            (positive if np.dot(p,u)>0 else negative).append(p)
    vertices=[]
    for p in positive:
        for q in negative:
            if np.max(np.abs(p+q)) < 1e-10: continue  # antipodal pair interior point 0
            alpha=np.dot(q,u)/(np.dot(q,u)-np.dot(p,u))
            vertices.append(alpha*p+(1-alpha)*q)
    basis=null_space(u.reshape(1,-1))
    verts=np.array(vertices)@basis
    if n==2:
        return float(np.ptp(verts[:,0]))
    return float(ConvexHull(verts).volume)


def main():
    count=0
    for n in [2,3,4]:
        a,P,D=exact_polynomials(n)
        print('n',n,'degree',n*(n-1)//2,'P=',sp.factor(P))
        count+=3
        for k in range(7):
            vals=[sp.Rational(1+i*i+2*k+3*i*k,7+i) for i in range(1,n+1)]
            if len(set(vals))<n: continue
            valp=P.subs(dict(zip(a,vals)))
            vald=D.subs(dict(zip(a,vals)))
            s=sum(vals[i]**(2*n-3)/sp.prod(vals[i]**2-vals[j]**2 for j in range(n) if j!=i) for i in range(n))
            assert valp==sp.factor(vald*s)
            count+=1
    rng=np.random.default_rng(20261120)
    for n in [2,3,4,5]:
        for i in range(55):
            a=np.sort(rng.uniform(.2,3.0,n)+np.arange(n)*.09)
            v=np.array(a)
            f=formula(v)
            g=geometric_section_volume(v)
            # formula expects a unit normal
            f*=np.linalg.norm(v)
            assert abs(f-g)<2e-8*max(1,g), (n,i,f,g)
            count+=1
    print('PASS',count,'exact and independent geometric checks')

if __name__=='__main__': main()
