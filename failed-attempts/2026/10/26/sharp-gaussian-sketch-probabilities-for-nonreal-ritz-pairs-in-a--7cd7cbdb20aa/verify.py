"""Independent arithmetic and distributional checks for a two-step Gaussian-sketched projection.
Usage: python3 verify.py. Only Python standard library is required.
The exact finite-sketch probability and asymptotic are proved separately; tests are not proofs.
"""
import math
import random
from fractions import Fraction as F


def scalar_product(u,v):
    return sum(a*b for a,b in zip(u,v))


def projected_from_sketch(rows,d,b,c):
    # A = [[d,b,0],[b,d,c],[0,c,d]], V=[e1,e2].
    g1=[r[0] for r in rows]
    g2=[r[1] for r in rows]
    h=[r[2] for r in rows]
    a=scalar_product(g1,g1)
    z=scalar_product(g1,g2)
    f=scalar_product(g2,g2)
    det=a*f-z*z
    if det==0: raise ValueError('sketch has dependent first columns')
    q1=scalar_product(g1,h)
    q2=scalar_product(g2,h)
    w1=(f*q1-z*q2)/det
    w2=(a*q2-z*q1)/det
    return ((d,b+c*w1),(b,d+c*w2)),(w1,w2)


def discriminant(M):
    return (M[0][0]-M[1][1])**2+4*M[0][1]*M[1][0]


def angular(r,b):
    if r<=b: return 0.0
    arg=(math.sqrt(r*r+8*b*b)-2*b)/r
    return math.acos(min(1,max(-1,arg)))/math.pi


def conditional_probability_ratio(nu,b,c,N=20000):
    # Simpson integral over the uniform radial-survival variable conditional on radius>b.
    assert N%2==0
    def f(t):
        if t==0 or t==1: return 0.
        rt=(b*b+c*c)*math.exp(-2*math.log(t)/nu)-c*c
        return angular(math.sqrt(rt),b)
    total=f(0)+f(1)
    for j in range(1,N):
        total+=(4 if j%2 else 2)*f(j/N)
    return total/(3*N)


def exact_probability(nu,b,c):
    return (1+(b/c)**2)**(-nu/2)*conditional_probability_ratio(nu,b,c)


def lead_ratio(nu,b,c):
    return math.sqrt((b*b+c*c)/(3*math.pi*b*b*nu))


def verify():
    checks=0
    # Exact rational example: SPD A has eigenvalues 5, 5+sqrt(5), 5-sqrt(5).
    B,w=projected_from_sketch([[F(1),F(0),F(-1)],
                               [F(0),F(1),F(0)],
                               [F(0),F(0),F(1)]],F(5),F(1),F(2))
    assert B==((F(5),F(-1)),(F(1),F(5)))
    assert w==(F(-1),F(0))
    assert discriminant(B)==-4
    checks+=3
    # Exact rational check for the Gaussian projection algebra on arbitrary integer sketches.
    rng=random.Random(230614206)
    for _ in range(1000):
        rows=[[F(rng.randrange(-4,5)) for i in range(3)] for j in range(4)]
        try: M,(w1,w2)=projected_from_sketch(rows,F(7),F(2),F(3))
        except ValueError:continue
        g1=[r[0] for r in rows];g2=[r[1] for r in rows];h=[r[2] for r in rows]
        assert scalar_product(g1,[h[i]-g1[i]*w1-g2[i]*w2 for i in range(4)])==0
        assert scalar_product(g2,[h[i]-g1[i]*w1-g2[i]*w2 for i in range(4)])==0
        assert discriminant(M)==(F(3)*w2)**2+F(8)*(F(2)+F(3)*w1)
        checks+=3
    # Purely numerical tests: direct Gaussian sketch vs Student radial survival.
    for ell in (2,3,5,9):
        nu=ell-1
        nsamp=20000
        nr=0;event=0
        radius=1.
        for i in range(nsamp):
            rows=[[rng.gauss(0,1) for k in range(3)] for j in range(ell)]
            M,(w1,w2)=projected_from_sketch(rows,5.,1.,1.)
            nr+=int(w1*w1+w2*w2>radius*radius)
            event+=int(discriminant(M)<0)
        radial=(1+radius*radius)**(-nu/2)
        assert abs(nr/nsamp-radial)<0.015,(ell,nr/nsamp,radial)
        predicted=exact_probability(nu,1.,1.)
        assert abs(event/nsamp-predicted)<0.012,(ell,event/nsamp,predicted)
        checks+=2
    # The angular probability is exactly zero at the closest radius and positive beyond.
    assert angular(1.,1.)==0
    for r in (1.01,1.1,2.,5.,50.):
        assert 0<angular(r,1.)<0.5
        checks+=1
    # Strong convergence checks for the derived leading asymptotic constant.
    for b,c in ((1.,1.),(2.,0.5),(1.,3.)):
        for nu in (500,2000,8000):
            ratio=conditional_probability_ratio(nu,b,c)/lead_ratio(nu,b,c)
            assert abs(ratio-1)<(0.12 if c>2*b else 0.04), (b,c,nu,ratio)
            checks+=1
    print('PASS: ',checks,'exact and numerical check assertions')
    print('SPD deterministic witness: Hhat = [[5,-1],[1,5]], eigenvalues 5 +/- i')
    for nu in (1,3,7,99):
        print('nu =',nu,' P_complex(b=c=1) =',format(exact_probability(nu,1.,1.), '.12g'))

if __name__=='__main__': verify()
