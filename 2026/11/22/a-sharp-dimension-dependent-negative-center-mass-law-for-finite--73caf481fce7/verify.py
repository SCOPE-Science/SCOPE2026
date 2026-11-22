#!/usr/bin/env python3
"""Independent finite verification of spherical-origin Euclidean distance energies.

All numerical cases are finite illustrations; the all-configuration theorem
is established by the analytic proof accompanying this program.
"""
from math import cos, sin, pi, sqrt, gamma, isclose
from itertools import product


def norm(a):
    return sqrt(sum(v*v for v in a))


def dist(a, b):
    return norm([u-v for u,v in zip(a,b)])


def gauging(points):
    # Gaussian elimination with partial pivoting for D p = c 1 and sum p = 1.
    n=len(points)
    a=[[dist(points[i],points[j]) for j in range(n)]+[-1.0, 0.0] for i in range(n)]
    a.append([1.0]*n+[0.0,1.0])
    for i in range(n+1):
        k=max(range(i,n+1),key=lambda j:abs(a[j][i]))
        if abs(a[k][i])<1e-12:
            raise AssertionError('singular gauging system')
        a[k],a[i]=a[i],a[k]
        v=a[i][i]
        for j in range(i,n+2): a[i][j]/=v
        for k in range(n+1):
            if k==i:continue
            v=a[k][i]
            for j in range(i,n+2): a[k][j]-=v*a[i][j]
    return [a[i][-1] for i in range(n)],a[n][-1]


def run_case(v):
    d=len(v[0]); r=norm(v[0]); assert all(abs(norm(x)-r)<1e-8 for x in v)
    w,c=gauging(v)
    aug=[tuple(0.0 for _ in range(d))]+v
    q,C=gauging(aug)
    predicted=(r-c)/(2*r-c)
    assert abs(q[0]-predicted)<5e-8,(q[0],predicted)
    assert max(abs(q[i+1]-r*w[i]/(2*r-c)) for i in range(len(v)))<5e-8
    Cd=2**(d-1)*gamma(d/2)**2/(sqrt(pi)*gamma(d-0.5))
    assert r<c<Cd*r,(r,c,Cd)
    assert (1-Cd)/(2-Cd)<q[0]<0
    # Potentials equal at every augmented site, including the center.
    for i in range(len(aug)):
        pot=sum(dist(aug[i],aug[j])*q[j] for j in range(len(aug)))
        assert abs(pot-C)<1e-7
    return c/r,q[0]


def main():
    cases=0
    for n in range(3,26):
        poly=[(cos(2*pi*j/n),sin(2*pi*j/n)) for j in range(n)]
        run_case(poly);cases+=1
    for d in range(2,8):
        xp=[]
        for i in range(d):
            e=[0.0]*d;e[i]=1.;xp.append(tuple(e))
            e=[0.0]*d;e[i]=-1.;xp.append(tuple(e))
        run_case(xp);cases+=1
    for d in (2,3,5):
        for eps in (0.02,0.05,0.15,0.3,0.7):
            u=[1.0]+[0.0]*(d-1)
            v=[cos(eps),sin(eps)]+[0.0]*(d-2)
            run_case([tuple(u),tuple(-t for t in u),tuple(v),tuple(-t for t in v)])
            cases+=1
    # Non-transitive non-antipodal spanning clouds with 0 in hull:
    # convexly include a regular (d+1)-vertex simplex and adjoin extra sites.
    for d in (2,3):
        if d==2:
            base=[(cos(2*pi*j/3),sin(2*pi*j/3)) for j in range(3)]
            for angle in (0.19,0.37,0.71,1.23):
                run_case(base+[(cos(angle),sin(angle))]);cases+=1
        else:
            base=[(1.,0.,0.),(-1.,0.,0.),(0.,1.,0.),(0.,-1.,0.),(0.,0.,1.),(0.,0.,-1.)]
            for angle in (0.11,0.29,0.63,1.02):
                run_case(base+[(cos(angle),sin(angle),0.)]);cases+=1
    print('PASS:',cases,'finite geometric gauging cases; max residual <1e-7')
    for d in (2,3,4,8,24,100):
        # log gamma for overflow avoidance
        from math import lgamma,exp,log
        Cd=exp((d-1)*log(2)+2*lgamma(d/2)-lgamma(d-0.5)-0.5*log(pi))
        print('d=',d,'C_d=',format(Cd,'.12f'),'sharp negative mass lower=',format((1-Cd)/(2-Cd),'.12f'))

if __name__=='__main__':
    main()
