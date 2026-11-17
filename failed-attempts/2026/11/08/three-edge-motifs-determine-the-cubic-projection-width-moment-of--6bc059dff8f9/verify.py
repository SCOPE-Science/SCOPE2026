#!/usr/bin/env python3
"""Reproducible numerical diagnostics for graphical-zonotope third width moments.
Only Python standard-library modules are required. Finite tests are not a proof.
"""
from itertools import combinations
from math import pi, sqrt, asin, erf, exp, gamma, comb


def constants():
    mu=2/sqrt(pi)
    v=1/3+2*sqrt(3)/pi
    theta=asin(1/3)
    k0=8/sqrt(pi)-6*mu+2*mu**3
    k1=5/sqrt(pi)-mu*(2+2*v)+2*mu**3
    ks=(4*sqrt(2)+18*theta)/pi**1.5-3*mu*v+2*mu**3
    kp=(4*sqrt(2)+2*pi-6*theta)/pi**1.5-mu*(2*v+mu**2)+2*mu**3
    kt=3/sqrt(pi)-3*mu*v+2*mu**3
    return mu,v,k0,k1,ks,kp,kt


def motif_counts(n, edges):
    e=[tuple(sorted(x)) for x in edges]
    deg=[0]*n
    for a,b in e:deg[a]+=1;deg[b]+=1
    w2=sum(comb(k,2) for k in deg if k>=2)
    star=sum(comb(k,3) for k in deg if k>=3)
    triangles=sum(1 for a,b,c in combinations(range(n),3) if
                  (a,b) in e and (a,c) in e and (b,c) in e)
    paths=sum((deg[a]-1)*(deg[b]-1) for a,b in e)-3*triangles
    # Independent direct enumeration of all three-edge subsets.
    direct=[0,0,0]
    for triple in combinations(e,3):
        touched=set().union(*map(set,triple))
        if len(touched)==3: direct[2]+=1
        elif len(touched)==4:
            ds=[sum(v in edge for edge in triple) for v in touched]
            if max(ds)==3: direct[0]+=1
            elif sorted(ds)==[1,1,2,2]: direct[1]+=1
    assert direct == [star,paths,triangles],(n,e,direct,[star,paths,triangles])
    return len(e),w2,star,paths,triangles


def gaussian_moments(n, edges):
    m,w,star,path,tri=motif_counts(n,edges)
    mu,v,k0,k1,ks,kp,kt=constants()
    a1=m*mu
    a2=2*m+m*(m-1)*mu**2+2*w*(v-mu**2)
    k3=m*k0+6*w*k1+6*star*ks+6*path*kp+6*tri*kt
    a3=k3+3*a1*a2-2*a1**3
    return a1,a2,a3,k3,(m,w,star,path,tri)


def sph_cumulant(n,edges):
    a1,a2,a3,_,_=gaussian_moments(n,edges)
    d=n-1
    r=lambda k:2**(k/2)*gamma((d+k)/2)/gamma(d/2)
    q1,q2,q3=a1/r(1),a2/r(2),a3/r(3)
    return q3-3*q1*q2+2*q1**3, (q1,q2,q3)


def midpoint_integral(fn,a,b,count=30000):
    h=(b-a)/count
    return h*sum(fn(a+(j+.5)*h) for j in range(count))


def standalone_integrals():
    mu,v,k0,k1,ks,kp,kt=constants()
    phi=lambda z:exp(-z*z/2)/sqrt(2*pi)
    h=lambda z:2*phi(z)+z*erf(z/sqrt(2))
    q=lambda z:erf(z)/sqrt(pi)-phi(z)*erf(z/sqrt(2))
    s=midpoint_integral(lambda z:phi(z)*h(z)**3,-10,10)
    p=midpoint_integral(lambda z:4*(1/pi-q(z)**2),0,10)
    theta=asin(1/3)
    assert abs(s-(4*sqrt(2)+18*theta)/pi**1.5)<2e-8
    assert abs(p-(4*sqrt(2)+2*pi-6*theta)/pi**1.5)<2e-8
    # The triangle product equals (E r^3)/sqrt(2) times
    # (2/pi)*integral_0^1 |1-4*t*t| dt = 3/sqrt(pi).
    assert abs(3/sqrt(pi)-1.692568750643269)<1e-14
    assert ks>0 and kp<0 and kt<0
    assert kt-3*kp < -0.2


def graphs():
    k33=[(a,b) for a in range(3) for b in range(3,6)]
    prism=[(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)]
    return k33,prism


def main():
    standalone_integrals()
    for n in range(3,6):
        possibles=list(combinations(range(n),2))
        for mask in range(1,1<<len(possibles)):
            edges=[e for i,e in enumerate(possibles) if (mask>>i)&1]
            motif_counts(n,edges)
    k33,prism=graphs()
    _,moment_k= sph_cumulant(6,k33)
    _,moment_p= sph_cumulant(6,prism)
    assert abs(moment_k[0]-moment_p[0])<1e-10
    assert abs(moment_k[1]-moment_p[1])<1e-10
    kdiff=sph_cumulant(6,prism)[0]-sph_cumulant(6,k33)[0]
    assert -0.205<kdiff<-0.204
    assert gaussian_moments(6,k33)[-1]==(9,18,6,36,0)
    assert gaussian_moments(6,prism)[-1]==(9,18,6,30,2)
    print('GRAPHICAL_ZONOTOPE_THIRD_WIDTH_MOMENT_CHECKS_PASSED')
    print('Prism minus K33 spherical third cumulant:',round(kdiff,12))

if __name__=='__main__':main()
