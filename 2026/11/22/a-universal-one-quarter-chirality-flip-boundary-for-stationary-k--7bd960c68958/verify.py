"""Reproduce the fourth-cumulant identity and independent ordered-time checks.

Requires Python 3 and SymPy. The independent resolvent calculation uses only
Python's standard library. Run: python verify.py
"""
from functools import lru_cache
from itertools import permutations
import math
import random
import sympy as sp

G, L, W = sp.symbols("g ell omega", real=True)
@lru_cache(None)
def moment(p, q):
    if p == q == 0:
        return sp.Integer(1), sp.Integer(0)
    m = q - p
    n = p + q + G*m*m
    rs = ra = sp.Integer(0)
    if p:
        x, y = moment(p-1,q)
        rs += p*x; ra += p*y
    if q:
        x, y = moment(p,q-1)
        rs += q*x; ra += q*y
    den = n*(n+2*L) + m*m*W*W
    return (sp.cancel(((n+2*L)*rs+sp.I*m*W*ra)/den),
            sp.cancel((sp.I*m*W*rs+n*ra)/den))

A = 4*L - 1
B = (10*G**3 + (13*L+8)*G**2 - (28*L**2+38*L+12)*G
     - (28*L**3+68*L**2+47*L+10))
C = (14*G**5+(91*L+83)*G**4+(210*L**2+396*L+166)*G**3
     +(196*L**3+594*L**2+538*L+148)*G**2
     +(56*L**4+280*L**3+454*L**2+284*L+60)*G
     +(24*L**4+84*L**3+102*L**2+51*L+9))
H = ((G**2+2*G*L+2*G+2*L+W**2+1)**2
   * (G**2+2*G*L+6*G+6*L+W**2+9)
   * (4*G**2+2*G*L+4*G+L+W**2+1))

# Reconstruct every stationary mixed angular moment up to degree four.
m2 = sp.factor(moment(1,1)[0]); m4 = sp.factor(moment(2,2)[0])
assert sp.cancel(m2-(G+2*L+1)/(G**2+2*G*L+2*G+2*L+W**2+1)) == 0
assert sp.cancel((m4-2*m2*m2)*H-(A*W**4+B*W**2-C)) == 0
assert sp.factor(B.subs(L,sp.Rational(1,4))-(2*G+3)*(80*G**2-30*G-141)/16)==0
assert sp.factor((m4-2*m2*m2).subs(W,0)-(m4-2*m2*m2).subs({W:0,L:0}))==0
print('Exact generator identity, thermal independence, and critical factorization: PASS')

# Independent evaluation: integrate all 24 chronological orderings of the
# four angular factors using 2x2 Fourier-tilted Markov resolvents.
def multiply(a,b):
    return ((a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]),
            (a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]))

def resolvent(mode, rate, g, ell, omega):
    # rate*I minus Fourier generator for angle with telegraph torque.
    a = complex(rate+g*mode**2+ell,-mode*omega)
    d = complex(rate+g*mode**2+ell,mode*omega)
    det = a*d-ell*ell
    return ((d/det,ell/det),(ell/det,a/det))

def time_ordered_integral(charges,g,ell,omega):
    n=len(charges)
    answer=0j
    for order in permutations(charges):
        product=((1+0j,0j),(0j,1+0j))
        for j in range(n-1,0,-1):
            product=multiply(product,resolvent(sum(order[:j]),n-j,g,ell,omega))
        answer += (product[0][0]+product[0][1]+product[1][0]+product[1][1])/2
    assert abs(answer.imag)<1e-9
    return answer.real/n

rng=random.Random(20261119)
cases=[(1,1,8),(1,1,10),(5,.1,5),(5,.1,20),(5,.1,60),
       (3,.25,10),(1,.2,0)]
for _ in range(30):
    cases.append((rng.uniform(.15,7),rng.uniform(.03,3),rng.uniform(.2,24)))
for g,ell,omega in cases:
    r2=time_ordered_integral((1,-1),g,ell,omega)
    r4=time_ordered_integral((1,1,-1,-1),g,ell,omega)
    assert math.isclose(r2,float(m2.subs({G:g,L:ell,W:omega})),abs_tol=2e-10,rel_tol=1e-9)
    rat=float(((A*W**4+B*W**2-C)/H).subs({G:g,L:ell,W:omega}))
    assert math.isclose(r4-2*r2*r2,rat,abs_tol=2e-10,rel_tol=2e-8), (g,ell,omega)
print(f'Independent time-ordered integrals and cumulants: {len(cases)} parameter checks PASS')

# Exact double-crossing and single-crossing representative cases.
for g,ell,omega,sign in [(1,1,8,-1),(1,1,10,1),(5,.1,5,-1),
                         (5,.1,20,1),(5,.1,60,-1)]:
    val=float(((A*W**4+B*W**2-C)/H).subs({G:g,L:ell,W:omega}))
    assert val*sign>0
print('One-crossing and reentrant two-crossing sign witnesses: PASS')
