"""Symbolic and numerical checks of an exact conjugacy and escape thresholds."""
import sympy as s
import math
import numpy as np
x,y,z,a,alpha,Omega=s.symbols('x y z a alpha Omega',real=True)
u=x*x+y*y; k=a**4-1
P=alpha*x*z/4+Omega*y
Q=alpha*y*z/4-Omega*x
R=alpha*(-a*a*u+z*z+k)/2
operator=lambda f:s.simplify(s.diff(f,x)*P+s.diff(f,y)*Q+s.diff(f,z)*R)
X=k/u-a*a
Y=s.Symbol('q', positive=True)*z/u
q=s.Symbol('q', positive=True)
assert s.simplify(operator(X)+alpha*k*z/(2*u))==0
assert s.simplify(operator(Y)-alpha*q*(k/u-a*a)/2)==0
assert s.simplify((x*Q-y*P)/u+Omega)==0
H=s.factor(((u-a*a)**2+z*z-1)/u**2)
assert s.simplify(operator(H))==0
assert s.simplify((X**2+k*(z/u)**2)-(1+k*H))==0
assert s.simplify((k/u-a*a)**2+k*(z/u)**2-(1+k*H))==0
# numerical reconstruction and finite-difference ODE: various radii; complementary claims
A=2.0; al=1.3; Om=0.7; kk=A**4-1; sig=al*math.sqrt(kk)/2
for rad,phase in [(0.0,0.0),(1.5,0.6),(A*A-1e-4,1.2),(A*A,0.0),(A*A+3,0.2)]:
    X0=rad*math.cos(phase);Y0=rad*math.sin(phase)
    if X0<=-A*A:continue
    def inv(xx,yy,th):
        U=kk/(xx+A*A)
        return np.array([math.sqrt(U)*math.cos(th),math.sqrt(U)*math.sin(th),math.sqrt(kk)*yy/(xx+A*A)])
    xx=X0; yy=Y0
    p0=inv(xx,yy,.3)
    dt=1e-7
    xx2=xx*math.cos(sig*dt)-yy*math.sin(sig*dt)
    yy2=xx*math.sin(sig*dt)+yy*math.cos(sig*dt)
    p1=inv(xx2,yy2,.3-Om*dt)
    xp,yp,zp=p0
    deriv=np.array([al*xp*zp/4+Om*yp,al*yp*zp/4-Om*xp,al*(-A*A*(xp*xp+yp*yp)+zp*zp+kk)/2])
    error=np.max(abs((p1-p0)/dt-deriv))
    assert error<1e-4,(rad,error)
# exact lifetime independent of phase; extremal radii
lifetime=lambda rad: 2*math.acos(-A*A/rad)/abs(sig) if rad>A*A else 2*math.pi/abs(sig)
assert abs(lifetime(A*A+1e-7)-lifetime(A*A))<1e-3
assert abs(lifetime(1e10)-math.pi/abs(sig))<1e-9
print('QUADRATIC_TORUS_HARMONIC_CONJUGACY_CHECK_OK')
