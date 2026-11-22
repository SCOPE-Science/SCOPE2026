"""Deterministic numerical checks for conditional crossing-chord radial theorem.
Uses only Python standard library; no third-party dependencies.
"""
import math
import random

PI=math.pi

def deficiency(angle, u, v):
    a=angle; b=PI-a
    s=math.sin(a)
    return ((math.cos(a*u)-math.cos(a))*(math.cos(b*v)-math.cos(b)))/(s*s)

def mean_deficiency(angle):
    return (1/angle-1/math.tan(angle))*(1/(PI-angle)+1/math.tan(angle))

def exact_cdf(angle,r):
    if r<=0: return 0.
    if r>=1: return 1.
    a=angle; b=PI-a; c=math.cos(a)
    # Smooth substitution t=cos(a u) eliminates square-root endpoint singularity.
    # With u>=0 uniform, P(Y>=z)=arccos(cos b+z)/b.
    def fun(u):
        x=math.cos(a*u)-c
        thresh=(1-r*r)*math.sin(a)**2/x if x>0 else math.inf
        val=math.cos(b)+thresh
        if val>=1: return 0.
        if val<=math.cos(b): return 1.
        return math.acos(max(-1,min(1,val)))/b
    return simpson(fun,0.,1.,8000)

def simpson(f,a,b,n):
    assert n%2==0
    h=(b-a)/n
    s=f(a)+f(b)
    for j in range(1,n):s+=(4 if j%2 else 2)*f(a+j*h)
    return h*s/3

def m_k(a,k):
    return simpson(lambda u:(math.cos(a*u)-math.cos(a))**k,0,1,8000)

def circle_point(t):return (math.cos(t),math.sin(t))

def intersection(theta):
    pts=[circle_point(t) for t in theta]
    A,B,C,D=pts
    v=(C[0]-A[0],C[1]-A[1]); w=(D[0]-B[0],D[1]-B[1]); d=(B[0]-A[0],B[1]-A[1])
    det=v[0]*w[1]-v[1]*w[0]
    t=(d[0]*w[1]-d[1]*w[0])/det
    return (A[0]+t*v[0],A[1]+t*v[1])

def conditional_angle(theta):
    gaps=[theta[(i+1)%4]-theta[i] if i<3 else theta[0]+2*PI-theta[3] for i in range(4)]
    return (gaps[0]+gaps[2])/2

if __name__=='__main__':
    rng=random.Random(918273)
    ntests=0
    # Exact geometry vs product identity for 3000 quadrilaterals.
    for _ in range(3000):
        theta=sorted(2*PI*rng.random() for _ in range(4))
        x,y=intersection(theta)
        a=conditional_angle(theta)
        gap=[(theta[1]-theta[0]),(theta[2]-theta[1]),(theta[3]-theta[2]),theta[0]+2*PI-theta[3]]
        u=gap[0]/a-1
        v=gap[1]/(PI-a)-1
        assert abs((1-x*x-y*y)-deficiency(a,u,v))<3e-11
        ntests+=1
    # Independent conditional uniform splits; compare numerical expectation, moment and CDF.
    for a in [.18,.5,1.,PI/2,2.7,3.]:
        b=PI-a
        for k in [1,2,3,4]:
            predicted=m_k(a,k)*m_k(b,k)/math.sin(a)**(2*k)
            manual=simpson(lambda u:simpson(lambda v:deficiency(a,u,v)**k,0,1,300),0,1,300)
            assert abs(predicted-manual)<3e-8,(a,k,predicted,manual)
            ntests+=1
        assert abs(mean_deficiency(a)-m_k(a,1)*m_k(b,1)/math.sin(a)**2)<1e-11
        ntests+=1
        for r in [.15,.37,.69,.87]:
            predicted=exact_cdf(a,r)
            # independently simulate conditional splits with 120k pairs
            draws=120000
            k=sum(1 for _ in range(draws) if deficiency(a,2*rng.random()-1,2*rng.random()-1)>=1-r*r)
            observed=k/draws
            assert abs(observed-predicted)<.012,(a,r,predicted,observed)
            ntests+=1
    # Global radial moment matches the Karamata dilogarithmic radial law.
    # The normalized density of a is 6*a*(pi-a)/pi^3.
    expected=simpson(lambda a: 6*a*(PI-a)/PI**3*(1-mean_deficiency(a)), .00001, PI-.00001, 16000)
    assert abs(expected-6/PI**2)<2e-8,(expected,6/PI**2)
    ntests+=1
    # Center and boundary coefficients, checked at a fixed nondegenerate angle.
    a=.91; b=PI-a
    small=0.015
    pref=PI*math.sin(a)/(2*a*b)
    assert abs(exact_cdf(a,small)/(small**2)-pref)<1e-3
    ntests+=1
    eps=.0002
    # CDF near r=1 uses numerical integration; asymptotic check generously bounded.
    tail=1-exact_cdf(a,1-eps)
    pref2=2/(a*b)
    assert .65<tail/(pref2*eps*math.log(1/eps))<1.4,(tail,pref2*eps*math.log(1/eps))
    ntests+=1
    print('PASS',ntests,'tests; global mean',expected,'target',6/PI**2)
