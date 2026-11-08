"""Numerical consistency checks of the prism width/brightness covariance theorem.

Python 3 standard library only. Monte Carlo is corroboration, not proof.
"""
from math import pi, sin, cos, sqrt
from random import Random

K = pi / 8 - 1 / 3

def polygon_area(P):
    return abs(sum(x*y1-y*x1 for (x,y),(x1,y1) in zip(P,P[1:]+P[:1]))) / 2

def widths(P,th):
    a,b=cos(th),sin(th)
    q=[a*x+b*y for x,y in P]
    return max(q)-min(q)

def invariants(P,steps=12000):
    A=polygon_area(P)
    w=[widths(P,2*pi*i/steps) for i in range(steps)]
    beta=sum(w)/steps
    c=sum(w[i]*w[(i+steps//4)%steps] for i in range(steps))/steps
    return A,beta,c

def cov_formula(A,beta,c,H):
    return -K*beta*(A+H*H)+H*(A/12+2*c/3-pi*pi*beta*beta/16)

def cov_roots(A,beta,c):
    L=A/12+2*c/3-pi*pi*beta*beta/16
    D=L*L-4*K*K*beta*beta*A
    if L<=0 or D<0:return None
    return ((L-sqrt(D))/(2*K*beta),(L+sqrt(D))/(2*K*beta))

def hull_area(P):
    P=sorted(set(P))
    if len(P)<3:return 0.
    def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower=[]
    for p in P:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(P):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
        upper.append(p)
    return polygon_area(lower[:-1]+upper[:-1])

def project(P,H,u):
    # Independent convex-hull reconstruction, without using the width formulas.
    x,y,z=u
    v=(1.,0.,0.) if abs(x)<.8 else (0.,1.,0.)
    a=(y*v[2]-z*v[1],z*v[0]-x*v[2],x*v[1]-y*v[0])
    m=sqrt(sum(k*k for k in a));a=tuple(k/m for k in a)
    b=(y*a[2]-z*a[1],z*a[0]-x*a[2],x*a[1]-y*a[0])
    pts=[(xx,yy,t) for (xx,yy) in P for t in [-H/2,H/2]]
    w=[sum(k*l for k,l in zip(p,u)) for p in pts]
    q=[(sum(k*l for k,l in zip(p,a)),sum(k*l for k,l in zip(p,b))) for p in pts]
    return max(w)-min(w),hull_area(q)

def mc_covariance(P,H,n=9000):
    rng=Random(20261101)
    sw=sb=swb=0.
    for _ in range(n):
        z=2*rng.random()-1
        ph=2*pi*rng.random()
        s=sqrt(1-z*z)
        w,b=project(P,H,(s*cos(ph),s*sin(ph),z))
        sw+=w;sb+=b;swb+=w*b
    return swb/n-(sw/n)*(sb/n)

def main():
    sq=[(-.5,-.5),(.5,-.5),(.5,.5),(-.5,.5)]
    thin=[(-.5,-.025),(.5,-.025),(.5,.025),(-.5,.025)]
    tri=[(cos(2*pi*i/3),sin(2*pi*i/3)) for i in range(3)]
    circ=[(cos(2*pi*i/32),sin(2*pi*i/32)) for i in range(32)]
    for name,P in [('square',sq),('thin_rectangle',thin),('triangle',tri),('regular_32_gon',circ)]:
        A,beta,c=invariants(P)
        for H in (.5,1.5,3.5):
            theory=cov_formula(A,beta,c,H)
            sample=mc_covariance(P,H)
            assert abs(theory-sample)<.07*(1+abs(theory)),(name,H,theory,sample)
        root=cov_roots(A,beta,c)
        if root:assert abs(root[0]*root[1]-A)<1e-9
        print(name,'A',round(A,9),'roots',root,'checked')
    A,beta,c=pi,2.,4.
    r=cov_roots(A,beta,c)
    assert r and r[0]<1.5<r[1] and abs(r[0]*r[1]-pi)<1e-11
    assert cov_roots(*invariants(thin)) is None
    # Exact rectangle Fourier means, against discrete angular integration.
    for eps in (.05,.5,1.):
        rec=[(-.5,-eps/2),(.5,-eps/2),(.5,eps/2),(-.5,eps/2)]
        A,beta,c=invariants(rec)
        assert abs(A-eps)<1e-12
        assert abs(beta-2*(1+eps)/pi)<1e-7
        assert abs(c-((1+eps*eps)/pi+eps))<1e-7
    # Constant-width gap always strictly positive by completing the square.
    delta=pi-pi*pi/4-2/3
    assert delta>0
    print('CIRCULAR_ROOTS',r,'UNIVERSAL_CONSTANT_WIDTH_GAP',delta)
    print('ALL_SAME_NORMAL_PRISM_COVARIANCE_CHECKS_PASSED')
if __name__=='__main__':main()
