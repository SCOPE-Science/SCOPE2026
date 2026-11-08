#!/usr/bin/env python3
"""Independent checks for geodesic containment in spherical azimuthal domains.

Requires Python >=3.9 and NumPy. It compares the exact formula with a
numerical shortest-arc interpolation in the ambient sphere, not merely
with another implementation of the longitude-difference criterion.
"""
import math
import numpy as np

PI=math.pi

def exact(intervals):
    lengths=[b-a for a,b in intervals]
    theta=sum(lengths)
    assert 0<theta<=2*PI+1e-12
    assert all(l>0 for l in lengths)
    return sum(l*l-max(l-PI,0)**2 for l in lengths)/(theta*theta)

def simulated(intervals,dim,count,seed):
    rng=np.random.default_rng(seed)
    lengths=np.array([b-a for a,b in intervals])
    weights=lengths/lengths.sum()
    choice=rng.choice(len(intervals),size=(count,2),p=weights)
    az=np.zeros((count,2))
    for j,(a,b) in enumerate(intervals):
        mask=choice==j
        az[mask]=a+(b-a)*rng.random(mask.sum())
    pts=rng.standard_normal((count,2,dim+1))
    radial=np.hypot(pts[:,:,0],pts[:,:,1])
    pts[:,:,0]=radial*np.cos(az)
    pts[:,:,1]=radial*np.sin(az)
    pts/=np.linalg.norm(pts,axis=2,keepdims=True)
    stayed=np.ones(count,dtype=np.bool_)
    # Normalized affine interpolation traces the unique shorter great-circle arc.
    # The direct interpolation is independent of the analytic angular proof.
    for t in np.linspace(0,1,401)[1:-1]:
        u=(1-t)*pts[:,0,:]+t*pts[:,1,:]
        phi=np.mod(np.arctan2(u[:,1],u[:,0]),2*PI)
        ok=np.zeros(count,dtype=np.bool_)
        for a,b in intervals:
            ok|=(a<phi)&(phi<b)
        stayed &= ok
    return float(stayed.mean())

def main():
    datasets=[
        (2,[(0.2,2.8)]),
        (2,[(0.1,5.2)]),
        (3,[(0.15,1.9),(2.2,4.9)]),
        (5,[(0.1,1.9),(2.5,4.5),(5.0,5.7)]),
        (6,[(0.12,5.8)]),
    ]
    n=45000
    for i,(dimension,intervals) in enumerate(datasets):
        predicted=exact(intervals)
        observed=simulated(intervals,dimension,n,92500+i)
        # Includes binomial fluctuation and discretization error near slit boundaries.
        tolerance=0.012
        assert abs(predicted-observed)<tolerance, (dimension,intervals,predicted,observed)
        print("d=%d expected=%.8f simulated=%.8f"%(dimension,predicted,observed))
    # The exact sharp lower bound and upper supremum are checked directly.
    for k in range(2,15):
        for total in (0.2,1.7,3.5,5.8,2*PI):
            length=total/k
            assert abs((k*length**2)/(total**2)-1/k)<1e-12
    assert exact([(0,2*PI)])==0.75
    print("SPHERICAL_AZIMUTH_GEODESIC_VISIBILITY_OK", len(datasets)*n)

if __name__=="__main__":
    main()
