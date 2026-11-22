"""Reproducibility checks for three-knot natural cubic spline quadrature.
Run: python verify.py (requires SymPy 1.14.0)."""
import random
from fractions import Fraction
import sympy as S

a, b, t, z = S.symbols('a b t z', positive=True)
y0, y1, y2 = S.symbols('y0 y1 y2')
M1 = 3 / (a + b) * ((y2 - y1) / b - (y1 - y0) / a)
area = a * (y0 + y1) / 2 + b * (y1 + y2) / 2 - (a**3 + b**3) * M1 / 24
w_raw = [S.factor(S.diff(area, v)) for v in (y0, y1, y2)]
expected = [
    (3*a*a + a*b - b*b)/(8*a),
    (a+b)*(a*a+3*a*b+b*b)/(8*a*b),
    (3*b*b+a*b-a*a)/(8*b),
]
assert all(S.cancel(w - ex) == 0 for w,ex in zip(w_raw,expected))
W = [S.factor(w.subs({a:t,b:1-t}, simultaneous=True)) for w in w_raw]
w0=(t+3-1/t)/8
w1=(1+t-t*t)/(8*t*(1-t))
w2=(4-t-1/(1-t))/8
assert all(S.cancel(w-e)==0 for w,e in zip(W,[w0,w1,w2]))
assert S.cancel(sum(W)-1) == 0
assert S.cancel(t*W[1]+W[2]-S.Rational(1,2)) == 0

q = (S.sqrt(13)-3)/2
assert S.simplify(w0.subs(t,q))==0
assert S.simplify(w2.subs(t,1-q))==0
assert S.simplify(1-2*q-(4-S.sqrt(13)))==0
n_left=S.factor(1-2*w0)
assert S.cancel(n_left-(1-t+1/t)/4)==0
# The inverse of n_left(t)=z is the positive root of t^2+(4z-1)t-1.
r=(S.sqrt((4*z-1)**2+4)-(4*z-1))/2
assert S.simplify(r*r+(4*z-1)*r-1)==0
assert S.limit(z*(2*r),z,S.oo)==S.Rational(1,2)
assert S.limit(t*w0,t,0,dir='+') == -S.Rational(1,8)
assert S.limit(t*w1,t,0,dir='+') == S.Rational(1,8)
assert S.limit(t*w2,t,0,dir='+') == 0
assert S.limit(t*t*sum(w*w for w in W),t,0,dir='+')==S.Rational(1,32)

# Independent exact rational checks of normalized areas, signs, and weight sums.
R=random.Random(35)
for _ in range(360):
    aa=Fraction(R.randint(1,100),R.randint(1,50))
    bb=Fraction(R.randint(1,100),R.randint(1,50))
    Y=[Fraction(R.randint(-10,10),R.randint(1,20)) for _ in range(3)]
    m=3*(((Y[2]-Y[1])/bb)-((Y[1]-Y[0])/aa))/(aa+bb)
    integral=(aa*(Y[0]+Y[1])+bb*(Y[1]+Y[2]))/2-(aa**3+bb**3)*m/24
    ww=[Fraction(3*aa*aa+aa*bb-bb*bb,8*aa*(aa+bb)),
        Fraction(aa*aa+3*aa*bb+bb*bb,8*aa*bb),
        Fraction(3*bb*bb+aa*bb-aa*aa,8*bb*(aa+bb))]
    assert sum(ww)==1
    assert integral/(aa+bb)==sum(w*y for w,y in zip(ww,Y))
    assert (min(ww)>=0)==(aa/bb <= (1+13**0.5)/2 and bb/aa <= (1+13**0.5)/2)

print('PASS: 3 symbolic weight identities, normalization, affine exactness, positivity boundaries, tail inversion and coefficient, squared-noise asymptotic; 360 exact-rational independent spline-integral checks')
