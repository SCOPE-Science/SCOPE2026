"""Independent numerical checks of shortfalls in the annular geodesic/chord ratio."""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq

PI=math.pi

def dist_geo(rho,sigma,angle,r):
    a=math.acos(min(1.,r/rho)); b=math.acos(min(1.,r/sigma))
    chord=math.sqrt((rho-sigma)**2+4*rho*sigma*math.sin(angle/2)**2)
    if angle <= a+b:
        return chord
    return math.sqrt(rho*rho-r*r)-r*a + math.sqrt(sigma*sigma-r*r)-r*b +r*angle

def stretch(u,v,eta):
    # Inner radius normalized to 1, eta=pi-angle.
    A=1+u; B=1+v; angle=PI-eta
    return dist_geo(A,B,angle,1)/math.sqrt((A-B)**2+4*A*B*math.sin(angle/2)**2)

def threshold(eps,u,v):
    if PI/2-stretch(u,v,0)>=eps:
        return 0.
    return brentq(lambda eta:PI/2-stretch(u,v,eta)-eps,0,min(PI,5*eps),xtol=1e-14)

def cutoff_u(eps, u0=0):
    return brentq(lambda u:PI/2-stretch(u,u0,0)-eps,0,10*eps,xtol=1e-14)

def numeric_tail(eps,r,R,N=32):
    assert 0<r<R and eps<0.05
    K=R*R-r*r
    x,w=leggauss(N)
    top=cutoff_u(eps)
    val=0.
    # nested integration with exact smooth threshold geometry
    for xi,wi in zip(x,w):
        u=top*(xi+1)/2
        vmax=cutoff_u(eps,u)
        inner=0.
        for xj,wj in zip(x,w):
            v=vmax*(xj+1)/2
            inner+=wj*(1+u)*(1+v)*threshold(eps,u,v)
        val+=wi*inner*vmax/2
    return 4*r**4/(PI*K*K)*val*top/2

def C(r,R):
    return 64*r**4/(3*PI**3*(R*R-r*r)**2)

def main():
    tests=[]
    for (r,R) in [(0.5,1.),(0.8,1.),(1.,2.)]:
        for eps in [0.02,0.008,0.003]:
            p=numeric_tail(eps,r,R)
            ratio=p/(C(r,R)*eps**3)
            tests.append((r,R,eps,p,ratio))
            print(f'r={r:.2f} R={R:.2f} eps={eps:.3g} prob={p:.11g} normalized={ratio:.7f}')
            assert 0.80 < ratio < 1.4
    assert all(abs(t[4]-1)<0.08 for t in tests if t[2]==0.003)
    for u,v,eta in [(0,0,0),(0.001,0.002,0.002),(0.0004,0.0008,0.001)]:
        deficit=PI/2-stretch(u,v,eta)
        linear=PI/4*(u+v)+eta/2
        assert abs(deficit-linear)<0.005
    rng=np.random.default_rng(41)
    # Direct finite check of global dilation bound over both geodesic regimes.
    for _ in range(20000):
        rho=1+3*rng.random(); sigma=1+3*rng.random(); ang=PI*rng.random()
        chord=math.sqrt((rho-sigma)**2+4*rho*sigma*math.sin(ang/2)**2)
        assert dist_geo(rho,sigma,ang,1)/chord <= PI/2+2e-13
    # Distortion-tail coefficient identifies the inner/outer radius ratio.
    for ratio in [0.02, 0.1, 0.4, 0.7, 0.99]:
        coeff=C(ratio,1)
        T=math.sqrt(3*PI**3*coeff/64)
        recovered=math.sqrt(T/(1+T))
        assert abs(recovered-ratio)<1e-13
    print('ANNULUS_STRETCH_TAIL_CHECKS_OK',len(tests)+3+20000+5)

if __name__=='__main__':main()
