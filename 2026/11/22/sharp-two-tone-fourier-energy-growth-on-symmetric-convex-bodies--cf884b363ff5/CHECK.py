"""Supplementary deterministic checks for the two-tone convex-body growth theorem.

Uses only Python's standard library. These finite tests do not prove universal claims.
"""
import cmath
import math
import random


def sinc(x):
    return math.sin(x)/x if x else 1.0


def cube_phi(gap):
    return math.prod(sinc(t) for t in gap)


def diamond_phi(t):
    # Uniform probability on {(x,y): |x|+|y| <= 1}; projection to x.
    if abs(t) < 1e-4:
        return 1.0 - t*t/12.0 + t**4/360.0
    return 2.0*(1.0-math.cos(t))/(t*t)


def energy(r, dim, phi, alpha, beta, gap):
    base=abs(alpha)**2+abs(beta)**2
    cross=2.0*(alpha*beta.conjugate()).real
    return (2*r)**dim*(base+cross*phi(tuple(r*x for x in gap)))


def check():
    rng=random.Random(20261119)
    n=0
    for dim in (2,3,4,5):
        for _ in range(1400):
            gap=tuple(rng.uniform(-9.0,9.0) for j in range(dim))
            alpha=complex(rng.uniform(-2,2),rng.uniform(-2,2))
            beta=complex(rng.uniform(-2,2),rng.uniform(-2,2))
            r=rng.uniform(0.25,1.5)
            R=r*rng.uniform(1.05,4.0)
            e1=energy(r,dim,cube_phi,alpha,beta,gap)
            e2=energy(R,dim,cube_phi,alpha,beta,gap)
            assert e1>0 and e2/e1 <= (R/r)**(dim+2)*(1+2e-11)
            # Exact generalized-eigenvalue expression, including a fixed gap.
            phir=cube_phi(tuple(r*x for x in gap))
            phiR=cube_phi(tuple(R*x for x in gap))
            branches=[(1+phiR)/(1+phir),(1-phiR)/(1-phir)]
            bound=(R/r)**dim*max(branches)
            assert e2/e1 <= bound*(1+2e-11)
            sg=1 if branches[0]>=branches[1] else -1
            e1ext=energy(r,dim,cube_phi,1+0j,sg+0j,gap)
            e2ext=energy(R,dim,cube_phi,1+0j,sg+0j,gap)
            assert abs(e2ext/e1ext-bound) <= 3e-10*bound
            n+=3
    # A non-product convex body, the planar diamond.
    for j in range(1,750):
        t=j/45.0
        r=0.5;R=1.75
        for sg in (-1,1):
            a=r*r*(1+sg*diamond_phi(t*r))
            b=R*R*(1+sg*diamond_phi(t*R))
            assert a>0 and b/a<(R/r)**4*(1+2e-11)
            n+=1
    # Collision limit demonstrates optimality of exponent d+2.
    for dim in (2,3,4,5):
        r=0.8;R=2.1
        g1=(0.0005,)+(0.,)*(dim-1)
        q=energy(R,dim,cube_phi,1+0j,-1+0j,g1)/energy(r,dim,cube_phi,1+0j,-1+0j,g1)
        assert abs(q/(R/r)**(dim+2)-1)<2e-6
        n+=1
    # Directional fourth/second moment collision coefficient for cube and diamond.
    for dim,phi,m2,m4 in ((3, lambda t: sinc(t), 1/3, 1/5),
                          (2, diamond_phi, 1/6, 1/15)):
        r=0.65; R=1.8
        for eps in (0.02,0.03,0.04):
            obs=((R/r)**dim)*(1-phi(R*eps))/(1-phi(r*eps))
            normalized=obs/(R/r)**(dim+2)
            coefficient=(m4/(12*m2))*(R**2-r**2)
            assert abs((1-normalized)/eps**2-coefficient)<0.0004
            n+=1
    print('PASS:',n,'deterministic checks (cubes, diamond, eigenvalue extrema, collision)')

if __name__=='__main__':
    check()
