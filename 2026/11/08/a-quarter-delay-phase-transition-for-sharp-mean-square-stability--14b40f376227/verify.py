"""Exact and numerical checks for Bernoulli-delay momentum stability.
Requires Python 3, SymPy and NumPy. Run: python verify.py
"""
from fractions import Fraction
from math import sqrt
import sympy as sp
import numpy as np

p,h,b=sp.symbols('p h b', real=True)
A0=sp.Matrix([[1+b-h,-b],[1,0]])
A1=sp.Matrix([[1+b,-b-h],[1,0]])
x,y,z=sp.symbols('x y z')
X=sp.Matrix([[x,y],[y,z]])
def lift(A):
    Y=sp.expand(A*X*A.T)
    return sp.Matrix([[sp.expand(Y[i,j]).coeff(t) for t in (x,y,z)] for i,j in ((0,0),(0,1),(1,1))])
L=sp.expand((1-p)*lift(A0)+p*lift(A1))
F=2*b*b + (1+(4*p-1)*b)*h+p*h*h-2
assert sp.simplify(sp.det(sp.eye(3)-L)+h*F)==0
assert sp.simplify(F.subs(b,0)-(p*h*h+h-2))==0
assert sp.simplify(F.subs(p,1)-(h+2*b+2)*(h+b-1))==0
assert sp.simplify(F.subs(p,0)-((1-b)*h+2*b*b-2))==0
assert sp.simplify(sp.diff(F,b)-(4*b+(4*p-1)*h))==0
assert sp.simplify(sp.diff(F,h)-(1+(4*p-1)*b+2*p*h))==0

# Symbolically check the stationary candidate for low-delay probabilities.
t=sp.symbols('t', positive=True)
# Parameterize p by t^2/(1+t^2), so sqrt(p(1-p))=t/(1+t^2).
pp=t*t/(1+t*t)
rr=4*t/(1+t*t)
hs=4/(1+rr)
bs=(1-4*pp)/(1+rr)
assert sp.simplify(F.subs({p:pp,h:hs,b:bs}))==0
assert sp.simplify(sp.diff(F,b).subs({p:pp,h:hs,b:bs}))==0
assert sp.simplify(F.subs({p:sp.Rational(1,10),h:sp.Rational(7,4),b:sp.Rational(3,11)})+sp.Rational(315,3872))==0
assert sp.simplify(F.subs({p:sp.Rational(1,10),h:sp.Rational(7,4),b:0})-sp.Rational(9,160))==0

# Derivative at zero: moment map eigenvalue through 1 has slope -2/(1-beta).
Z=L.subs(h,0)
assert sp.simplify(Z.charpoly().as_expr()-(Z.charpoly().gen-1)*(Z.charpoly().gen-b)*(Z.charpoly().gen-b*b))==0

def rho(pp,hh,bb):
    mat=np.asarray(L.subs({p:pp,h:hh,b:bb}),dtype=float)
    return float(max(abs(np.linalg.eigvals(mat))))

checks=0
for pp in [0.01,0.1,0.24,0.25,0.4,0.8,0.99]:
    for bb in [0.,0.1,0.33,0.7,0.95]:
        B=1+(4*pp-1)*bb
        H=4*(1-bb*bb)/(B+sqrt(B*B+8*pp*(1-bb*bb))) # positive root? CHECK formula!
        # exact positive root is 4(1-b^2)/(B + sqrt(B^2+8p(1-b^2)))
        # should be 4(1-b^2)/(...) == (sqrt(D)-B)/(2p)
        assert abs((pp*H*H+B*H+2*bb*bb-2))<2e-9,(pp,bb,H)
        assert rho(pp, 0.90*H,bb)<1-1e-6,(pp,bb)
        assert abs(rho(pp,H,bb)-1)<1e-8,(pp,bb)
        assert rho(pp,1.10*H,bb)>1+1e-6,(pp,bb)
        checks+=3

for pp in [0.01,0.1,0.24,0.25,0.35,0.6,0.95]:
    if pp <0.25:
        HM=4/(1+4*sqrt(pp*(1-pp)))
        bm=(1-4*pp)/(1+4*sqrt(pp*(1-pp)))
    else:
        HM=4/(1+sqrt(1+8*pp));bm=0.0
    assert abs(pp*HM*HM+(1+(4*pp-1)*bm)*HM+2*bm*bm-2)<1e-10
    for b_test in np.linspace(0,.999,101):
        F_test=pp*HM**2+(1+(4*pp-1)*b_test)*HM+2*b_test*b_test-2
        assert F_test>-1e-9
        checks+=1

print('PASS: symbolic lift, determinant, endpoint, extremizer and rational checks')
print('PASS: %d fixed-grid numerical spectral and stability-region checks'%checks)
print('example p=1/10, h=7/4: rho(momentum 3/11)=%.12g, rho(no momentum)=%.12g'%(rho(.1,1.75,3/11),rho(.1,1.75,0)))
