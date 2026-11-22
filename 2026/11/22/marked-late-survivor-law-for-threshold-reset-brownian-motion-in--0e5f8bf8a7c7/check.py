#!/usr/bin/env python3
"""Exact renewal checks for a marked heavy-tailed threshold-reset model.

No inference from finite tests to the continuum asymptotic theorem is made.
The analytic proof is given in RESULT.md.
"""
from fractions import Fraction
from math import isclose


def limit_law(b, nmax=40):
    a = 1-b
    joint = [(a*b**k/2, a*b**k/2) for k in range(nmax)]
    total = [a*b**n/2 + (a*a*n*b**(n-1)/2 if n else 0) for n in range(nmax)]
    assert abs(sum(map(sum, joint))-1) < 1.e-12
    assert abs(sum(total)-1) < 1.e-12
    assert abs(sum(n*p for n,p in enumerate(total)) - (2*b+1)/(2*a))<1.e-10
    assert abs(sum(n*n*p for n,p in enumerate(total)) - ((2*b+1)**2+1+6*b)/(4*a*a))<1.e-8
    return joint,total


def discrete_test(t, kmax=17, a=.6, b=.4, delta=.2):
    """Integer Pareto cycle durations: P(H=n)=1/[n(n+1)].

    Each exit type has the same heavy-component mass delta,
    but unequal total exit probabilities a, b.
    """
    f=[0.]*(t+1)
    for n in range(1,t+1):
        f[n]=delta/(n*(n+1))+(b-delta if n==1 else 0.)
    qA=[a]+[delta/(n+1) for n in range(1,t+1)]
    qB=[b]+[delta/(n+1) for n in range(1,t+1)]
    h=[0.]*(t+1)
    h[0]=1.
    rows=[]
    for k in range(kmax+1):
        pA=sum(h[s]*qA[t-s] for s in range(t+1))
        pB=sum(h[s]*qB[t-s] for s in range(t+1))
        rows.append((pA,pB))
        nxt=[0.]*(t+1)
        for s,v in enumerate(h):
            if v==0.:continue
            for j in range(1,t+1-s):
                nxt[s+j]+=v*f[j]
        h=nxt
    norm=sum(x+y for x,y in rows)
    out=[(x/norm,y/norm) for x,y in rows]
    ideal=[((a/2)*b**k,(a/2)*b**k) for k in range(kmax+1)]
    total_variation=.5*(sum(abs(x-X)+abs(y-Y) for (x,y),(X,Y) in zip(out,ideal)) + b**(kmax+1))
    return total_variation, out[0], norm


def main():
    counts=0
    for b in (.05,.2,.4,.5,.8,.95):
        a=1-b
        for n in range(0,22):
            mass=a*b**n/2+(a*a*n*b**(n-1)/2 if n else 0.)
            assert mass >=0
            counts+=1
        joint,total=limit_law(b, nmax=900 if b>.9 else (500 if b>.7 else 100))
        assert abs(sum(total)-1)<1e-10
        assert abs(sum(n*p for n,p in enumerate(total))-(2*b+1)/(2*a))<2e-8
        counts+=3
    errors=[]
    for t in (30,80,180,360):
        tv,zero,norm=discrete_test(t)
        errors.append(tv)
        print(f't={t}: conditional joint TV to marked geometric = {tv:.8f}; P(K=0,Y=A)={zero[0]:.8f}; P(T>t)={norm:.8f}')
        assert tv<.11
        counts+=3
    assert all(x>y for x,y in zip(errors,errors[1:])),errors
    counts+=3
    # The half-plane amplitude follows from a direct reflection-principle check.
    from math import gamma, pi,sin,sqrt
    for theta in (.1,.7,1.2):
        beta=.5;r0=1.7;D=.8;alpha=pi
        A0=4/pi*gamma(1+beta)/gamma(1+2*beta)*(r0*r0/(4*D))**beta*sin(pi*theta/alpha)
        refl=r0*sin(theta)/sqrt(pi*D)
        assert isclose(A0,refl,rel_tol=1e-12)
        counts+=1
    # Quadrant survival factorizes into two half-line survival laws.
    for theta in (.15,.5,1.1):
        beta=1.;r0=1.7;D=.8;alpha=pi/2
        A0=4/pi*gamma(1+beta)/gamma(1+2*beta)*(r0*r0/(4*D))**beta*sin(pi*theta/alpha)
        product=r0*r0*sin(theta)*__import__('math').cos(theta)/(pi*D)
        assert isclose(A0,product,rel_tol=1e-12)
        counts+=1
    print(f'PASS: {counts} algebraic and marked-renewal checks; monotone approach in the synthetic integer-Pareto example')

if __name__=='__main__': main()
