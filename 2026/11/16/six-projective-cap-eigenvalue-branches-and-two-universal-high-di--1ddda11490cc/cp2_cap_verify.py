#!/usr/bin/env python3
"""Exact Jacobi-sector verification for degree-two projective cap concentration.

Requires Python 3 and SymPy. All finite-dimensional checks use rational
symbolic arithmetic. The limiting-envelope identities are polynomial.
"""
import sympy as S

x, d, z = S.symbols('x d z', positive=True)
q = 1-x
Q = {
 (0, 0): 1-4*x+(2*d*d+6*d+6)*x*x-(d+1)**2*(d+4)*x**3+((d+1)*(d+2)/2)**2*x**4,
 (1, 0): 1+d*x-(d+1)*(d+6)*x*x/2+(d+1)*(d+2)**2*x**3/2,
 (1, 1): 1-2*x+(d+2)**2*x*x,
 (2, 0): 1+(d+1)*x+(d+1)*(d+2)*x*x/2,
 (2, 1): 1+(d+2)*x,
 (2, 2): S.Integer(1)
}

# Algebraic derivative identities imply every closed-form eigenvalue.
for (p, r), poly in Q.items():
    a, b = p+r+d-2, abs(p-r)
    j = 2-max(p, r)
    jac = S.jacobi(j, a, b, 2*x-1)
    norm = S.prod(j+k for k in range(1,b+1)) / (
        (2*j+a+b+1)*S.prod(j+a+k for k in range(1,b+1)))
    residual = (d-1+p+r)*poly-q*S.diff(poly,x) - x**b*jac**2/norm
    assert S.cancel(S.expand(residual)) == 0, (p,r,residual)
    assert poly.subs(x,0) == 1

# Check all distinct multiplicities against the complex spherical harmonic dimension.
n=d-1
A=lambda k:S.prod(n+i for i in range(k))/S.factorial(k)
h=lambda p,r: S.expand(A(p)*A(r) - (A(p-1)*A(r-1) if min(p,r)>0 else 0))
assert S.simplify(sum(h(p,r) for p in range(3) for r in range(3))-
    (S.binomial(d+1,2)**2-d**2)) == 0

# Invariant-kernel trace identity: total eigenvalue sum equals cap volume times dimension.
n=d-1
multiplicities={(0,0):1,(1,0):2*n,(1,1):n*n-1,
 (2,0):n*(n+1),(2,1):n*(n-1)*(n+2),
 (2,2):n*n*(n-1)*(n+3)/4}
trace_reduced=sum(multiplicities[k]*q**sum(k)*Q[k] for k in Q)
dim_total=(d*(d+1)/2)**2-d**2
assert S.factor(trace_reduced-dim_total)==0

# Symbolic strict minimal branch. Positive remaining factors hold for d>=3, 0<x<1.
F=q**4
normalized={k:S.expand(q**(k[0]+k[1])*v) for k,v in Q.items()}
assert S.simplify((normalized[(0,0)]-F)- d*x**2*(d+3)*(
    (d*d+3*d+4)*x*x-4*(d+3)*x+8)/4) == 0
assert S.simplify((normalized[(1,0)]-F)- x*(d+3)*q*(
    (d*d+2*d+2)*x*x-(d+4)*x+2)/2) == 0
assert S.simplify(normalized[(1,1)]-F-(x*x*(d+1)*(d+3)*q*q)) == 0
assert S.simplify(normalized[(2,0)]-F-(x*(d+3)*q*q*(d*x+2)/2)) == 0
assert S.simplify(normalized[(2,1)]-F-(x*(d+3)*q**3)) == 0

# Fixed-volume d->infinity yields six exact Laguerre-sector polynomials.
limit = {}
for k,poly in normalized.items():
    # t=z/d; remove the common factor (1-t)^(d-1) first.
    polynomial = S.expand(poly.subs(x,z/d))
    limit[k]=S.expand(S.limit(polynomial,d,S.oo))
A0=1+2*z**2-z**3+z**4/4
B0=1+z-z**2/2+z**3/2
C0=1+z**2
D0=1+z+z**2/2
E0=1+z
F0=S.Integer(1)
for k, val in {(0,0):A0,(1,0):B0,(1,1):C0,
 (2,0):D0,(2,1):E0,(2,2):F0}.items():
    assert S.factor(limit[k]-val)==0, (k,limit[k])
assert S.factor(A0-C0)==z**2*(z-2)**2/4
assert S.factor(D0-A0)==-z*(z-2)*(z*z-2*z+2)/4
assert S.factor(D0-B0)==-z*z*(z-2)/2
assert S.factor(B0-A0)==-z*(z-2)*(z*z-4*z+2)/4

# A separate exact polynomial-integral replay at small dimensions.
for dim in range(3,9):
    for (p,r),expr in Q.items():
        a,b=p+r+dim-2,abs(p-r)
        j=2-max(p,r)
        J=S.jacobi(j,a,b,2*x-1)
        W=S.Poly(S.expand(x**b*q**a*J**2),x)
        integ=lambda lo:S.expand(sum(co* (1-lo**(mon[0]+1))/(mon[0]+1)
             for mon,co in W.terms()))
        denom=integ(S.Integer(0))
        for t0 in (S.Rational(1,7),S.Rational(2,5),S.Rational(4,5)):
            actual=integ(t0)/denom
            formula=q.subs(x,t0)**(dim-1+p+r)*expr.subs({d:dim,x:t0})
            assert S.cancel(actual-formula)==0, (dim,p,r,t0)

print('CP2_SIX_JACOBI_BRANCHES_EXACT_PASS')
print('CP2_MULTIPLICITIES_AND_STRICT_MINIMUM_PASS')
print('CP2_FIXED_VOLUME_TWO_TRANSITIONS_PASS')
print('CP2_DIRECT_EXACT_BETA_INTEGRALS_PASS dimensions=3..8')
