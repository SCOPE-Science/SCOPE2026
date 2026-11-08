"""Finite reproducibility checks for the cyclic first-Fourier-moment spread theorem.

Run: python3 CHECK.py. Requires Python >= 3.9 and no third-party packages.
The theorem for all orders follows from strict convexity, not from these tests.
"""
import math
import random

TAU = 2.0 * math.pi


def data(n, rho):
    assert n >= 3 and 0.0 <= rho <= 1.0
    r = n // 2
    cs = [math.cos(TAU * j / n) for j in range(r + 1)]
    # Choose a segment at or above the first-harmonic target.
    k = next(j for j in range(r) if cs[j] + 1e-14 >= rho >= cs[j+1] - 1e-14)
    a, b = cs[k], cs[k+1]
    x = (rho - b) / (a - b)
    y = 1.0 - x
    beta = ((k+1)**2 - k**2) / (b-a)
    alpha = k**2 - beta*a
    return k, x, y, alpha, beta


def moment(p):
    n = len(p)
    return sum(p[j] * complex(math.cos(TAU*j/n), math.sin(TAU*j/n)) for j in range(n))


def dist2(n, j, center=0):
    z = (j - center) % n
    return min(z,n-z)**2


def var(p):
    n = len(p)
    return min(sum(p[j]*dist2(n,j,c) for j in range(n)) for c in range(n))


def bound(n,rho):
    k,x,y,alpha,beta = data(n,rho)
    return x*k*k + y*(k+1)**2


def canonical(n,rho):
    k,x,y,_,_ = data(n,rho)
    p = [0.0]*n
    if k == 0:
        p[0] += x
    else:
        p[k] += x/2; p[-k] += x/2
    p[(k+1)%n] += y/2
    p[-(k+1)%n] += y/2
    return p


def run():
    rng = random.Random(260907)
    count = 0
    for n in range(3,53):
        targets=[0.,1.]+[j/32. for j in range(33)]
        for rho in targets:
            k,x,y,alpha,beta=data(n,rho)
            assert x >= -1e-12 and y >= -1e-12
            assert beta < 0
            p=canonical(n,rho)
            assert abs(sum(p)-1)<2e-12
            assert abs(moment(p).real-rho)<4e-12
            assert abs(moment(p).imag)<4e-12
            assert abs(var(p)-bound(n,rho))<1e-8
            assert abs(bound(n,rho)-(alpha+beta*rho))<1e-8
            assert all(dist2(n,j) >= alpha+beta*math.cos(TAU*j/n)-1e-8 for j in range(n))
            assert bound(n,rho)+1e-8 >= (n/TAU)**2 * math.acos(rho)**2
            count += 7
        # Exact zero-notch arithmetic resonance.
        b=bound(n,0.)
        if n%4==0: assert abs(b-n*n/16)<1e-9
        if n%4==2: assert abs(b-(n*n/16+0.25))<1e-9
        count+=1
        for _ in range(135):
            w=[rng.random() for j in range(n)]
            w=[v/sum(w) for v in w]
            rho=abs(moment(w))
            b=bound(n,rho)
            assert var(w)>=b-1e-7, (n,rho,var(w),b)
            # Exact dual defect identity at every cyclic center.
            k,x,y,alpha,beta=data(n,rho)
            c=rng.randrange(n)
            real=sum(w[j]*math.cos(TAU*((j-c)%n)/n) for j in range(n))
            spread=sum(w[j]*dist2(n,j,c) for j in range(n))
            slack=sum(w[j]*(dist2(n,j,c)-alpha-beta*math.cos(TAU*((j-c)%n)/n)) for j in range(n))
            gap=-beta*(rho-real)
            assert slack>=-1e-7 and gap>=-1e-7
            assert abs(spread-b-(slack+gap)) < 3e-7
            count+=4
    print('CYCLIC_NOTCH_SPREAD_CHECKS_PASSED',count)


if __name__=='__main__':
    run()
