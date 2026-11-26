"""Independent algebraic and numerical checks for the small-band matrix-sine endpoint norm."""
import sympy as s
import numpy as np
from scipy.linalg import sinm
from math import sqrt
x,y,z,p,q,r,t,u=s.symbols('x y z p q r t u',real=True)
B=s.Matrix([[x,y],[y,z]])
H=s.Matrix([[p,q],[q,r]])
S=s.expand(B**2*H+B*H*B+H*B**2)
assert s.expand(S[0,0]-( (3*x*x+2*y*y)*p+2*y*(2*x+z)*q+y*y*r))==0
assert s.expand(S[0,1]-(y*(2*x+z)*p+(x*x+x*z+z*z+3*y*y)*q+y*(x+2*z)*r))==0
CD=-3*x*x-y*y+2*y*(2*x+z)
CO=-(x*x+x*z+z*z+3*y*y)+3*y*(x+z)
cr=s.expand(CD.subs({x:r+(1-r)*t,y:(1-r)*u,z:r+(1-r)*(1-t)}))
cr=s.expand(cr.subs(u**2,t*(1-t)))
C=-2*t*t-t+2*(1+t)*u
a=2*u*(1-2*t-2*u)
D=(1-t)*(3-2*t+2*u)+2*u
assert s.rem(s.expand(cr-C-a*r+D*r*r), u*u-t*(1-t), u)==0
# Exact constants for the two intervals of the rank-one optimization.
R=s.Rational
assert R(1,8)<R(51,400)<R(9,25)**2
assert R(17,20)*R(27,10)>2 and R(8,5)*R(9,25)<1
envelope=C.subs({t:R(3,20),u:R(9,25)})+R(18,25)**2/8
assert envelope<R(7,10) and 3>((8*R(7,10)+3)/5)**2
P=32*t**4-16*t**3-14*t**2+t+1
assert s.expand((1+t-4*t*t)**2-(4*t+1)**2*t*(1-t)-P)==0
assert s.Poly(P,t).count_roots(0,s.Rational(2,3))==1
assert s.Poly(P,t).count_roots(s.Rational(2,3),1)==1
root=0.283554610289061
assert abs(float(P.subs(t,root)))<1e-12
k=(-2*root*root-root+2*(1+root)*sqrt(root*(1-root)))/6
assert 0.1187824<k<0.1187825
# C_o row negative: for eigenvalues 1,r and y=(1-r)u, u<=1/2,
# C_o=-1-r-r^2-2y^2+3(1+r)y, increasing on [0,(1-r)/2], max -3r^2.
for rv in np.linspace(0,1,51):
    ymax=(1-rv)/2
    assert abs((-1-rv-rv*rv-2*ymax**2+3*(1+rv)*ymax)+3*rv*rv)<1e-12
# Finite interval derivative identity: sin(A) via central difference,
# max entry relative sensitivity, orientation at rank-one optimum.
Bstar=np.array([[root, sqrt(root*(1-root))],[sqrt(root*(1-root)),1-root]])
assert np.allclose(Bstar@Bstar,Bstar)
Hstar=np.array([[1.,-1.],[-1.,-1.]])
for bb in (0.1,0.05,0.025):
    A=bb*(1-2e-5)*Bstar+bb*1e-5*np.eye(2)
    dh=bb*1e-7
    F=(sinm(A+dh*Hstar)-sinm(A-dh*Hstar))/(2*dh)
    assert abs(F[0,0])>1.
    ratio=(F[0,0]-1)/(bb*bb)
    assert abs(ratio-k)<1e-3
# Random matrix spectral domains, random perturbation controls of the expansion
rng=np.random.default_rng(23641)
for _ in range(400):
    v=rng.normal(size=(2,2)); Q,_=np.linalg.qr(v)
    vals=rng.uniform(0,1,size=2)
    M=Q@np.diag(vals)@Q.T
    W=rng.uniform(-1,1,size=(2,2)); W=(W+W.T)/2
    hh=1e-5;bb=.08
    d=(sinm(bb*M+hh*W)-sinm(bb*M-hh*W))/(2*hh)
    expected=W-bb*bb/6*(M@M@W+M@W@M+W@M@M)
    assert np.max(abs(d-expected))<2e-5
print('PASS: symbolic coefficients, Sturm root counts, rank-one sharpness, 400 random Taylor tests; k=',k)
