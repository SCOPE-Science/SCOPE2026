"""Exact finite-state checks for an independent-seed bond outbreak on P3.
Uses only the Python standard library; analytic monotonicity is proved separately.
"""
from fractions import Fraction as Q
from itertools import product

N_CHECKS = 0

def check(condition, message):
    global N_CHECKS
    N_CHECKS += 1
    if not condition:
        raise AssertionError(message)

def enum(q, p):
    """Independently sum all 8 imported-seed and 4 edge states."""
    ex0=ex1=ex2=ex01=ex02=prseed=Q(0)
    for seeds in product((0,1),repeat=3):
        seedprob=Q(1)
        for s in seeds:
            seedprob*=q if s else (1-q)
        for e0,e1 in product((0,1),repeat=2):
            edgeprob=(p if e0 else (1-p))*(p if e1 else (1-p))
            weight=seedprob*edgeprob
            connected=[{0},{1},{2}]
            if e0:
                connected[0].add(1); connected[1].add(0)
            if e1:
                connected[1].add(2); connected[2].add(1)
            active={i for i,s in enumerate(seeds) if s}
            reach=set(active)
            while True:
                new=reach | set().union(*(connected[v] for v in reach)) if reach else set()
                if new==reach:break
                reach=new
            x0,x1,x2=(int(i in reach) for i in range(3))
            ex0+=weight*x0;ex1+=weight*x1;ex2+=weight*x2
            ex01+=weight*x0*x1;ex02+=weight*x0*x2
            prseed+=weight*bool(active)
    return ex0,ex1,ex2,ex01,ex02,prseed

def analytic(q,p):
    t=1-q
    A=t*(1-p)+p*(1-p)*t*t+p*p*t**3
    B=t*(1-p)**2+2*p*(1-p)*t*t+p*p*t**3
    C=t*t*(1-p+p*t)
    D=t*t*((1-p)**2+(2*p-p*p)*t)
    z=1-t**3
    nadj=z*(1-A-B+C)-(1-A)*(1-B)
    nend=z*(1-2*A+D)-(1-A)**2
    F=-t+(2+t-t*t)*p+(t*t+2*t-1)*p*p-t*(1-t)*p**3
    adjfactor=(1-p)*q*q*t*t*F
    endfactor=-q*q*t**3*(1-p)**2*(1+2*p*(1+t)+p*p*t)
    return A,B,C,D,z,nadj,nend,F,adjfactor,endfactor

for di in range(1,13):
    for dj in range(1,13):
        q,p=Q(di,13),Q(dj,13)
        ex0,ex1,ex2,ex01,ex02,zobs=enum(q,p)
        A,B,C,D,z,nadj,nend,F,af,ef=analytic(q,p)
        check(zobs==z, 'seed event')
        check(ex0==1-A and ex2==1-A and ex1==1-B, 'marginal event')
        check(ex01==1-A-B+C, 'adjacent joint')
        check(ex02==1-2*A+D, 'end joint')
        check(nadj==af, 'adj factorization')
        check(nend==ef, 'end factorization')
        check(z*ex01-ex0*ex1==nadj,'adj direct conditional covariance')
        check(z*ex02-ex0*ex2==nend,'end direct conditional covariance')
        check(nend<0, 'strict endpoint anticorrelation')
        check(z>0,'conditioning positive')
        fp0=2+(1-q)-(1-q)**2
        check(fp0>0, 'positive derivative at zero')
        check(F==(- (1-q)+(2+(1-q)-(1-q)**2)*p+((1-q)**2+2*(1-q)-1)*p**2-(1-q)*q*p**3),'polynomial')

for qi in range(1,100):
    q=Q(qi,101);t=1-q
    f=lambda p: -t+(2+t-t*t)*p+(t*t+2*t-1)*p*p-t*(1-t)*p**3
    check(f(Q(0))<0, 'left root sign')
    check(f(Q(1))>0, 'right root sign')
    for k in range(101):
        p=Q(k,100)
        deriv=(2+t-t*t)*(1-p)**2+2*(1+3*t)*p*(1-p)+2*t*(1+2*t)*p*p
        check(deriv>0, 'Bernstein derivative positivity')
        if k<100:
            check(f(Q(k+1,100))>f(p),'strict increase')
print('PASS:', N_CHECKS, 'exact finite-state, factorization, root and monotonicity checks')
