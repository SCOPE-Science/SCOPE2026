"""Exact checks for the tangential hypersurface of the quartic scroll S(2,2)."""
from itertools import product
import sympy as sp

A0,A1,A2,B0,B1,B2,z,u,v,alpha,beta = sp.symbols('A0 A1 A2 B0 B1 B2 z u v alpha beta')
M0=A1*B2-A2*B1
M1=A2*B0-A0*B2
M2=A0*B1-A1*B0
H=sp.expand(M1**2-4*M0*M2)
Q=sp.expand(-M1)
assert sp.Poly(H,*[A0,A1,A2,B0,B1,B2]).total_degree()==4
assert sp.Poly(Q,*[A0,A1,A2,B0,B1,B2]).total_degree()==2
assert sp.Poly(H,*[A0,A1,A2,B0,B1,B2],modulus=2)==sp.Poly(Q**2,*[A0,A1,A2,B0,B1,B2],modulus=2)

# Both rows of a generic tangent matrix lie in span(q,q').
subs={A0:alpha*z**2+2*u*z,A1:alpha*z+u,A2:alpha,
      B0:beta*z**2+2*v*z,B1:beta*z+v,B2:beta}
assert sp.expand(H.subs(subs,simultaneous=True))==0
assert sp.Poly(sp.expand(Q.subs(subs,simultaneous=True)),z,u,v,alpha,beta,modulus=2).is_zero
for x in [A0,A2,B0,B2]:
    assert sp.diff(Q,x)!=0
assert all(sp.diff(Q,x)==0 for x in [A1,B1])
# In characteristic 2, the cone is singular precisely at A0=A2=B0=B2=0.

def norm(p,q):
    k=next(i for i,x in enumerate(p) if x%q)
    inv=pow(p[k]%q,-1,q)
    return tuple((x*inv)%q for x in p)

def fieldpoints(q,n):
    return {norm(p,q) for p in product(range(q),repeat=n) if any(p)}

def tangent_locus(q):
    pts=set()
    for s,t in fieldpoints(q,2):
        base=(s*s,s*t,t*t)
        deriv=(2*s,t,0) if t else (0,s,2*t)
        for a,b,c,d in product(range(q),repeat=4):
            row1=tuple((a*x+b*y)%q for x,y in zip(base,deriv))
            row2=tuple((c*x+d*y)%q for x,y in zip(base,deriv))
            v=row1+row2
            if any(v): pts.add(norm(v,q))
    return pts

def minors(t):
    a,b,c,d,e,f=t
    return ((b*f-c*e),(c*d-a*f),(a*e-b*d))

def matrix_rank_two(t,q): return any(x%q for x in minors(t))

def defining(t,q):
    x,y,z=minors(t)
    return (y*y-4*x*z)%q

for p in (2,3,5):
    universe=fieldpoints(p,6)
    tang=tangent_locus(p)
    target={pt for pt in universe if defining(pt,p)==0}
    target_rank2={pt for pt in target if matrix_rank_two(pt,p)}
    tang_rank2={pt for pt in tang if matrix_rank_two(pt,p)}
    assert target_rank2==tang_rank2,(p,len(target_rank2),len(tang_rank2))
    assert tang <= target
    print('p',p,'rank-2 target and tangent',len(target_rank2),'total equation',len(target),'total rational tangent',len(tang))

# The rational inverse parameter over characteristic 2 is a square root.
# On A2=1, put A0=w, B2=t, B0=t*w, A1=x, B1=y.
# Q is identically zero; w is an indeterminate in k(w,t,x,y)
# and is not a square by valuation at the prime (w).
print('ALL_CHECKS_PASSED')
