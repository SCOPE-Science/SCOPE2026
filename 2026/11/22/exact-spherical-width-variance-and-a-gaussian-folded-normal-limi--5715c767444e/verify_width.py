"""Independent computational spot checks for cube-plus-diagonal zonotope widths.

Requires Python >=3.10 and numpy. Run: python verify_width.py.
Analytic limit theorems and the spherical moment identities are proved in RESULT.md;
finite tests are not substitutes for those arguments.
"""
import math
from itertools import product
import numpy as np

PI=math.pi
MU=math.sqrt(2/PI)


def c(d):
    return math.exp(math.lgamma(d/2)-math.lgamma((d+1)/2))/math.sqrt(PI)


def k(rho):
    return (2/PI)*(math.sqrt(1-rho*rho)+rho*math.asin(rho))


def moments(d,b,a):
    cd=c(d)
    mean=cd*(b*d+a*math.sqrt(d))
    vbox=1+2*(d-1)/PI-(d*cd)**2
    vdiag=1-d*cd**2
    cross=math.sqrt(d)*(k(1/math.sqrt(d))-d*cd**2)
    return mean,b*b*vbox+a*a*vdiag+2*a*b*cross


def width_support(u,b,a):
    return b*np.abs(u).sum()+a*abs(u.sum())


def exhaustive_corner_width(u,b,a):
    d=len(u)
    values=[]
    for signs in product((-1,1),repeat=d+1):
        v=(b/2)*np.array(signs[:d])+a/2*signs[-1]
        values.append(float(u@v))
    return max(values)-min(values)


def main():
    rng=np.random.default_rng(5173)
    nchecked=0
    for d in range(2,8):
        for b,a in ((1.0,0.4),(1.7,2.1)):
            for _ in range(20):
                x=rng.standard_normal(d)
                u=x/np.linalg.norm(x)
                direct=exhaustive_corner_width(u,b,a)
                closed=width_support(u,b,a)
                assert abs(direct-closed)<5e-12,(d,b,a,direct,closed)
                nchecked+=1
    # Independent deterministic circle integration (d=2): no distributional sampling.
    theta=(np.arange(65536)+0.5)*(2*PI/65536)
    u=np.stack([np.cos(theta),np.sin(theta)],axis=1)
    for b,a in ((1,0.3),(2,1.5)):
        widths=b*np.abs(u).sum(axis=1)+a*np.abs(u.sum(axis=1))
        theo_mean,theo_var=moments(2,b,a)
        assert abs(widths.mean()-theo_mean)<3e-8
        assert abs(widths.var()-theo_var)<3e-8
    # Distinct spherical sampling mechanism: independent normalized Gaussian samples.
    for d in (8,64,256):
        n=60000
        g=rng.standard_normal((n,d))
        u=g/np.linalg.norm(g,axis=1)[:,None]
        widths=np.abs(u).sum(axis=1)+0.7*np.abs(u.sum(axis=1))
        mean,var=moments(d,1,0.7)
        assert abs(float(np.mean(widths))-mean)<0.035,(d,'mean',float(np.mean(widths)),mean)
        assert abs(float(np.var(widths))-var)<0.035,(d,'var',float(np.var(widths)),var)
    lim=1-3/PI+0.7**2*(1-2/PI)
    assert abs(moments(20000,1,0.7)[1]-lim)<0.0002
    print('ISOCANTED_ANGULAR_WIDTH_EXACT_PASS corners=',nchecked,' circle_moments=2 sphere_samples=3')


if __name__=='__main__':
    main()
