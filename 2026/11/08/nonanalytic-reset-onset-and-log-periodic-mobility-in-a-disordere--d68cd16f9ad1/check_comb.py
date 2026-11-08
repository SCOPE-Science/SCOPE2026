#!/usr/bin/env python3
"""Exact finite-network and high-precision checks of random-comb asymptotics.
Requires only the Python standard library. Scientific conclusions require the proof.
"""
from decimal import Decimal, localcontext
from fractions import Fraction

PASS = 0

def check(condition, label):
    global PASS
    if not condition:
        raise AssertionError(label)
    PASS += 1


def gauss(A, b):
    """Exact Gaussian elimination of a rational square system."""
    n = len(A)
    aug = [[Fraction(z) for z in A[i]] + [Fraction(b[i])] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if aug[i][j])
        aug[j], aug[pivot] = aug[pivot], aug[j]
        t = aug[j][j]
        aug[j] = [v/t for v in aug[j]]
        for i in range(n):
            if i == j: continue
            t = aug[i][j]
            if t:
                aug[i] = [a-t*b for a,b in zip(aug[i],aug[j])]
    return [aug[i][-1] for i in range(n)]


def branch_exact(L, a, b, r):
    if L == 0: return Fraction(0)
    A = [[Fraction(0) for _ in range(L)] for _ in range(L)]
    rhs = [Fraction(0) for _ in range(L)]
    for m in range(1, L+1):
        if m < L:
            A[m-1][m-1] = a+b+r
            if m < L: A[m-1][m] = -b
        else:
            A[m-1][m-1] = b+r
        if m == 1: rhs[0] = a
        else: A[m-1][m-2] = -a
    return sum(gauss(A,rhs),Fraction(0))


def branch_decimal(L, a, b, r):
    if L == 0: return Decimal(0)
    z = a+b+r
    vp = (z+(z*z-4*a*b).sqrt())/(2*b)
    um = a/(b*vp)
    q = vp/um
    T = (a-b*um)/(b*vp-a)
    w = q ** (-L)
    return ((a-b*um)/r)*(1-w)/(1+T*w)


def comb_exact(lengths, a, b, r):
    N = len(lengths)
    sites = [(i,m) for i,L in enumerate(lengths) for m in range(L+1)]
    idx = {site:j for j,site in enumerate(sites)}
    n=len(sites)
    A=[[Fraction(0) for j in range(n)] for i in range(n)]
    def edge(src,dst,rate):
        x,y=idx[src],idx[dst]
        A[y][x] += rate
        A[x][x] -= rate
    for i,L in enumerate(lengths):
        edge((i,0),((i+1)%N,0),a)
        edge((i,0),((i-1)%N,0),b)
        if L:edge((i,0),(i,1),a)
        for m in range(1,L+1):
            edge((i,m),(i,m-1),b)
            if m<L:edge((i,m),(i,m+1),a)
            edge((i,m),(i,0),r)
    A[-1]=[Fraction(1)]*n
    rhs=[Fraction(0)]*(n-1)+[Fraction(1)]
    p=gauss(A,rhs)
    return {site:p[j] for j,site in enumerate(sites)}


def theta(s, f, x):
    """Rapidly convergent periodization defining the actual leading amplitude."""
    logf=f.ln()
    ans=Decimal(0)
    for j in range(-80,81):
        h=(x-Decimal(j))*logf
        ans+=(s*h).exp()/(Decimal(1)+h.exp())
    return ans


def disorder_mean(r, a, b, rho, cutoff=350):
    total=Decimal(0); mass=Decimal(1)-rho
    p=Decimal(1)
    for L in range(cutoff):
        total += mass*p*branch_decimal(L,a,b,r)
        p *= rho
    return total


def run():
  with localcontext() as ctx:
    ctx.prec=180
    d=lambda x:Decimal(str(x))
    a,b,r=Fraction(7),Fraction(2),Fraction(3,5)
    for L in range(1,9):
        exact=branch_exact(L,a,b,r)
        got=branch_decimal(L,d(7),d(2),d('0.6'))
        want=Decimal(exact.numerator)/Decimal(exact.denominator)
        check(abs(got-want)<d('1e-75'),f'finite branch L={L}')
    a,b,r=Fraction(3),Fraction(1),Fraction(1,2)
    lengths=(1,0,2,3)
    joint=comb_exact(lengths,a,b,r)
    p0=next(joint[(i,0)] for i in range(len(lengths)))
    for i,L in enumerate(lengths):
        check(joint[(i,0)]==p0, f'backbone uniform i={i}')
        check(sum(joint[(i,m)] for m in range(1,L+1))==p0*branch_exact(L,a,b,r),f'branch marginal i={i}')
    E=sum((branch_exact(L,a,b,r) for L in lengths),Fraction(0))/len(lengths)
    check(p0 == Fraction(1,len(lengths))/(1+E),'exact normalization')
    check(sum(joint.values(),Fraction(0))==1,'exact stationary mass')
    check((a-b)*len(lengths)*p0 == (a-b)/(1+E),'exact drift')
    # Geometric teeth and a large bias enhance nonconstant log-periodic modulation.
    a,b=d(100),d(1)
    f=a/b;c=(a-b)*(a-b)/a
    rho=d('0.1');s=d('0.5')
    t0=theta(s,f,d('0'))
    t1=theta(s,f,d('0.5'))
    check(abs(t0-t1)>d('0.01'),'nontrivial phase amplitude f=100')
    for phase in (d('0'),d('0.5')):
        for n in (4,6,8,10):
            rr=c*(f**(-n-phase))
            E=disorder_mean(rr,a,b,rho)
            speed=(a-b)/(1+E)
            prediction=(c**s)*(rr**(1-s))/((1-rho)*theta(s,f,phase))
            rel=abs(speed/prediction-1)
            check(rel<d('2e-3'),f'fractional onset phase={phase} n={n}, rel={rel}')
    # At the exact trap threshold rho=1/f, the coefficient is inverse logarithmic.
    rho=Decimal(1)/f
    for n in (20,30,40,50):
        rr=c*(f**(-n))
        E=disorder_mean(rr,a,b,rho)
        check(abs(E/Decimal(n)-1)<d('0.05'),f'critical logarithmic branch mass n={n}')
        speed=(a-b)/(1+E)
        check(abs(speed*Decimal(n)/(a-b)-1)<d('0.06'),f'critical inverse log speed n={n}')
    print('PASS',PASS,'independent rational-stationarity and high-precision assertions')
    print('theta(0)=',t0)
    print('theta(1/2)=',t1)
    print('phase contrast relative=',abs(t0-t1)/t0)

if __name__=='__main__':
    run()
