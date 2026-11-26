#!/usr/bin/env python3
"""Exact checks for the rational singularities of the plane-filling pencil.
Requires SymPy for formal identities; finite-field checks use Python integers.
"""
import math
import sympy as S

x,z,t,k,u=S.symbols('x z t k u', nonzero=True)
h=t*x**2-x**3+z-t**3+(z**2+k*x**2)*(t**3*x-t*z)
k0=(1-t**7)/t**3
H=S.hessian(h,(x,z)).subs({x:t,z:t**3,k:k0})
assert S.simplify(H[0,0]+4*t**8)==0
assert S.simplify(H[0,1]-2*(2*t**7-1)/t)==0
assert S.simplify(H[1,1]+4*t**4)==0
assert S.factor(H.det()-4*(4*t**7-1)/t**2)==0
# At the corank-one locus 4t^7=1, the tangent line has direction (1,-t^2).
line=S.Poly(S.expand(h.subs({x:t+u,z:t**3-t**2*u,k:3/(4*t**3)})),u)
cubic=S.factor(line.coeff_monomial(u**3))
assert S.factor(cubic-(4*t**7+1)/2)==0
assert S.rem(S.together(2*cubic-2).as_numer_denom()[0],4*t**7-1,t)==0
# In characteristic 3 with q=3, the q-th powers contribute at degree 3;
# check the complete defining equation directly at the only cusp t=1, k=0.
X,Z=1+u,1-u
F3=S.expand(X**5-X**3+Z-Z**3+X*Z**5-Z**3*X**3)
assert int(F3.coeff(u,2))%3==0
assert int(F3.coeff(u,3))%3==1

def field_points(p):
    for y in range(p):
        for z in range(p):yield (1,y,z)
    for z in range(p):yield (0,1,z)
    yield (0,0,1)

def grad(p,k,X,Y,Z):
    q=p;mod=p
    fx=(2*pow(X,q+1,p)*Y-3*X*X*pow(Y,q,p)+pow(Z,q+2,p)+3*k*X*X*pow(Z,q,p)-2*k*pow(X,q+1,p)*Z)%p
    fy=(pow(X,q+2,p)+2*pow(Y,q+1,p)*Z-3*Y*Y*pow(Z,q,p))%p
    fz=(pow(Y,q+2,p)+2*pow(Z,q+1,p)*X-3*Z*Z*pow(X,q,p)-k*pow(X,q+2,p))%p
    return fx,fy,fz

for p in (3,5,7,11,29):
    P=list(field_points(p))
    assert len(P)==p*p+p+1
    for kvalue in range(p):
        actual=set(Pt for Pt in P if grad(p,kvalue,*Pt)==(0,0,0))
        predicted=set()
        for tt in range(1,p):
            if (pow(tt,7,p)+kvalue*pow(tt,3,p)-1)%p==0:
                # chart y=1; normalize x=1 to compare against projective enumeration
                inv=pow(tt,-1,p)
                predicted.add((1,inv,(tt**3*inv)%p))
        assert actual==predicted,(p,kvalue,actual,predicted)
    g=math.gcd(7,p-1)
    kzero=[tt for tt in range(1,p) if pow(tt,7,p)==1]
    assert len(kzero)==g
    print(f'p={p}, k=0: {g} rational singularities; ' +
          ('cusps' if p==3 else ('split nodes' if pow(-3%p,(p-1)//2,p)==1 else 'nonsplit nodes')))
# For F_{3^e}, 7|(3^e-1) iff 6|e; hence k=0 has 7 rational cusps for e multiple of 6.
assert [pow(3,e,7) for e in range(1,7)]==[3,2,6,4,5,1]
print('ALL_CHECKS_PASS')
