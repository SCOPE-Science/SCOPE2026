"""Supplementary numerical checks for spatially heterogeneous crop-salinity response.

This code checks examples but does not constitute a proof of the infinite-domain statement.
"""
import math
import random


def area_response(values, weights, p, scale):
    mean = sum(x*w for x,w in zip(values,weights))
    return (sum(w/(1+(scale*x)**p) for x,w in zip(values,weights))
            - 1/(1+(scale*mean)**p))


def symmetric_threshold(mean, delta):
    assert 0 < delta < mean
    return (3*mean/(6*mean**4-3*mean**2*delta**2+delta**4))**(1/3)


def main():
    rng = random.Random(904182)
    checks=0
    for _ in range(1000):
        size = rng.randint(2, 12)
        vals = [10**rng.uniform(-1,1) for i in range(size)]
        raw = [rng.uniform(.1,2) for i in range(size)]
        ws = [x/sum(raw) for x in raw]
        mu = sum(x*w for x,w in zip(vals,ws))
        if max(vals)-min(vals)<1e-9:continue
        for p in (.4, .7, 1.):
            for k in (.01,.1,.5,1,2,4,10,100):
                d=area_response(vals,ws,p,k/mu)
                assert d > -5e-12, (vals,p,k,d)
                checks +=1
        for p in (1.1,1.5,2.,3.,5.):
            low = min(vals); high=max(vals)
            bend=((p-1)/(p+1))**(1/p)
            dlo=area_response(vals,ws,p,.8*bend/high)
            dhi=area_response(vals,ws,p,1.2*bend/low)
            assert dlo < 1e-13 and dhi > -1e-13, (p,dlo,dhi)
            checks+=2
            # Bisect only after analytic bracketing; no inference of uniqueness from grid.
            lo=.8*bend/high;hi=1.2*bend/low
            for i in range(55):
                mid=(lo+hi)/2
                dm=area_response(vals,ws,p,mid)
                if dm<0:lo=mid
                else:hi=mid
            # strong margin avoids roundoff near root
            root=(lo+hi)/2
            assert area_response(vals,ws,p,.9*root) < 1e-11
            assert area_response(vals,ws,p,1.1*root) > -1e-11
            checks+=2
    for _ in range(4000):
        mu=10**rng.uniform(-1,2)
        ratio=rng.uniform(.001,.999)
        d=mu*ratio
        rt=symmetric_threshold(mu,d)
        assert (1/2)**(1/3) < rt*mu < (3/4)**(1/3)
        assert area_response([mu-d,mu+d],[.5,.5],3,.85*rt)<0
        assert area_response([mu-d,mu+d],[.5,.5],3,1.15*rt)>0
        checks+=3
    # External numeric example, with dimensionful salinity values 5,15 and half-yield 12.
    mu,d,c50=10.,5.,12.
    lam=c50*symmetric_threshold(mu,d)
    assert abs(lam - 0.9918713591323858)<1e-12
    for factor, expected in [(.7,-1),(1.,0),(1.3,1)]:
        dd=area_response([mu-d,mu+d],[.5,.5],3,factor*lam/c50)
        assert abs(dd)<2e-14 if expected==0 else dd*expected>0
        checks+=1
    print(f'PASS: {checks} supplementary numerical assertions; no exhaustive or formal certification')

if __name__ == '__main__':main()
