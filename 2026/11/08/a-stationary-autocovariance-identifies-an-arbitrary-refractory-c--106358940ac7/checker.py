"""Exact finite-phase checks for a stationary partial-reset diffusion's covariance.

The general theorem is proved analytically; this checker verifies rational
Markov-phase special cases without relying on the renewal derivation.
Only Python's standard library is required.
"""
from fractions import Fraction as F
from math import exp, isclose


def solve(A, b):
    a = [list(map(F, row)) + [F(rhs)] for row, rhs in zip(A, b)]
    n = len(a)
    for j in range(n):
        pivot = next(k for k in range(j, n) if a[k][j])
        a[j], a[pivot] = a[pivot], a[j]
        z = a[j][j]
        a[j] = [x / z for x in a[j]]
        for i in range(n):
            if i != j:
                z = a[i][j]
                a[i] = [a[i][k] - z * a[j][k] for k in range(n + 1)]
    return [row[-1] for row in a]


def transform(a, r, D, mean, s, w):
    Q = 2 * D / (r * (1 - a * a))
    e = (s + a * r * (1 - w)) / (s * (s + r - a * r * w))
    residual = 1 / s + (1 - w) / (mean * s) * (e - 1 / s)
    return Q / (1 + r * mean) * (e + a * a * r * mean * residual)


def direct_exponential(a, r, D, mean, s):
    h = 1 / mean
    Q = 2 * D / (r * (1 - a * a))
    pE = 1 / (1 + r * mean)
    M = [[-r, h], [a * r, -h]]
    initial = [pE * Q, pE * r * mean * a * a * Q]
    A = [[(s if i == j else 0) - M[i][j] for j in range(2)] for i in range(2)]
    return sum(solve(A, initial), F(0))


def direct_erlang2(a, r, D, mean, s):
    h = 2 / mean
    Q = 2 * D / (r * (1 - a * a))
    pE = 1 / (1 + r * mean)
    M = [[-r, 0, h], [a * r, -h, 0], [0, h, -h]]
    initial = [pE * Q, pE * r / h * a * a * Q, pE * r / h * a * a * Q]
    A = [[(s if i == j else 0) - M[i][j] for j in range(3)] for i in range(3)]
    return sum(solve(A, initial), F(0))


def direct_hyperexponential(a, r, D, h1, h2, p, s):
    m = p / h1 + (1-p) / h2
    Q = 2 * D / (r * (1 - a * a))
    pe = 1 / (1 + r * m)
    M = [[-r,h1,h2],[a*r*p,-h1,0],[a*r*(1-p),0,-h2]]
    v = [pe*Q, pe*r*p/h1*a*a*Q, pe*r*(1-p)/h2*a*a*Q]
    A = [[(s if i==j else 0)-M[i][j] for j in range(3)] for i in range(3)]
    return sum(solve(A,v),F(0))


def inverse_w(a,r,D,m,s,chat):
    Q=2*D/(r*(1-a*a))
    G=(1+r*m)*chat/Q
    H=G-a*a*r*m/s
    return 1-s*s*(1-(s+r*(1-a))*H)/(a*r*(s*s*H-s+a*r*(1-a)))


def main():
    tests=0
    for a,r,D,mean in [(F(2,5),F(3,2),F(5,4),F(4,3)),
                        (F(3,4),F(2),F(3,5),F(1,2)),
                        (F(1,3),F(5,3),F(2,7),F(4,5))]:
        special=a*r
        ss=[F(1,9),F(1,2),F(7,5),F(13,4),special]
        for s in ss:
            wE=1/(1+s*mean)
            w2=(1/(1+s*mean/2))**2
            e=transform(a,r,D,mean,s,wE)
            er=transform(a,r,D,mean,s,w2)
            assert e==direct_exponential(a,r,D,mean,s)
            assert er==direct_erlang2(a,r,D,mean,s)
            tests +=2
            Q=2*D/(r*(1-a*a))
            if s==special:
                expected=Q/(1+r*mean)*(1/r+a*mean)
                assert e==er==expected
                tests+=1
            else:
                assert inverse_w(a,r,D,mean,s,e)==wE
                assert inverse_w(a,r,D,mean,s,er)==w2
                tests+=2
            b=Q*(1+a*a*r*mean)/(1+r*mean)/Q
            assert (1-b)/(r*(b-a*a))==mean
            tests+=1
        # independent hyperexponential model of random idle times
        h1=F(2,3); h2=F(7,2); p=F(2,5)
        mh=p/h1+(1-p)/h2
        for s in [F(1,5),F(4,3),F(8,3),a*r]:
            w=p*h1/(s+h1)+(1-p)*h2/(s+h2)
            x=transform(a,r,D,mh,s,w)
            assert x==direct_hyperexponential(a,r,D,h1,h2,p,s)
            tests+=1
            if s!=a*r:
                assert inverse_w(a,r,D,mh,s,x)==w
                tests+=1

    # Strict ordering of exponential and deterministic refractory transforms,
    # and a single universal Laplace-spectrum crossing.
    for a,r,D,m in [(.2,1.8,1.,.75),(.6,3.,.5,2.),(.8,.7,3.,1.1)]:
        for s in [.1*a*r,.5*a*r,a*r,2*a*r,7*a*r]:
            wExp=1/(1+s*m)
            wDet=exp(-s*m)
            expv=transform(a,r,D,m,s,wExp)
            detv=transform(a,r,D,m,s,wDet)
            if s<a*r:
                assert expv>detv
            elif s>a*r:
                assert expv<detv
            else:
                assert isclose(expv,detv,rel_tol=2e-13,abs_tol=2e-13)
            tests+=1
    print(f'PASS: {tests} exact-rational / finite-phase / numerical checks')

if __name__=='__main__':
    main()
