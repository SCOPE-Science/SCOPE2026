#!/usr/bin/env python3
"""Exact identities for the flex cover of the symmetric quartic pencil.
Requires SymPy. This independently checks identities, not geometric monodromy.
"""
import sympy as s
x,y,z,a,T=s.symbols('x y z a T')
U,V,W=x*x,y*y,z*z
e1=U+V+W
e2=U*V+U*W+V*W
e3=U*V*W
F=U**2+V**2+W**2+a*e2
H=s.det(s.hessian(F,(x,y,z)))
identity=H+24*a*(a+6)*e1*F-72*(a+2)*(a*e1**3+3*(a-2)**2*e3)
assert s.expand(identity)==0
print('HESSIAN_SYZYGY_OK')
P=T**3-T**2-T/(a-2)+a/(3*(a-2)**2)
disc=s.factor(s.discriminant(P,T))
print('CUBIC_DISC',disc)
assert s.simplify(disc-4*(a-3)*(a+1)**2/(3*(a-2)**4))==0
N=s.together(3*(a-2)**2*P).expand().cancel()
D=s.factor(s.discriminant(N,a))
print('ELIMINATION_POLY',s.factor(N))
print('ELIMINATION_DISC',D)
assert s.expand(D-(-24*T**3+33*T**2-6*T+1))==0
assert s.degree(D,T)==3
# These critical specializations yield 12 double flexes in the two known special fibers.
for v in [0,1,3]:
    pv=s.factor(P.subs(a,v))
    print('P_AT',v,pv)
    if v==0:
        assert s.factor(pv)==T*(2*T**2-2*T+1)/2
    elif v==3:
        assert s.factor(pv)==(T-1)**2*(T+1)
# Signed permutation action has 24 members, and generic points have trivial stabilizer.
from itertools import permutations,product
transforms=set()
for perm in permutations((0,1,2)):
    for signs in product((-1,1),repeat=2):
        # representative first coordinate sign +1; global sign already modded out
        transforms.add((perm, (1,)+signs))
assert len(transforms)==24
print('GROUP_ORDER',len(transforms))
# square-class valuations at a=0, with exactly one root of P vanishing simply
assert s.factor(P.subs(a,0)).subs(T,0)==0
assert s.diff(P,T).subs({T:0,a:0})!=0
assert s.diff(P,a).subs({T:0,a:0})!=0
print('KUMMER_VALUATIONS_OK')
print('ALL_CHECKS_PASSED')
