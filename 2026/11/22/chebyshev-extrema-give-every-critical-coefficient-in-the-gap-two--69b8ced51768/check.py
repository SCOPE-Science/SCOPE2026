"""Finite checks for a Chebyshev description of harmonic-trinomial folds.
Scientific proof in RESULT.md is analytic; this program is a diagnostic only.
Usage: python check.py
"""
import math
import sympy as sp

x,t=sp.symbols('x t', real=True)
checks=0
for k in range(1,20,2):
    n=k+2
    U=sp.chebyshevu(k,x)
    # Main imaginary-part identity after dividing by sin(theta)^3.
    S=sp.expand(k*sp.chebyshevu(n-1,x)-n*sp.chebyshevu(k-1,x))
    assert sp.simplify(S+2*(1-x*x)*sp.diff(U,x))==0
    checks+=1
    # The real-part formula holds modulo the stationary equation.
    B=sp.chebyshevt(n,x)+sp.Rational(n,k)*sp.chebyshevt(k,x)
    residue=sp.together(B-sp.Rational(2,k)*U)
    if k>1:
        assert sp.rem(sp.Poly(sp.together(residue).as_numer_denom()[0],x),sp.Poly(sp.diff(U,x),x))==0
    checks+=1
    roots=sp.nroots(sp.diff(U,x), maxsteps=100) if k>1 else []
    roots=sorted(float(sp.re(z)) for z in roots)
    assert len(roots)==k-1
    assert all(abs(float(sp.im(z)))<1e-8 and abs(float(sp.re(z)))<1 for z in roots)
    hs=[float(k+1)]+[float(U.subs(x,r)) for r in roots if float(U.subs(x,r))>1e-8]
    assert len(hs)==(k+1)//2
    assert all(h>0 for h in hs)
    hs=sorted(hs,reverse=True)
    assert all(hs[j]>hs[j+1]+1e-8 for j in range(len(hs)-1))
    cs=[n/k*(k/(2*h))**(2/n) for h in hs]
    assert all(cs[j]<cs[j+1] for j in range(len(cs)-1))
    for r in roots:
        theta=math.acos(r)
        im=math.sin(n*theta)-n/k*math.sin(k*theta)
        re=math.cos(n*theta)+n/k*math.cos(k*theta)
        assert abs(im)<2e-7 and abs(re-2*float(U.subs(x,r))/k)<2e-7
        checks+=1
    checks+=5
# Closed special case and large degree law.
k=3; n=5
special=n/k*(9*math.sqrt(6)/16)**(2/n)
assert abs(special-1.8946457081379975)<1e-13
checks+=1
for k in (21,51,101):
    n=k+2
    U=sp.chebyshevu(k,x)
    # Numerically isolate critical point nearest 0, without computing all roots.
    xx=sp.nsolve(sp.diff(U,x), (0.1/k,math.pi/k), solver='bisect',verify=False)
    hh=abs(float(U.subs(x,xx)))
    cN=n/k*(k/(2*hh))**(2/n)
    c1=n/k*(k/(2*(k+1)))**(2/n)
    ratio=(cN-c1)/(2*math.log(k)/k)
    assert .8<ratio<1.2
    checks+=1
print('PASS:',checks,'symbolic and finite numerical diagnostics')
