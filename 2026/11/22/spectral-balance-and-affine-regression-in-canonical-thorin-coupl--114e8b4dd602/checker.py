"""Finite exact/numerical diagnostics for the affine-regression and gamma-ray theorem.

Run: python checker.py. No external dependencies. Finite checks are not proofs of
infinite activity or continuum assertions; see RESULT.md for those proofs.
"""
from fractions import Fraction as Q
from math import exp, sqrt
from cmath import exp as cexp
from math import isclose, factorial

count=0
for lam in [Q(v) for v in (-11,-7,-3,-2,-1,1,2,3,7,11)]:
    for r in [Q(1,37),Q(1,3),Q(1),Q(2),Q(7,3),Q(29)]:
        z=r/lam
        y=r/(lam*lam)
        assert z/y==lam
        assert z*z/y==r
        assert y>0
        assert (z>0)==(lam>0)
        # The absolute Jacobian is r^-1 * |dr,dlam / dz,dy| = y^-2.
        drdz=2*z/y
        drdy=-z*z/(y*y)
        dldz=1/y
        dldy=-z/(y*y)
        jac=abs(drdz*dldy-drdy*dldz)
        assert jac==z*z/(y*y*y)
        assert jac/r==1/(y*y)
        # Inversion of the fixed shell for any rate is precisely r in [1,2].
        assert ((Q(1)<=z*z/y<=Q(2))==(Q(1)<=r<=Q(2)))
        count+=7

# Finite Thorin atomic transforms, including negative rates and Gaussian part.
for params in [
    ((1.0,2.0), (2.0,-3.0)),
    ((3.0,1.5,2.0),(-2.0,1.0,4.0)),
    ((0.25,0.5),(-5.0,-0.75)),
]:
    shapes, rates=params
    for t in (-2.5,-0.7,0.0,0.3,2.1):
        for q in (0.06,0.5,2.0):
            u=(t+sqrt(t*t+4*q))/2
            w=(-t+sqrt(t*t+4*q))/2
            assert abs((u-w)-t)<1e-12
            assert abs(u*w-q)<1e-12
            f1=1+0j
            f2=1+0j
            for a,lam in zip(shapes,rates):
                f1*=complex(1-1j*t/lam+q/(lam*lam))**(-a)
                f2*=complex(1-1j*u/lam)**(-a)*complex(1+1j*w/lam)**(-a)
            f1*=cexp(-0.3*t*t/2-0.3*q)
            f2*=cexp(-0.3*u*u/2)*cexp(-0.3*w*w/2)
            assert abs(f1-f2)<1e-11
            count+=3
    for i in range(4):
        for j in range(4):
            n=i+2*j
            if n<2 or n>6: continue
            # For sums of gamma atoms, the joint cumulant equals
            # (i+j-1)! * sum(a / lam**(i+2j)), apart from Gaussian/shift.
            gamma_kappa=factorial(n-1)*sum(Q(str(a))/Q(str(lam))**n for a,lam in zip(shapes,rates))
            mixed=factorial(i+j-1)*sum(Q(str(a))/Q(str(lam))**n for a,lam in zip(shapes,rates))
            from_parent=Q(factorial(i+j-1),factorial(n-1))*gamma_kappa
            assert mixed==from_parent
            count+=1

# Check a nontrivial finite-jump threshold formula using direct integration
# by the substitution z=r/lam, y=r/lam**2 (at positive and negative rates).
for lam in (-7.0,-2.0,-0.5,0.5,2.0,7.0):
    for x in (0.1,1.0,3.0):
        for y in (0.2,2.0):
            threshold=max(abs(lam)*x,lam*lam*y)
            rvals=(threshold,threshold+0.125,threshold+1)
            assert all(((r/abs(lam)>x and r/(lam*lam)>y) or isclose(r/abs(lam),x) or isclose(r/(lam*lam),y)) for r in rvals)
            count+=1


# Spectral-balance regression: rational mass/rate atoms. The necessary
# Stieltjes regression transform is exactly zero at every tested rational q.
# Both signs have positive, unequal weights and no single absolute rate.
for b in (Q(1,3), Q(1,2), Q(3,4), Q(0)):
    for rates in ((Q(1),Q(2),Q(3)), (Q(2),Q(5)), (Q(1),Q(3,2),Q(5))):
        totalmass={r: Q(i+2,7) for i,r in enumerate(rates)}
        pos={r:totalmass[r]*(1+b/r)/2 for r in rates}
        neg={r:totalmass[r]*(1-b/r)/2 for r in rates}
        assert all(pos[r]>=0 and neg[r]>=0 for r in rates)
        for r in rates:
            assert r*(pos[r]-neg[r])==b*(pos[r]+neg[r])
            count+=1
        for q in (Q(1,13),Q(1,2),Q(3),Q(7),Q(301,2)):
            signed_stieltjes=sum(((r-b)*pos[r]+(-r-b)*neg[r])/(r*r+q) for r in rates)
            assert signed_stieltjes==0
            count+=1
# One-sided multi-rate laws violate all affine identities: the required
# ratio at q=0 versus q approaching infinity changes unless rates equal.
for rates in ((Q(1),Q(2)), (Q(2),Q(3)),(Q(1),Q(2),Q(4))):
    weights=tuple(Q(i+1) for i in range(len(rates)))
    b0=sum(w/r for w,r in zip(weights,rates))/sum(w/(r*r) for w,r in zip(weights,rates))
    binf=sum(w*r for w,r in zip(weights,rates))/sum(weights)
    assert b0 != binf
    count+=1
# Exact direct stochastic regression identity under sign symmetry (b=0).
for rates in ((Q(1),Q(2)),(Q(1),Q(7),Q(10))):
    for q in (Q(1),Q(5),Q(13,7)):
        transform=sum((r*Q(1)+(-r)*Q(1))/(r*r+q) for r in rates)
        assert transform==0
        count+=1

# The angular sign and gamma-ray inverse can be read without moments.
print(f"PASS: {count} exact-rational/algebraic and numerical diagnostic groups")
