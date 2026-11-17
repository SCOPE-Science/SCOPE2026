"""Reproduce the circular three-point Euclidean MST endpoint diagnostics.
Run: python verify_mst.py (requires numpy and scipy).
All random draws are reproducibly seeded; the proof is analytical, not simulation-based.
"""
import math
import numpy as np
from scipy.optimize import brentq

PI=math.pi
C2=9/PI**2
C3=-18*math.sqrt(3)/PI**2


def local_cross_section(t, u):
    """Exact radial cutoff for the near-equilateral wedge (small t)."""
    def deficit(r):
        return 2*math.sqrt(3)-4*math.sin(PI/3-r/4)*math.cos(3*r*u/4)
    return brentq(lambda r: deficit(r)-t, 0.0, max(0.2,4*t), xtol=1e-14)


def exact_local_cdf(t, order=96):
    u,weight=np.polynomial.legendre.leggauss(order)
    rr=np.array([local_cross_section(t,float(v)) for v in u])
    return (9/(8*PI**2))*np.dot(weight,rr**2)


def direct_sample(t, count=2_400_000, seed=20261110):
    rng=np.random.default_rng(seed)
    ne=0; sR=0.; sU=0.; sU2=0.; probs=[]
    for start in range(0,count,200_000):
        k=min(200_000,count-start)
        th=rng.uniform(0,2*PI,(k,3))
        rel=np.mod(th[:,1:]-th[:,0,None],2*PI)
        rel.sort(axis=1)
        gaps=np.column_stack([rel[:,0],rel[:,1]-rel[:,0],2*PI-rel[:,1]])
        sides=2*np.sin(gaps/2)
        mst=np.sum(sides,axis=1)-np.max(sides,axis=1)
        mask=(mst>2*math.sqrt(3)-t)
        idx=np.flatnonzero(mask)
        ne+=len(idx)
        if len(idx):
            dev=gaps[idx]-2*PI/3
            m=np.argmax(dev,axis=1)
            r=dev[np.arange(len(idx)),m]
            z=dev[np.arange(len(idx)),(m+1)%3]-dev[np.arange(len(idx)),(m+2)%3]
            uu=z/(3*r)
            sR+=np.sum(r/(2*t))
            sU+=np.sum(uu)
            sU2+=np.sum(uu**2)
    p=ne/count
    sig=math.sqrt(p*(1-p)/count)
    return p,sig,ne,sR/ne,sU/ne,sU2/ne


def main():
    print('coefficients',format(C2,'.14f'),format(C3,'.14f'))
    prev=[]
    for t in [0.04,0.02,0.01,0.005,0.002]:
        exact=exact_local_cdf(t)
        leading=C2*t**2
        two=leading+C3*t**3
        corr=(exact-leading)/t**3
        residual=(exact-two)/t**4
        prev.append((t,exact,leading,two,corr,residual))
        print(f't={t:g} exact={exact:.14g} leading_ratio={exact/leading:.9f} cubic_coeff={corr:.9f} residual/t4={residual:.8f}')
        assert abs(exact-two)<25*t**4
    # independent finite-element quadrature using a rectangular grid in gap simplex
    # near-max tail agrees with wedge-based integral; this tests factor 3 and Jacobian.
    t=.04
    N=1800
    a=np.arange(N)[:,None];b=np.arange(N)[None,:]
    delta1=-.17+(.34/N)*(a+.5)
    delta2=-.17+(.34/N)*(b+.5)
    delta3=-delta1-delta2
    good=(np.abs(delta3)<.17)
    sides=np.stack([np.broadcast_to(2*np.sin(PI/3+delta1/2),(N,N)),
                    np.broadcast_to(2*np.sin(PI/3+delta2/2),(N,N)),
                    2*np.sin(PI/3+delta3/2)])
    val=sides.sum(axis=0)-np.max(sides,axis=0)
    grid=((val>2*math.sqrt(3)-t)&good).sum()*(.34/N)**2/(2*PI**2)
    e=exact_local_cdf(t)
    print('independent rectangular-gap quadrature',grid,'wedge integral',e,'relative error',abs(grid/e-1))
    assert abs(grid/e-1)<.012
    p,se,n,R,U,U2=direct_sample(.08)
    expected=exact_local_cdf(.08)
    print(f'independent iid-circle simulation: successes={n}, p={p:.8f}, exact={expected:.8f}, sigma={se:.8f}')
    print('conditional R, U, U^2 means',R,U,U2,'limits 2/3, 0, 1/3')
    assert abs(p-expected)<5.5*se
    assert abs(R-2/3)<.07 and abs(U)<.04 and abs(U2-1/3)<.05
    print('CIRCLE_THREE_POINT_MST_TWO_TERM_AND_MARKED_LAW_OK')

if __name__=='__main__':
    main()
