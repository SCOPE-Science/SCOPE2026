"""Finite and symbolic checks for the gap-four rational Hartogs root theorem.

Requires SymPy. Finite root computations are diagnostics only; the paper's
infinite proof is by exact coefficient sums and Descartes' rule.
"""
from __future__ import annotations
import math
import sympy as sp

H, J, U, Z = sp.symbols('h J u z', integer=True)
checks = 0

def ck(condition, description='assertion'):
    global checks
    assert bool(condition), description
    checks += 1

def coeffs_closed(h, r):
    if r == 1:
        return (
            (h + 1)*(h + 2)*(4*h + 3)/6,
            (h + 1)*(4*h*h + 11*h + 8),
            (h + 1)*(2*h + 3)*(4*h + 5),
            (h + 1)*(12*h*h + 33*h + 22),
            (44*h**3 + 165*h*h + 217*h + 99)/3,
        )
    if r == 3:
        return (
            (h + 1)*(h + 2)*(4*h + 9)/6,
            (h + 2)*(4*h*h + 13*h + 11),
            (h + 2)*(2*h + 3)*(4*h + 7),
            (h + 2)*(12*h*h + 39*h + 31),
            (44*h**3 + 231*h*h + 415*h + 255)/3,
        )
    raise ValueError('r must equal 1 or 3')

def exact_five_sums(h, r):
    L = h+1
    m = 4*L + r
    v = 2*L + (0 if r == 1 else 1)
    w = 3*L + (0 if r == 1 else 2)
    return (
        sp.summation((m-J)*(4*J-3*m),(J,w+1,m-1)),
        sp.summation((m-J)*(4*J-2*m),(J,v+1,w)) + sp.summation((m-J)*(4*m-4*J),(J,w+1,m-1)),
        sp.summation((m-J)*(4*J-m),(J,L+1,v)) + sp.summation((m-J)*(3*m-4*J),(J,v+1,w)),
        sp.summation((m-J)*4*J,(J,1,L)) + sp.summation((m-J)*(2*m-4*J),(J,L+1,v)),
        m*m + 2*sp.summation((m-J)*(m-4*J),(J,1,L)),
    )

def q_from_five(c):
    a,b,c2,d,e=c
    return sp.expand(a*(1+Z**8)+b*(Z+Z**7)+c2*(Z**2+Z**6)+d*(Z**3+Z**5)+e*Z**4)

def direct_coeffs(m,n):
    # Coefficient c_{4+t}, direct finite triangular convolution.
    cs={}
    for t in range(-4,5):
        cs[t+4] = sum(max(m-abs(A),0)*max(m-abs(m*t-4*A),0)
                       for A in range(-m+1,m))
    return [cs[i] for i in range(9)]

def f_from_five(c):
    a,b,c2,d,e=c
    Y=sp.symbols('y')
    return sp.expand(a*(Y**4-4*Y**2+2)+b*(Y**3-3*Y)+c2*(Y**2-2)+d*Y+e)

Y=sp.symbols('y')
for r in (1,3):
    expected=tuple(map(sp.factor,coeffs_closed(H,r)))
    exact=exact_five_sums(H,r)
    for e0,e1 in zip(expected,exact):
        ck(sp.simplify(e0-e1)==0,'symbolic tent-sum coefficient identity')
    f=f_from_five(expected)
    if r==1:
        coeff_u=[4*H+5,
            -2*(H+1)*(8*H**2+22*H+27)/3,
            -(H+1)*(8*H**2+22*H+39)/3,
            H*(H+1)*(4*H+11)/3,
            (H+1)*(H+2)*(4*H+3)/6]
        f3=-(12*H**3+45*H**2+85*H+50)/2
    else:
        coeff_u=[4*H+7,
            -2*(H+2)*(8*H**2+26*H+33)/3,
            -(H+2)*(8*H**2+26*H+45)/3,
            (H+2)*(H+3)*(4*H+1)/3,
            (H+1)*(H+2)*(4*H+9)/6]
        f3=-(12*H**3+63*H**2+139*H+124)/2
    transformed=sp.Poly(sp.expand(f.subs(Y,-2-U)),U)
    for i,expr in enumerate(coeff_u):
        ck(sp.simplify(transformed.coeff_monomial(U**i)-expr)==0,
           'symbolic Descartes sign coefficient')
    ck(sp.simplify(f.subs(Y,-3)-f3)==0,'symbolic crossing value')
    ck(sp.simplify(f.subs(Y,-2)-(4*H+4+r))==0,'symbolic left-end value')
    for h in range(0,21):
        n=4*h+r;m=n+4
        exact_values=[int(sp.expand(c.subs(H,h))) for c in expected]
        actual=direct_coeffs(m,n)
        for j,expect in enumerate([exact_values[0],exact_values[1],exact_values[2],exact_values[3],exact_values[4],exact_values[3],exact_values[2],exact_values[1],exact_values[0]]):
            ck(actual[j] == expect,'independent exact centered coefficient sum')
        ck(all(k>0 for k in actual),'positive coefficients')
        ck(actual==actual[::-1],'reciprocal coefficients')
        ck(sum(actual)==m**3,'normalized value at one')
        # Certified real-zero count with exact rational arithmetic.
        f0=sp.Poly(f.subs(H,h),Y)
        ck(f0.count_roots(-sp.oo,-3)==1,'one real reduced root <-3')
        ck(f0.count_roots(-3,-2)==1,'one real reduced root in (-3,-2)')
        ck(f0.count_roots(-2,sp.oo)==0,'no other real reduced roots')
    for h in range(0,5):
        n=4*h+r
        poly=sp.Poly(q_from_five([e.subs(H,h) for e in expected]),Z)
        roots=sp.nroots(poly,n=30,maxsteps=200)
        interior=[z for z in roots if abs(z)<1]
        real=[z for z in interior if abs(sp.im(z))<sp.Rational(1,10)**12]
        nonreal=[z for z in interior if abs(sp.im(z))>=sp.Rational(1,10)**12]
        ck(len(roots)==8 and len(interior)==4,'all eight roots and four inside')
        ck(len(real)==2 and len(nonreal)==2,'two negative real inside and conjugate nonreal pair')
        threshold=-(3-sp.sqrt(5))/2
        ck(sum(float(sp.re(z))<float(threshold) for z in real)==1,
           'unique real inner root in first interval')
        ck(sum(float(sp.re(z))>float(threshold) for z in real)==1,
           'unique real inner root in second interval')

print('PASS:',checks,'symbolic and finite checks')
