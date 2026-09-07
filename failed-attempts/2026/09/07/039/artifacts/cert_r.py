import sympy as sp
from fractions import Fraction
import json

x=sp.Symbol('x')

def sturm_seq(p):
    return sp.sturm(sp.Poly(p,x))

def sgn_at(poly, v):
    # exact sign of univariate Poly at Rational v (or 'inf')
    if v=='inf': return 1 if poly.LC()>0 else -1
    if v=='-inf':
        lc=poly.LC(); d=poly.degree()
        return (1 if lc>0 else -1)*((-1)**d)
    val=poly.eval(v)  # exact with Rational
    return (1 if val>0 else (-1 if val<0 else 0))

def variations(seq, v):
    signs=[s for s in (sgn_at(p,v) for p in seq) if s!=0]
    return sum(1 for a,b in zip(signs,signs[1:]) if a!=b)

def count_gt(seq, B):
    # # distinct roots in (B, oo)
    return variations(seq, sp.Rational(B))-variations(seq,'inf')

def count_all(seq):
    return variations(seq,'-inf')-variations(seq,'inf')

# ---- r(y): degree-4 factor in y=x^2
y=sp.Symbol('y')
r=sp.Poly(y**4-12*y**3+43*y**2-52*y+16, y)
# sympy sturm needs same symbol; rebuild in x
rx=sp.Poly(x**4-12*x**3+43*x**2-52*x+16, x)
seq=sturm_seq(rx)
print("len sturm:",len(seq))
print("total distinct real roots of r:",count_all(seq))
print("roots of r in (169/25,oo):",count_gt(seq, sp.Rational(169,25)))
print("roots of r in (-oo,-169/25):", variations(seq,'-inf')-variations(seq, sp.Rational(-169,25)))
# exact fraction checks
B=Fraction(169,25)
def rval(t): return t**4-12*t**3+43*t**2-52*t+16
def rpval(t): return 4*t**3-36*t**2+86*t-52
print("r(169/25) =",rval(B),">0:",rval(B)>0)
print("r(-169/25)=",rval(-B),">0:",rval(-B)>0)
print("r'(169/25)=",rpval(B),">0:",rpval(B)>0)
print("r'(-169/25)=",rpval(-B),"<0:",rpval(-B)<0)
# r''(y)=12y^2-72y+86; for y>=169/25: (y-3)^2>=(94/25)^2
t=Fraction(94,25)
print("12*(94/25)^2-22 =",12*t*t-22,">0:",12*t*t-22>0)
print("sqrt2<8/5 check: 2 < (8/5)^2 =",Fraction(64,25), 2<Fraction(64,25))
print("sqrt5<12/5 check: 5 < (12/5)^2 =",Fraction(144,25), 5<Fraction(144,25))
print("(13/5)^2 =",(Fraction(13,5))**2)
# numeric roots of r for the record
import numpy as np
print("numeric roots r:",np.sort(np.roots([1,-12,43,-52,16])))
