"""Independent reproducibility checks for spherical antiprism contact tails.
Requires Python 3, NumPy, and SciPy. All angles use radians.
"""
from math import acos, cos, sin, sqrt, pi, tan
import numpy as np
from scipy.integrate import quad
from scipy.spatial import ConvexHull


def parameters(n):
    c, s = cos(pi/n), sin(pi/n)
    a = 1/sqrt(1+c)
    h = sqrt(c/(1+c))
    return c,s,a,h


def sites(n, height=None):
    c,s,a,h=parameters(n)
    if height is not None:
        h=height
        a=sqrt(1-h*h)
    arr=[]
    for j in range(n):
        th=2*pi*j/n
        arr.append([a*cos(th),a*sin(th),h])
        th=(2*j+1)*pi/n
        arr.append([a*cos(th),a*sin(th),-h])
    return np.array(arr)


def half_width(t,z,p,a):
    rho=a*sqrt(max(0,1-z*z))
    x=t-p*z
    if rho<1e-15:
        return pi if x<=0 else 0.0
    x=x/rho
    if x>=1:return 0.
    if x<=-1:return pi
    return acos(x)


def uncovered_by_latitude(n,r,z,height=None):
    c,s,a,h=parameters(n)
    if height is not None:
        h=height
        a=sqrt(1-h*h)
    delta=pi/n
    t=cos(r)
    u=half_width(t,z,h,a)
    v=half_width(t,z,-h,a)
    return max(0.,1-(u+v)/delta)


def uncovered_by_longitude(n,r,z,numerical_points=50000,height=None):
    xx=np.arange(numerical_points)*2*pi/numerical_points
    q=sqrt(1-z*z)
    vs=sites(n,height)
    zz=np.array([q*np.cos(xx),q*np.sin(xx),np.full_like(xx,z)]).T
    m=(zz@vs.T).max(axis=1)
    return np.mean(m<cos(r))


def exact_ranged_uncovered(n,eps):
    c,s,a,h=parameters(n)
    t=h*cos(eps)+a*sin(eps)
    d=pi/n
    def endpoints(p,q):
        L=p*p+q*q
        assert t<sqrt(L)
        m=p*t/L
        w=q*sqrt(L-t*t)/L
        return (m-w,m+w)
    def lat_gap(th):
        lo_u,hi_u=endpoints(h,a*cos(th))
        lo_l,hi_l=endpoints(-h,a*cos(d-th))
        return (1-hi_u)+(1+lo_l)+max(0.,lo_u-hi_l)
    edge=min(d/3,15*eps)
    cuts=sorted(set([0.,edge,d-edge,d]))
    return n/(2*pi)*sum(quad(lat_gap,l,u,epsabs=1.e-13,epsrel=2.e-11,limit=400)[0]
                          for l,u in zip(cuts[:-1],cuts[1:]))


def K(n):
    c,s,_,_=parameters(n)
    return n*(1+c)/(pi*c*s)


def main():
    count=0
    # Check the putative regular antiprism geometry via independently
    # reconstructed 3D convex hulls and their supporting planes.
    for n in [3,4,5,6,8,10,14,20]:
        c,s,a,h=parameters(n)
        hull=ConvexHull(sites(n))
        distances=np.abs(hull.equations[:,-1]) / np.linalg.norm(hull.equations[:,:3],axis=1)
        assert len(hull.simplices)==4*n-4, (n,len(hull.simplices))
        assert np.allclose(distances,h,atol=5e-13), (n,distances)
        count+=2
        for eps in [.025,.01,.004,.0015]:
            v=exact_ranged_uncovered(n,eps)
            assert v>0
            assert abs(v/(K(n)*eps**2)-1) < max(.03,8*n*n*eps), (n,eps,v/(K(n)*eps**2))
            count+=2
        # Independent direct dot-product enumeration of cap membership
        # on horizontal circles, compared with the analytic interval law.
        for z in [-.93,-.58,-.29,0,.22,.61,.91]:
            for r in [.2,.45,acos(h)*.99]:
                analytic=uncovered_by_latitude(n,r,z)
                empirical=uncovered_by_longitude(n,r,z,18000)
                assert abs(analytic-empirical)<3*n/18000+1e-10,(n,z,r,analytic,empirical)
                count+=1
    # Unrestricted latitude, and apertures spanning and exceeding a hemisphere.
    # The independent test uses individual spherical dot products rather than
    # an approximation to the interval formula.
    for n in [3,5,8,12]:
        for h in [.2,.52,.79]:
            for z in [-.83,-.31,0.,.37,.87]:
                for r in [.3,.7,1.15,1.58,2.05]:
                    analytic=uncovered_by_latitude(n,r,z,h)
                    empirical=uncovered_by_longitude(n,r,z,18000,h)
                    assert abs(analytic-empirical)<3*n/18000+1e-10,(n,h,z,r,analytic,empirical)
                    count+=1
    # At six sites the formula reduces to the octahedral coefficient.
    assert abs(K(3)-6*sqrt(3)/pi)<1e-12
    count+=1
    # The square-antiprism special case reduces to an existing exact fact.
    assert abs(K(4)-(8+4*sqrt(2))/pi)<1e-12
    count+=1
    print(f'ANTIPRISM_TAIL_VERIFIED {count} assertions; sample coefficients:',
          [(n,round(K(n),8)) for n in [3,4,5,8,12]])

if __name__=='__main__':main()
