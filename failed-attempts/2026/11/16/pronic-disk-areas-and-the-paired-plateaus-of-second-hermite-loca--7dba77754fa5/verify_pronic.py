#!/usr/bin/env python3
"""Reproducible exact checks of the second-Hermite disk ordering theorem.

Requires Python 3 and SymPy. All algebraic comparisons use exact arithmetic.
"""
import math
import sympy as sp

j,t=sp.symbols('j t')
Q=lambda a: t*t-2*a*t+a*(a-1)
A,B=Q(j),Q(j+1)
identity=sp.expand((t-j+1)*A*B-t*(sp.diff(A,t)*B+A*sp.diff(B,t))-t*B**2+(j+1)*A**2)
assert identity==0

# Integrate each polynomial density using the exact integer incomplete-gamma expansion.
def tail_polynomial(level):
    u=sp.symbols('u')
    r=sp.Integer(level)
    qr=u*u-2*r*u+r*(r-1)
    dens=sp.cancel(u**(r-2)*qr*qr/(2*sp.factorial(r)))
    p=sp.Poly(dens,u)
    assert p.is_univariate
    return sp.expand(sum(c*sp.factorial(k)*sum(t**m/sp.factorial(m) for m in range(k+1))
                         for (k,),c in p.terms()))

tails=[tail_polynomial(i) for i in range(44)]
assert all(P.subs(t,0)==1 for P in tails) # each full radial integral equals one
for idx in range(43):
    exact_difference=sp.factor(tails[idx]-tails[idx+1])
    predicted=sp.cancel(-t**(idx-1)*Q(idx)*Q(idx+1)/(2*sp.factorial(idx+1)))
    assert sp.simplify(exact_difference-predicted)==0, (idx,exact_difference,predicted)

# At a pronic area the only equal-neighbor edges form two three-term blocks.
for k in range(1,6):
    s=k*(k+1)
    a=k*k
    b=(k+1)*(k+1)
    edges=[]
    for idx in range(43):
        q0=sp.expand(Q(idx)).subs(t,s)
        q1=sp.expand(Q(idx+1)).subs(t,s)
        if q0*q1==0: edges.append(idx)
        else: assert q0*q1>0,(k,idx)
    assert edges==[a-1,a,b-1,b],(k,edges)
    assert tails[a].subs(t,s)<tails[b].subs(t,s) # lambda_a > lambda_b

# Exact two distinct triplets at the smallest special disk.
assert [tails[z].subs(t,2) for z in (0,1,2)]==[5,5,5]
assert [tails[z].subs(t,2) for z in (3,4,5)]==[sp.Rational(17,3)]*3
assert all(tails[z].subs(t,2)<tails[z+1].subs(t,2) for z in range(5,43))

# Non-pronic radii have at least one genuine upward neighboring jump.
for s in [sp.Rational(1,10),sp.Rational(1,2),sp.Rational(3,2),
          sp.Rational(5,2),3,4,5,7,8,9,11,13,15,17,19]:
    assert any(sp.expand(Q(i)).subs(t,s)*sp.expand(Q(i+1)).subs(t,s)<0
               for i in range(43)),s

print('H2_PRONIC_ORDER_PASS universal_polynomial_identity=1 exact_integral_levels=44 '
      'exact_neighbor_gaps=43 pronic_areas=5 nonpronic_radii=15 double_triplet_area=2')
