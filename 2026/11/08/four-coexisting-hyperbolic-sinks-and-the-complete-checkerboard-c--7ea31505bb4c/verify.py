"""Exact polynomial and interval checks for the alternating Gumowski--Mira fixed points.

Requires Python 3, SymPy, and NumPy. No external data are needed.
The general ring-size assertion follows from the Fourier proof, not from finite tests.
"""
from fractions import Fraction as R
import sympy as s
import numpy as np

z=s.symbols('z')
a,b,mu,e=s.Rational(33,100),s.Rational(1,10),s.Rational(-3,5),s.Rational(3,10)
g=mu+2*(1-mu)/(1+z)
H=(1-e)*((1+a)*(g-1)-a*b*z*(g-1)**3+g)-(1+e)
Q=3696*z**4-136463*z**3-161162*z**2+27929*z+78500
assert s.factor(H*(1+z)**3-s.Rational(2,78125)*Q)==0
bounds=[(s.Rational(5,8),s.Rational(63,100)),(s.Integer(38),s.Integer(39))]
for left,right in bounds:
    assert Q.subs(z,left)>0 if left==s.Rational(5,8) else Q.subs(z,left)<0
    assert Q.subs(z,right)<0 if left==s.Rational(5,8) else Q.subs(z,right)>0
# Descartes' rule of signs (+,-,-,+,+) gives <=2 positive roots counted with multiplicity.
assert s.Poly(Q,z).all_coeffs()==[3696,-136463,-161162,27929,78500]
fp=mu+2*(1-mu)*(1-z)/(1+z)**2
ypow=z*(g-1)**2
ap=(1+a)-3*a*b*ypow
D=(1-e)*ap
L,U=bounds[0]
assert (s.diff(fp,z).subs(z,s.Rational(5,8))<0)  # derivative (16/5)*(z-3)/(1+z)^3
assert s.factor(s.diff(fp,z)-s.Rational(16,5)*(z-3)/(1+z)**3)==0
assert fp.subs(z,L)<-s.Rational(7,50)
assert fp.subs(z,U)>-s.Rational(4,25)
ypow_upper=U*s.Rational(64,25)*((1-L)/(1+L))**2
assert ypow_upper<s.Rational(9,100)
assert (1-e)*((1+a)-3*a*b*s.Rational(9,100))>s.Rational(9,10)
assert (1-e)*(1+a)<s.Rational(19,20)
assert ((1-e)+s.Rational(19,20))*s.Rational(4,25)+e==s.Rational(141,250)
assert s.Rational(141,250)**2<4*s.Rational(9,10)
# Outer branch: z>=38 implies y^2>50 and determinant<-1.
assert 38*s.Rational(64,25)*(s.Rational(37,39))**2>50
assert (1-e)*((1+a)-3*a*b*50)<-1
# Homogeneous +/-1 sinks: trace and determinant bounds for all Fourier q in [-1,1].
D0=s.Rational(7,10)*s.Rational(133,100)
Tmax=s.Rational(3,5)*(s.Rational(7,10)+D0)+s.Rational(3,10)
assert 0<D0<1 and Tmax*Tmax<4*D0
# Numerical replay at the actual fixed-point states for several full ring sizes.
root_small=0.625755804100183
root_big=38.0618273205942
A=lambda y:float((1+a)*y-a*b*y**3)
F=lambda x:float(mu*x+2*(1-mu)*x/(1+x*x))
moduli=[]
for n in (2,4,6,10,50):
    for zz in (root_small,root_big):
        u=zz**.5
        v=u*(float(mu)+2*(1-float(mu))/(1+zz)-1)
        x=np.array([u if i%2==0 else -u for i in range(n)])
        y=np.array([v if i%2==0 else -v for i in range(n)])
        newx=(1-float(e))*(np.array([A(t) for t in y])+np.array([F(t) for t in x])) + float(e)*(np.roll(x,1)+np.roll(x,-1))/2
        newy=-x+np.array([F(t) for t in newx])
        assert max(abs(newx-x))<3e-9 and max(abs(newy-y))<3e-9
        ff=float(fp.subs(z,zz)); aa=float(ap.subs(z,zz)); dd=(1-float(e))*aa
        for k in range(n):
            q=np.cos(2*np.pi*k/n)
            t=((1-float(e))*ff+float(e)*q)+ff*dd
            roots=np.roots([1,-t,dd])
            if zz==root_small:
                assert max(abs(abs(lam)-dd**.5) for lam in roots)<2e-13
                assert max(abs(lam) for lam in roots)<1
            else:
                assert max(abs(lam) for lam in roots)>1
    # homogeneous +/-1
    for u in (-1.,1.):
        x=np.full(n,u); y=np.zeros(n)
        newx=(1-float(e))*(np.array([A(t) for t in y])+np.array([F(t) for t in x])) +float(e)*(np.roll(x,1)+np.roll(x,-1))/2
        newy=-x+np.array([F(t) for t in newx])
        assert max(abs(newx-x))<3e-12 and max(abs(newy-y))<3e-12
        for k in range(n):
            q=np.cos(2*np.pi*k/n)
            t=float(mu)*((1-float(e))+float(D0))+float(e)*q
            lam=np.roots([1,-t,float(D0)])
            assert max(abs(abs(v)-float(D0)**.5) for v in lam)<2e-13
print('VERIFY_OK polynomial_identity=1 exact_root_brackets=4 stability_rational_bounds=12 ring_sizes=5 states_checked=20 Fourier_modes_checked=288')
