"""Reproducible symbolic and independent finite-time checks for the four-direction velocity process."""
import math
import sympy as sp
import numpy as np
from scipy.linalg import expm

def analytic(a,b,h,v,theta):
    m=a+b
    ell=m+2*h
    omega=a-b
    qq=ell*ell+omega*omega
    ff=ell*((2*m-ell)*ell*ell-(ell+2*m)*omega*omega)
    k2=v*v*ell/qq
    k4=-3*v**4*(ff+qq*qq*math.sin(2*theta)**2)/(m*qq**3)
    return k2,k4

def finite_moments(a,b,h,v,theta,t):
    q=np.zeros((4,4))
    for j in range(4):
        q[j,j]=-(a+b+h)
        q[j,(j+1)%4]=a
        q[j,(j-1)%4]=b
        q[j,(j+2)%4]=h
    vv=np.array([v*math.cos(theta),v*math.sin(theta),-v*math.cos(theta),-v*math.sin(theta)])
    z=np.zeros((20,20))
    for n in range(5):
        z[4*n:4*n+4,4*n:4*n+4]=q.T
        if n>0:
            z[4*n:4*n+4,4*(n-1):4*n]=n*np.diag(vv)
    init=np.zeros(20);init[:4]=1/4
    obs=expm(z*t)@init
    mn=np.array([obs[4*n:4*n+4].sum() for n in range(5)])
    assert abs(mn[1])<1e-6 and abs(mn[3])<1e-5
    return mn[2],mn[4]-3*mn[2]**2

def main():
    aa,bb,hh,vx,vy,k,lam=sp.symbols('a b h vx vy k lam')
    Q=sp.zeros(4)
    for j in range(4):
        Q[j,j]=-(aa+bb+hh)
        Q[j,(j+1)%4]=aa
        Q[j,(j-1)%4]=bb
        Q[j,(j+2)%4]=hh
    m=aa+bb;ell=m+2*hh; omega=aa-bb
    q0=ell**2+omega**2
    charpol=sp.expand((lam*sp.eye(4)-Q-sp.diag(k*vx,k*vy,-k*vx,-k*vy)).det(method='domain-ge'))
    proposed=lam*(lam+2*m)*((lam+ell)**2+omega**2)-k*k*(vx**2+vy**2)*(lam+m)*(lam+ell)+k**4*vx**2*vy**2
    assert sp.cancel(charpol-proposed)==0
    eta=(vx**2+vy**2)*ell/(2*q0)
    beta=sp.factor(((vx**2+vy**2)*(m+ell)*eta-(q0+4*m*ell)*eta**2-vx**2*vy**2)/(2*m*q0))
    FF=ell*((2*m-ell)*ell**2-(ell+2*m)*omega**2)
    pred=-3*((vx**2+vy**2)**2*FF+4*vx**2*vy**2*q0**2)/(m*q0**3)
    assert sp.cancel(24*beta-pred)==0
    print('PASS: exact 4x4 characteristic polynomial and independent fourth-cumulant expansion')
    k2,k4=analytic(5,1,0,1,0)
    mm=sp.Integer(6); ll=sp.Integer(6); ww=sp.Integer(4)
    qq=ll**2+ww**2
    ff=ll*((2*mm-ll)*ll**2-(ll+2*mm)*ww**2)
    assert sp.cancel(-3*ff/(mm*qq**3)-sp.Rational(27,17576))==0
    assert sp.cancel(-3*(ff+qq**2)/(mm*qq**3)+sp.Rational(71,8788))==0
    assert abs(k4-float(sp.Rational(27,17576)))<1e-15
    assert abs(analytic(5,1,0,1,math.pi/4)[1]+float(sp.Rational(71,8788)))<1e-14
    print('PASS: rational example axial 27/17576 and diagonal -71/8788')
    for w,q in [(math.sqrt(7/20),0),(math.sqrt(7/20),1/8),(math.sqrt(7/20),1/2)]:
        a=(1+w)/2;b=(1-w)/2;h=q
        print('reentrant example q=',q,'axial K4/t=',analytic(a,b,h,1,0)[1])
    tests=[(5,1,0,1,0),(5,1,0,1,math.pi/4),(2,2,1,1,0),(0.2,2.8,.5,1,.22),(1.0,1.0,0.25,2,0.9)]
    for a,b,h,v,angle in tests:
        k2,k4=analytic(a,b,h,v,angle)
        t=160/max(1,a+b+h)
        m2,m4=finite_moments(a,b,h,v,angle,t)
        print('params',a,b,h,angle,'k2',k2,'finite k2/t',m2/t,'k4',k4,'finite k4/t',m4/t)
        assert abs(m2/t-k2) < max(.1*abs(k2),0.025)
        assert abs(m4/t-k4) < max(.4*abs(k4),.08)
    print('PASS: five independent large-time matrix-exponential moment-chain comparisons')

if __name__=='__main__': main()
