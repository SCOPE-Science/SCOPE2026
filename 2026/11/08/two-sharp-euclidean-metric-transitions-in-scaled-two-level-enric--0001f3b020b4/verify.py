"""Exact finite reproducibility tests for two-level enriched poset polytope metric formulas.
Requires only the Python 3 standard library. This is not an infinite proof.
"""
from itertools import product
from fractions import Fraction

def order_points(m,n,a,b):
    return sorted(set([(0,)*m + tuple(b*y for y in ys)
                       for ys in product((-1,0,1),repeat=n)] +
                      [tuple(a*x for x in xs) + (b,)*n
                       for xs in product((-1,0,1),repeat=m)]))

def chain_points(m,n,a,b):
    return sorted(set([tuple(a*x for x in xs) + (0,)*n
                       for xs in product((-1,0,1),repeat=m)] +
                      [(0,)*m + tuple(b*y for y in ys)
                       for ys in product((-1,0,1),repeat=n)]))

def support(pts,v):
    return max(sum(x*y for x,y in zip(p,v)) for p in pts)

def widths(v,m,a,b):
    U=a*sum(abs(x) for x in v[:m])
    V=b*sum(abs(y) for y in v[m:])
    T=b*abs(sum(v[m:]))
    return max(2*U,2*V,U+V+T),2*max(U,V)

def diameter_sq(pts):
    return max(sum((x-y)**2 for x,y in zip(p,q)) for p in pts for q in pts)

pairs=0; normals=0; branchA=0;branchB=0;ties=0
for m,n in product((2,3,4),repeat=2):
 for a,b in ((1,1),(1,2),(2,1),(3,2),(1,3),(3,1)):
    O=order_points(m,n,a,b); C=chain_points(m,n,a,b)
    assert diameter_sq(O)==max(4*m*a*a,m*a*a+4*n*b*b)
    assert diameter_sq(C)==4*max(m*a*a,n*b*b)
    A=Fraction(1,a*a)+Fraction(1,2*b*b)
    B=Fraction(1,b*b)
    K=max(A,B)
    J=Fraction(1,a*a)+Fraction(1,b*b)
    if A>B:branchA+=1
    elif B>A:branchB+=1
    else:ties+=1
    for z in product((-1,0,1), repeat=m+n):
      if not any(z):continue
      wo,wc=widths(z,m,a,b)
      assert wo==support(O,z)+support(O,tuple(-v for v in z))
      assert wc==support(C,z)+support(C,tuple(-v for v in z))
      norm_sq=sum(v*v for v in z)
      assert wo*wo*K >= 4*norm_sq
      assert wc*wc*J >= 4*norm_sq
      normals+=1
    # Three-supported and one-supported equality candidate directions.
    z=[0]*(m+n);z[0]=2*b;z[m]=a;z[m+1]=-a
    wo,_=widths(z,m,a,b)
    assert Fraction(wo*wo,sum(v*v for v in z))==4/A
    z=[0]*(m+n);z[m]=1
    wo,_=widths(z,m,a,b)
    assert Fraction(wo*wo,sum(v*v for v in z))==4/B
    z=[0]*(m+n);z[0]=b;z[m]=a
    _,wc=widths(z,m,a,b)
    assert Fraction(wc*wc,sum(v*v for v in z))==4/J
    pairs+=1
print('TWOLEVEL_ENRICHED_SCALED_CHECKS_PASSED', 'profiles=',pairs, 'integer_directions=',normals, 'mixed=',branchA, 'upper=',branchB, 'boundary=',ties)
