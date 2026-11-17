import math
import numpy as np
import sympy as sp

l,g,w,u,v,c,s=sp.symbols('l g w u v c s', real=True)
H=sp.diag(-u,v)
R=sp.Matrix([[-c,-s],[-s,c]])
K=R*H
assert sp.simplify(K.trace()-(u+v)*c)==0
assert sp.simplify(K.det()-u*v*(c*c+s*s))==0
L=sp.eye(2)*l*l + sp.eye(2)*g*l + w*K
p=sp.expand(L.det().subs(s*s,1-c*c))
expected=l**4+2*g*l**3+(g**2+w*(u+v)*c)*l**2+g*w*(u+v)*c*l+w**2*u*v
assert sp.simplify(p-expected)==0
nu=sp.symbols('nu',positive=True,real=True)
qt=(l*l+nu*nu)*((l+g)**2+nu*nu)
assert sp.simplify(sp.expand(qt-expected).subs(nu**2,w*(u+v)*c/2).subs(u*v,(g*g*(u+v)*c/w+(u+v)**2*c*c/2)/2))==0

rng=np.random.default_rng(20261114)
for k in range(1000):
    uu,vv,gg,ww=np.exp(rng.uniform(-2,2,4))
    Tstar=(math.sqrt(gg**4+4*ww**2*uu*vv)-gg**2)/ww
    tc=Tstar/(uu+vv)
    assert 0<tc<1,(uu,vv,gg,ww,tc)
    theta=.5*math.acos(tc)
    for tt, target in [(0,1),(theta*.8,1),(theta,-0),(theta+(math.pi/4-theta)*.5,-1),(math.pi/4,-1),(.5*math.pi,-1)]:
        cs,ss=math.cos(2*tt),math.sin(2*tt)
        kval=np.array([[uu*cs,-vv*ss],[uu*ss,vv*cs]])
        a=np.block([[np.zeros((2,2)),np.eye(2)],[-ww*kval,-gg*np.eye(2)]])
        rr=np.linalg.eigvals(a)
        realmax=max(rr.real)
        if target==1: assert realmax<-1e-10,(k,tt,theta,realmax)
        elif target==-1: assert realmax>1e-10,(k,tt,theta,realmax)
        else: assert abs(realmax)<1e-7,(k,rr,theta)
        coeff=np.poly(a)
        correct=np.array([1,2*gg,gg**2+ww*(uu+vv)*cs,gg*ww*(uu+vv)*cs,ww**2*uu*vv])
        assert np.allclose(coeff,correct,rtol=1e-9,atol=1e-10)

# Concrete stability discrepancy: unit curvatures/damping, 30deg
ang=math.pi/6
Kexample=np.array([[math.cos(2*ang),-math.sin(2*ang)],[math.sin(2*ang),math.cos(2*ang)]])
a=np.block([[np.zeros((2,2)),np.eye(2)],[-Kexample,-np.eye(2)]])
assert all(z.real<0 for z in np.linalg.eigvals(-Kexample))
assert any(z.real>0 for z in np.linalg.eigvals(a))
threshold=.5*math.acos((math.sqrt(5)-1)/2)
print('PASS symbolic determinant & factorization; 1000 random parameter families, 6000 eigenvalue checks and 6000 coefficient comparisons')
print('unit theta_critical radians', threshold,'degrees',math.degrees(threshold))
print('unit theta 30deg spectrum',np.linalg.eigvals(a))
