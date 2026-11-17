"""Reproduce elementary and numerical checks for the two-site rectangle law.
Run: python check.py (requires NumPy).
"""
import math
from fractions import Fraction
import numpy as np


def area_by_clipping(x, y, side1, side2):
    # Independent polygon-halfplane construction of the Voronoi region.
    vertices = [(-side1/2,-side2/2), (side1/2,-side2/2),
                (side1/2,side2/2), (-side1/2,side2/2)]
    w = y - x
    m = (x + y) / 2
    h = float(np.dot(w, m))
    def f(z):
        return float(np.dot(w,z)) - h
    out=[]
    for a,b in zip(vertices, vertices[1:]+vertices[:1]):
        fa,fb=f(a),f(b)
        if fa<=0:
            out.append(a)
        if (fa<0<fb) or (fb<0<fa):
            z=fa/(fa-fb)
            out.append((a[0]+z*(b[0]-a[0]),a[1]+z*(b[1]-a[1])))
    if not out:
        return 0.0
    area=0.5*abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(out,out[1:]+out[:1])))
    return min(area,side1*side2-area)


def smaller_area(x,y,Lx,Ly):
    w=y-x
    p=np.abs(w[...,0]);q=np.abs(w[...,1]);
    h=np.abs(np.sum(((x+y)/2)*w,axis=-1))
    z=(p*Lx+q*Ly)/2-h
    # Truncated-corner integral, valid for every bisector orientation.
    cap=(np.maximum(z,0)**2-np.maximum(z-p*Lx,0)**2
         -np.maximum(z-q*Ly,0)**2+np.maximum(z-p*Lx-q*Ly,0)**2)/(2*p*q)
    return np.minimum(cap,Lx*Ly-cap)


def simulation(Lx,Ly,n,threshold,seed):
    rng=np.random.default_rng(seed)
    hits=0; samples=[]
    for k in range((n+199999)//200000):
        size=min(200000,n-k*200000)
        x=(rng.random((size,2))-.5)*[Lx,Ly]
        y=(rng.random((size,2))-.5)*[Lx,Ly]
        area=smaller_area(x,y,Lx,Ly)
        mask=area<threshold*Lx*Ly
        hits+=int(mask.sum())
        if Lx==Ly and mask.any():
            a=x[mask];b=y[mask];w=b-a
            h=np.sum((a+b)*w/2,axis=1)
            corner=np.sign(w)*np.sign(h)[:,None]
            deficits=[Lx/2,Ly/2]-(a+b)*corner/2
            aa,bb=deficits[:,0],deficits[:,1]
            p,q=np.abs(w[:,0])/2,np.abs(w[:,1])/2
            Xi=aa*p/(aa*p+bb*q)
            Lambda=np.sqrt(bb*p/(aa*q))
            J=np.maximum(p/aa,q/bb)**2
            samples.append(np.stack((area[mask]/(threshold*Lx*Ly), Xi,
                                     np.log(Lambda),J),axis=1))
    return hits,np.concatenate(samples) if samples else None


def main():
    # Integral identity: int_{A+B<c} A B / 2 dA dB = c^4/48.
    # Eight symmetry cases; Jacobian 4; density 1/S^2; c^4=4 t^2.
    assert Fraction(8*4,1)*Fraction(4,48)==Fraction(8,3)
    rng=np.random.default_rng(20261112)
    for lx,ly in [(2.,2.),(4.,1.)]:
        for _ in range(150):
            x=(rng.random(2)-.5)*[lx,ly]
            y=(rng.random(2)-.5)*[lx,ly]
            one=float(smaller_area(x,y,lx,ly))
            other=area_by_clipping(x,y,lx,ly)
            assert abs(one-other)<5e-12,(one,other)
    print('Independent polygon clipping: 300/300 verified')
    for lx,ly,seed in [(2.,2.,1001),(4.,1.,1002)]:
        eps=.025
        N=2_000_000
        hits,marks=simulation(lx,ly,N,eps,seed)
        predicted=(8/3)*eps**2
        observed=hits/N
        relative_se=math.sqrt(max(1,hits))/N/predicted
        # Finite-threshold bias is nonzero, especially for elongated rectangles.
        assert abs(observed/predicted-1)<max(.13,6*relative_se)
        print('Rectangle',lx,ly,'N',N,'hits',hits,
              'P',round(observed,9),'leading',round(predicted,9),
              'ratio',round(observed/predicted,5))
        if marks is not None:
            # Target: Beta(2,1), Beta(2,2), Laplace(scale=1/2), Uniform(0,1).
            means=[marks[:,0].mean(),marks[:,1].mean(),
                   (marks[:,2]<0).mean(),marks[:,3].mean()]
            target=[2/3,.5,.5,.5]
            assert max(abs(x-y) for x,y in zip(means,target))<.07,means
            print('Conditional means/medians proxies',np.round(means,4))
    print('RECTANGLE_TWO_SITE_CHECKS_OK')


if __name__=='__main__': main()
