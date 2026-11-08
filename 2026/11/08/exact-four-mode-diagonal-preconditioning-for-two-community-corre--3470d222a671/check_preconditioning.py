#!/usr/bin/env python3
"""Standalone deterministic exact and finite numerical checks of the two-community scaling formula."""
from fractions import Fraction as Q
import math
import random


def formula(m, n, u, v, g):
    alpha = 1 + (m - 1) * u
    beta = 1 + (n - 1) * v
    a, b = 1 - u, 1 - v
    delta = m * n * g * g
    assert m >= 2 and n >= 2 and 0 < u < 1 and 0 < v < 1 and g > 0
    assert delta < alpha * beta
    x0, xc = beta / alpha, b / a
    def clip(z, lo, hi):
        return min(hi, max(lo, z))
    if x0 <= xc:
        xstar = clip((beta - delta / (alpha - a)) / a, x0, xc)
    else:
        den = alpha * (beta - b) - delta
        xstar = clip(b * (beta - b) / den, xc, x0) if den > 0 else x0
    return xstar


def condition(m, n, u, v, g, x):
    alpha = 1 + (m - 1) * u
    beta = 1 + (n - 1) * v
    a, b = 1 - u, 1 - v
    delta = m * n * g * g
    disc = math.sqrt((alpha*x - beta)**2 + 4*delta*x)
    larger = (alpha*x + beta + disc)/2
    smaller = 2*x*(alpha*beta-delta)/(alpha*x+beta+disc)
    return larger/min(smaller,a*x,b)


def determinant(M):
    N=len(M)
    if N==0: return Q(1)
    if N==1: return M[0][0]
    return sum(((-1)**j)*M[0][j]*determinant([row[:j]+row[j+1:] for row in M[1:]]) for j in range(N))


def exact_example():
    m=n=2;u=Q(3,10);v=Q(3,5);g=Q(1,2)
    a=1-u;b=1-v;alpha=1+u;beta=1+v;delta=4*g*g
    x0=beta/alpha;xc=b/a
    den=alpha*(beta-b)-delta
    assert x0==Q(16,13) and xc==Q(4,7)
    xstar=formula(m,n,u,v,g)
    assert xstar==Q(6,7) and den==Q(14,25)
    assert a*xstar==Q(3,5) and b==Q(2,5)
    assert alpha*xstar+beta==Q(19,7)
    assert xstar*(alpha*beta-delta)==Q(162,175)
    lam_minus=Q(2,5);lam_plus=Q(81,35)
    assert lam_minus+lam_plus==alpha*xstar+beta
    assert lam_minus*lam_plus==xstar*(alpha*beta-delta)
    assert lam_plus/lam_minus==Q(81,14)
    A=[[Q(1),u,g,g],[u,Q(1),g,g],[g,g,Q(1),v],[g,g,v,Q(1)]]
    d2=[xstar,xstar,Q(1),Q(1)]
    AD2=[[A[i][j]*d2[j] for j in range(4)] for i in range(4)]
    for z in range(5):
        z=Q(z)
        mat=[[z*(i==j)-AD2[i][j] for j in range(4)] for i in range(4)]
        exact=(z-Q(3,5))*(z-Q(2,5))*(z-lam_minus)*(z-lam_plus)
        assert determinant(mat)==exact
    assert Q(29,8)+Q(1,8)*Q(20,1) > Q(81,14) # rough strict bound on unscaled Jacobi
    return 21


def run():
    checked=exact_example()
    rng=random.Random(20261107)
    for _ in range(3000):
        m,n=rng.randint(2,13),rng.randint(2,13)
        u,v=rng.uniform(.002,.998),rng.uniform(.002,.998)
        alpha=1+(m-1)*u;beta=1+(n-1)*v
        g=rng.uniform(.01,.99)*math.sqrt(alpha*beta/(m*n))
        xs=formula(m,n,u,v,g)
        fs=condition(m,n,u,v,g,xs)
        for k in range(-12,13):
            x=xs*math.exp(k*.09)
            fx=condition(m,n,u,v,g,x)
            assert fs <= fx*(1+3e-12), (m,n,u,v,g,xs,x,fs,fx)
            checked+=1
    print('PASS:',checked,'rational identity and finite-parameter checks')


if __name__ == '__main__':
    run()
