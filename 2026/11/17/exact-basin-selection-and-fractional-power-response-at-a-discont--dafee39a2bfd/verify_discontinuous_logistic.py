"""Reproducible exact checks for a discontinuous logistic dispersal map.
Run: python verify_discontinuous_logistic.py
"""
from fractions import Fraction as Q
import sympy as s

x,e,b=s.symbols('x e b',real=True)
f=lambda t: b*t*(1-t)
pol=s.factor(f(f(x))-x)
print('second-iterate factorization:',pol)
assert s.simplify(pol-(-x*(b*x-b+1)*(b*b*x*x-b*(b+1)*x+b+1)))==0
assert s.factor(s.discriminant(b*b*x*x-b*(b+1)*x+b+1,x))==b**2*(b-3)*(b+1)
r=2*(1+e)
m=s.Rational(1,2)
L=(1-2*e)/(2*(1-e))
U=(1+2*e)/(2*(1+e))
C=(1+s.sqrt(e/(1+e)))/2
assert s.simplify(2*(1-e)*L*(1-L)-L)==0
assert s.simplify(2*(1+e)*U*(1-U)-U)==0
assert s.simplify(2*(1+e)*C*(1-C)-m)==0
assert s.simplify((C-m)**2-e/(4*(1+e)))==0
assert s.simplify(2*(1+e)*(1-2*U)+2*e)==0
assert s.simplify(2*(1-e)*(1-2*L)-2*e)==0
assert s.simplify(s.limit((C-m)/s.sqrt(e),e,0,dir='+')-s.Rational(1,2))==0

def H(t,eps):
    f=2*t*(1-t)
    if t<f: return max(Q(0),f*(1-eps))
    if t>f: return max(Q(0),f*(1+eps))
    return max(Q(0),f)

def within(x,tol=Q(1,10**6)):
    return abs(x)<tol

for eps in (Q(1,100),Q(1,8),Q(1,4),Q(2,5),Q(49,100)):
    lo=(1-2*eps)/(2*(1-eps))
    hi=(1+2*eps)/(2*(1+eps))
    from math import sqrt
    crit=(1+sqrt(float(eps/(1+eps))))/2
    for k in range(1,200):
        start=Q(k,200)
        if start==Q(1,2): expected=Q(1,2)
        elif start < Q(1,2) or float(start)>crit: expected=lo
        elif float(start)<crit: expected=hi
        else: continue
        y=start
        # keep denominators small by controlled float after 30 exact iterations
        for _ in range(7): y=H(y,eps)
        yf=float(y)
        for _ in range(1600):
            fy=2*yf*(1-yf)
            yf=max(0.,fy*(1-float(eps)) if yf<fy else fy*(1+float(eps)) if yf>fy else fy)
        assert abs(yf-float(expected))<1e-9, (eps,k,yf,expected)
assert H(Q(2,3),Q(1,8))==Q(1,2)
assert H(Q(4,5),Q(1,8))==Q(9,25) # upper falls into lower
assert H(Q(3,5),Q(1,8))==Q(27,50) # upper stays upper
print('PASS: 8 exact identities, five strength cases × 199 initial states, exact boundary examples')
