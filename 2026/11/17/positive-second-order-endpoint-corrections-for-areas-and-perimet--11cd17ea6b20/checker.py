"""Reproducible diagnostics for the near-regular random cyclic polygon perimeter law."""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import gamma


def constants(n,observable="perimeter"):
    t=math.pi/n if observable=="perimeter" else 2*math.pi/n
    fac=1 if observable=="perimeter" else 4
    a=math.sin(t); c=math.cos(t); d=n-1
    leading=math.factorial(d)/(math.sqrt(n)*gamma((n+1)/2)*(math.pi*a)**(d/2))
    correction=(d*(n-2)*c*c/(12*n*(n+1)*a**3)
                +d*d/(8*n*(n+1)*a))
    return leading,fac*correction


def sphere_points(n):
    if n==3:
        theta=2*math.pi*np.arange(8192)/8192
        orth=np.stack([np.cos(theta),np.sin(theta)],axis=1)
        weights=np.full(len(theta),1/len(theta))
    elif n==4:
        z,w=leggauss(84)
        theta=2*math.pi*np.arange(192)/192
        xx=np.sqrt(1-z[:,None]**2)*np.cos(theta)[None,:]
        yy=np.sqrt(1-z[:,None]**2)*np.sin(theta)[None,:]
        zz=np.broadcast_to(z[:,None],xx.shape)
        orth=np.stack([xx,yy,zz],axis=-1).reshape(-1,3)
        weights=np.repeat(w/2/192,192)
    else:
        raise ValueError('only n=3 and 4')
    B=np.stack([np.eye(n)[:,i]-np.eye(n)[:,-1] for i in range(n-1)],axis=1)
    Q,_=np.linalg.qr(B)
    return orth@Q.T,weights


def exact_probability(n,eps,observable="perimeter"):
    points,weights=sphere_points(n)
    t=math.pi/n if observable=="perimeter" else 2*math.pi/n
    low=np.zeros(len(points))
    high=np.full(len(points),2.0)
    def deficit(r):
        y=t+points*r[:,None]/(2 if observable=="perimeter" else 1)
        return (2 if observable=="perimeter" else .5)*(n*math.sin(t)-np.sin(y).sum(axis=1))
    if np.any(deficit(high)<eps):
        raise RuntimeError('radius bracket inadequate')
    for _ in range(48):
        mid=(low+high)/2
        f=deficit(mid)
        high=np.where(f>=eps,mid,high)
        low=np.where(f<eps,mid,low)
    radii=(low+high)/2
    d=n-1
    omega=2*math.pi**(d/2)/gamma(d/2)
    density=math.factorial(d)/(2*math.pi)**d
    return density/math.sqrt(n)*omega/d*np.dot(weights,radii**d)


def check(n,eps_list,observable="perimeter"):
    C,B=constants(n,observable)
    print(f'observable={observable} n={n} C={C:.12g} B={B:.12g}')
    ratios=[]
    for eps in eps_list:
        exact=exact_probability(n,eps,observable)
        approx=C*eps**((n-1)/2)*(1+B*eps)
        ratio=exact/approx
        print(f' eps={eps:.4g} numerical={exact:.12g} two_term={approx:.12g} ratio={ratio:.12g}')
        ratios.append(abs(ratio-1))
        assert abs(ratio-1)<0.002
    assert ratios[-1]<ratios[0]


if __name__=='__main__':
    check(3,[0.15,0.06,0.015])
    check(4,[0.12,0.06,0.02])
    check(3,[0.09,0.04,0.01],"area")
    check(4,[0.09,0.04,0.01],"area")
    print('FIXED_N_POLYGON_AREA_PERIMETER_SECOND_ORDER_CHECK_OK')
