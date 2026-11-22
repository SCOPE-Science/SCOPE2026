"""Exact and numerical supplementary checks for the three-character Poisson fourth-moment theorem.

Install sympy (e.g. pip install -r requirements.txt).  Run python checker.py.
"""
import math
from fractions import Fraction
from itertools import product
import sympy as s

checks=0

def verify(z):
    global checks
    assert bool(z)
    checks += 1

a,b=s.symbols('a b', positive=True,real=True)
x,y,z=s.symbols('x y z',real=True)
t=s.symbols('t',real=True)
w=[s.Integer(1),a,b]
Q=s.Matrix([[w[i]**2 if i==j else 2*w[i]*w[j] for j in range(3)] for i in range(3)])
H=sum(1/wi for wi in w); J=sum(1/wi**2 for wi in w)
Den=2*H**2-5*J
xs=s.Matrix([s.cancel((2*H/wi-5/wi**2)/Den) for wi in w])
verify(s.simplify(sum(xs)-1)==0)
verify(s.simplify((xs.T*Q*xs)[0]-5/Den)==0)
for i in (1,2):verify(s.simplify((Q*xs)[i]-(Q*xs)[0])==0)
bcrit=s.Rational(3,2)*a/(1+a)
T=s.Matrix([[a*a-4*a+1,2*a*b-2*a-2*b+1],[2*a*b-2*a-2*b+1,b*b-4*b+1]])
det=s.factor(T.det())
verify(s.simplify(det.subs(b,bcrit)+15*a*a*(a*a-4*a+1)/(4*(a+1)**2))==0)
verify(s.simplify(det.subs(b,a)-a*a*(-3*a*a+8*a-2))==0)
verify(s.simplify(s.diff(det,b,2)+2*(3*a*a-4*a+3))==0)
for i in range(3):verify(s.simplify(xs[i].subs(b,bcrit)-([a*(2-a)/(4*a-1-a*a),(2*a-1)/(4*a-1-a*a),0][i]))==0)

# Exact Fourier convolution identity for arbitrary three complex coefficients.
I=s.I
for m in range(1,13):
    for n in range(m+1,16):
        for u,v,k in [(1+I,2-I,3+2*I),(s.Rational(1,2)-I,2+3*I,1+I),(1,s.Rational(2,3),I)]:
            coeff={0:u,m:v*a,n:k*b}
            convolution={}
            for k1,c1 in coeff.items():
                for k2,c2 in coeff.items():
                    convolution[k1+k2]=convolution.get(k1+k2,0)+c1*c2
            observed=s.expand(sum(s.expand(q*s.conjugate(q)) for q in convolution.values()))
            base=(u*s.conjugate(u))**2+a**4*(v*s.conjugate(v))**2+b**4*(k*s.conjugate(k))**2
            base+=4*a**2*(u*s.conjugate(u))*(v*s.conjugate(v))
            base+=4*b**2*(u*s.conjugate(u))*(k*s.conjugate(k))
            base+=4*a**2*b**2*(v*s.conjugate(v))*(k*s.conjugate(k))
            if n==2*m:base+=2*a**2*b*(u*k*s.conjugate(v)**2+s.conjugate(u*k)*v**2)
            verify(s.expand(observed-base)==0)

# Here a and b in the convolution above are AMPLITUDE multipliers;
# the theorem uses squared multipliers a=rho^(2m), b=rho^(2n).
R=x**4+a*a*y**4+a**4*z**4+4*a*x*x*y*y+4*a*a*x*x*z*z+4*a**3*y*y*z*z+4*a*a*x*y*y*z
S=(x*x+y*y+z*z)**2-R.subs(a,s.Rational(1,2))
SOS=(x*z-y*y/2)**2+y**4/2+s.Rational(15,16)*z**4+s.Rational(3,2)*y*y*z*z
verify(s.expand(S-SOS)==0)
# Series in the resonant near-critical variables: y^2=t, z=z.
delta,U,V=s.symbols('delta U V',real=True)
q=s.sqrt(1-t-z*z)
rr=R.subs({x:q,y**4:t*t,y**2:t})  # explicitly evaluate all y even powers
rr=s.expand(rr)
series=s.series(rr.subs({t:delta*U,z:delta*V,a:s.Rational(1,2)+delta}),delta,0,3).removeO().expand()
verify(s.simplify(series.coeff(delta,1))==0)
verify(s.simplify(series.coeff(delta,2)-(-s.Rational(3,4)*U*U+U*V+4*U-V*V))==0)

# For every physically feasible pair 0<b<=a<=1, random simplex profiles obey
# the exact nonresonant sharp formula and the two forbidden-mode thresholds.
import random
rng=random.Random(1927)
for aa in [s.Rational(1,2),s.Rational(11,20),s.Rational(3,4),s.Rational(4,5),s.Rational(9,10),s.Integer(1)]:
    for bb in [aa/5,aa/2,3*aa/(2*(1+aa)),aa*(1+s.Rational(3,2)/(1+aa))/2,aa]:
        if bb>aa:continue
        ac=float(aa);bc=float(bb)
        if aa<=s.Rational(1,2): M=1.0
        elif bb<=s.Rational(3,2)*aa/(1+aa):M=float(1+(2*aa-1)**2/(4*aa-1-aa*aa))
        else:M=float((5/Den).subs({a:aa,b:bb}))
        verify(M>=1-1e-10)
        for k in range(45):
            xx=[rng.random() for _ in range(3)]
            xx=[u/sum(xx) for u in xx]
            val=sum(([1,ac,bc][i]**2*xx[i]**2) for i in range(3))
            val+=4*sum([1,ac,bc][i]*[1,ac,bc][j]*xx[i]*xx[j] for i in range(3) for j in range(i+1,3))
            verify(val<=M+1e-11)

# The two threshold roots rho^(2(n-m))*(1+rho^(2m))=3/2
# must exist between the constant-mode threshold and radius 1.
for m in range(1,18):
    for n in range(m+1,23):
        r0=2.0**(-1/(2*m))
        verify(r0**(2*(n-m))*(1+r0**(2*m))<1.5)
        verify(1**(2*(n-m))*(1+1**(2*m))>1.5)

print('PASS:',checks,'exact algebraic, convolutional and numerical checks')
