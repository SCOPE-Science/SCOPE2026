#!/usr/bin/env python3
"""Independent symbolic and exact-arithmetic checks for the quadratic EA dynamics.

Only the equations and parameters of the mathematical statement are used.
The all-iteration assertions in the theorem follow by induction, not by finite checking.
"""
from fractions import Fraction
import sympy as sp

x,y,a,b=sp.symbols('x y a b')
f=lambda z,w: sp.factor(z-(z*z-1)*(z-w)/(2*z*(z-w)-(z*z-1)))
check=lambda lhs,rhs: sp.factor(lhs-rhs)==0
X=f(x,y); Y=f(y,x)
coords={x:(1+a)/(1-a),y:(1+b)/(1-b)}
Xab=sp.factor(X.subs(coords)); Yab=sp.factor(Y.subs(coords))
assert check((Xab-1)/(Xab+1), a*a/b)
assert check((Yab-1)/(Yab+1), b*b/a)
Ysequential=sp.factor(f(y,X).subs(coords))
assert check((Ysequential-1)/(Ysequential+1), b**3/a**2)
# The root-coordinate identity survives arbitrary noncoincident complex roots.
alpha,beta=sp.symbols('alpha beta')
P=(x-alpha)*(x-beta)
Xgen=sp.factor(x-P*(x-y)/(sp.diff(P,x)*(x-y)-P))
inv=lambda t:(alpha-beta*t)/(1-t)
Xgenab=sp.factor(Xgen.subs({x:inv(a),y:inv(b)}))
assert check((Xgenab-alpha)/(Xgenab-beta),a*a/b)
assert check((a*a/b)*(b*b/a),a*b)
assert check((a*a/b)**2*(b**3/a**2),a*a*b)
assert check((a*a/b)/(b*b/a),(a/b)**3)
assert check((a*a/b)/(b**3/a**2),(a/b)**4)

for q,(aa,bb) in [(3,(-1,2)),(4,(-2,3))]:
    mat=sp.Matrix([[2,-1],[aa,bb]])
    assert mat.eigenvals()=={1:1,q:1}
    for m in range(1,7):
        matpow=mat**m
        assert matpow.det()==q**m and matpow.trace()==1+q**m

# Exact samples of the native EA maps are crosschecked against closed forms.
# a_0=1/2,b_0=2 gives x_0=3,y_0=-3; inverse root coordinate is (1+a)/(1-a).
def native(z,w):
    return z-(z*z-1)*(z-w)/(2*z*(z-w)-(z*z-1))
for q,gauss_seidel in [(3,False),(4,True)]:
    a0,b0=Fraction(1,2),Fraction(2)
    xx,yy=Fraction(3),Fraction(-3)
    r=a0/b0
    for k in range(6):
        N=(q**k-1)//(q-1)
        aa=a0*r**N
        bb=b0*r**(-N if q==3 else -2*N)
        assert aa!=1 and bb!=1
        assert xx==(1+aa)/(1-aa) and yy==(1+bb)/(1-bb)
        if k<5:
            xx2=native(xx,yy)
            yy2=native(yy,xx2 if gauss_seidel else xx)
            xx,yy=xx2,yy2

# Check non-root period-two Jacobi example r=i, a=2, b=-2i.
r=sp.I
aa=sp.Integer(2)
bb=2/r
for k in range(2):
    aa,bb=sp.simplify(aa*aa/bb),sp.simplify(bb*bb/aa)
assert sp.simplify(aa-2)==0 and sp.simplify(bb-2/r)==0

# All prime m>=2 cycles exist because N_m = 1+q+...+q^(m-1)
# is greater than q^j-1 for each 1<=j<m. Confirm finite ranges.
for q in (3,4):
    for m in range(2,15):
        N=(q**m-1)//(q-1)
        assert all((q**j-1)%N!=0 for j in range(1,m))

# The two schemes have distinct pole-exception sets even off the separator.
for a0,b0,jacobi_pole,cyclic_pole in [(4,2,True,False),(8,4,False,True)]:
    A,B=sp.Rational(a0),sp.Rational(b0)
    jac=(A*A/B,B*B/A)
    cyc=(A*A/B,B**3/A**2)
    assert (sp.Integer(1) in jac)==jacobi_pole
    assert (sp.Integer(1) in cyc)==cyclic_pole
print('PASS: general-root and normalized symbolic conjugacies, invariant laws, 12 eigenspectrum certificates, 12 exact rational trajectories, exact pole asymmetry, a two-cycle, and 26 finite divisibility tests.')
