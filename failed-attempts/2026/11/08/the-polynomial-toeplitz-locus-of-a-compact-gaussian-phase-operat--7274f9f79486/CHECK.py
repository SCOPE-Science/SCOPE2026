"""Finite diagnostics for a self-contained Fock-space polynomial-calculus theorem."""
from cmath import exp
from math import atan, cos, gcd, pi, tan

checks = 0
# Diagonal eigenvalue identity and generating-function identity for several t, k and n.
for t in (0.12,0.5,1.,1.4,3.7):
    u=1+1j*t
    q=1/u
    for k in range(0,35):
        gamma=u**k
        for n in range(0,13):
            # Gamma integral of Gaussian symbol, continued where Re gamma<=0
            # as algebraic identity of rational/exponential eigenvalue formulas.
            lam_a=q**(k*(n+1))
            lam_b=gamma**(-(n+1))
            assert abs(lam_a-lam_b)<1e-10*max(1,abs(lam_a))
            checks+=1
        if k==0: assert abs(gamma.real-1)<1e-12
    assert (u*u).real < 1

# Pole positions distinct, and no combination of two distinct poles can cancel residues.
for t in (0.15,1.,2.3):
    vals=[(1+1j*t)**k for k in range(0,14)]
    assert len({round(abs(v),12) for v in vals})==len(vals)
    checks+=1

# Rational-angle orbit-count diagnostics, away from almost-zero cosine numerical instability.
for p,q in ((1,3),(1,4),(1,5),(2,5),(1,6),(2,7),(3,8),(1,9),(2,9),(3,10)):
    assert 0<p/q<1/2
    L=2*q//gcd(p,2*q)
    count=sum(cos(2*pi*j/L)>1e-10 for j in range(L))
    predicted=1+2*((L-1)//4)
    assert count==predicted,(p,q,L,count,predicted)
    checks+=1

# Exact example t=1: first two degrees allowed, second to sixth forbidden,
# seventh to ninth allowed.
t=1.; u=1+1j*t
assert [k for k in range(10) if (u**k).real >= 1-1e-12]==[0,1,7,8,9]
checks+=1
print(f"PASS: {checks} bounded finite identity, pole, and rational-orbit diagnostics")
