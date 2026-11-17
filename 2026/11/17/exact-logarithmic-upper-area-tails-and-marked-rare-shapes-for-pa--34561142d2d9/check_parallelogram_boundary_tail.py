"""Independent diagnostics: near-maximal area of three boundary-random points
on a parallelogram. Uses numpy and scipy, with no external data files.
"""
import math
import numpy as np
from scipy.integrate import quad


def component_distinct(e):
    # Exact probability that x(1-y)+y z<e for independent U(0,1) x,y,z.
    return (1-2*e)*math.log1p(-e) + e + e*e*math.log((1-e)/e)

def component_adjacent(e):
    # P(|X_1-X_2|Y>1-e), all variables independent U(0,1).
    return -e*e+2*e+2*(1-e)*math.log1p(-e)

def formula(e, a, b):
    assert 0<e<.5 and a>0 and b>0
    u=a/(2*(a+b)); v=b/(2*(a+b))
    return 6*u*v*(component_distinct(e)+component_adjacent(e)) + 6*(u**3+v**3)*e*e

def independent_integral(e,a,b):
    u=a/(2*(a+b));v=b/(2*(a+b))
    def area_at_y(y):
        h=max(y,1-y); lo=min(y,1-y)
        if lo<e: return (e-lo/2)/h
        return e*e/(2*y*(1-y))
    f=2*quad(area_at_y,0,e,epsabs=1e-13)[0]+quad(area_at_y,e,1-e,epsabs=1e-13)[0]
    j=quad(lambda d:2*(1-d)*(1-(1-e)/d),1-e,1,epsabs=1e-13)[0]
    return 6*u*v*(f+j)+6*(u**3+v**3)*e*e

def direct_simulation(e,a,b,angle,n=1_600_000,seed=723):
    rng=np.random.default_rng(seed)
    # Four oriented sides in coordinates (s,t) on a unit square.
    weights=np.array([a,b,a,b],float)/(2*(a+b))
    cdf=weights.cumsum()
    hits=0
    for st in range(0,n,200_000):
        batch=min(200_000,n-st)
        side=np.searchsorted(cdf,rng.random((batch,3)))
        along=rng.random((batch,3))
        s=np.select([side==0,side==1,side==2,side==3],
                    [along,np.ones_like(along),1-along,np.zeros_like(along)])
        t=np.select([side==0,side==1,side==2,side==3],
                    [np.zeros_like(along),along,np.ones_like(along),1-along])
        # Affine map, explicitly sample Euclidean parallelogram and divide its area.
        xx=a*s+b*math.cos(angle)*t
        yy=b*math.sin(angle)*t
        area=np.abs((xx[:,1]-xx[:,0])*(yy[:,2]-yy[:,0])
                    -(xx[:,2]-xx[:,0])*(yy[:,1]-yy[:,0]))/2
        hits+=np.count_nonzero(area > a*b*math.sin(angle)*(1-e)/2)
    return hits/n

def run():
    for a,b,angle in [(1,1,math.pi/2),(2,1,math.pi/3),(5,1,math.pi*0.37)]:
        for e in [0.12,0.07,0.028]:
            exact=formula(e,a,b)
            q=independent_integral(e,a,b)
            assert abs(q-exact)<2e-12, (a,b,e,exact,q)
            print('aspect',a,b,'eps',e,'formula',f'{exact:.12g}','quadrature',f'{q:.12g}')
        e=.07
        sample=direct_simulation(e,a,b,angle)
        p=formula(e,a,b)
        sigma=math.sqrt(p*(1-p)/1_600_000)
        print('direct',a,b,'estimate',sample,'target',p,'zscore',(sample-p)/sigma)
        assert abs(sample-p)<5*sigma
    # Verified exact lower-tail expansion in e for a=b and a=5b:
    for a,b in [(1,1),(5,1)]:
        u=a/(2*(a+b));v=b/(2*(a+b))
        e=.0005
        two_term=(6*u*v)*e*e*math.log(1/e)+(9*u*v+6*(u**3+v**3))*e*e
        # Error exactly of order e^4, with an especially small coefficient.
        assert abs(formula(e,a,b)-two_term)<e**4
    print('PARALLELOGRAM_BOUNDARY_LOG_TAIL_AND_DIRICHLET_MARK_OK')

if __name__=='__main__':run()
