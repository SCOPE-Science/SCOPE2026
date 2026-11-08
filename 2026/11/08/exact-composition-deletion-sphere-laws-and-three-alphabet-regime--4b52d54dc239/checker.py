"""Reproducibility checker for prefix/suffix composition deletion sphere laws.
Uses only Python's standard library; exact rational arithmetic throughout.
"""
from fractions import Fraction
from collections import Counter, defaultdict
from itertools import product
from math import factorial


def sphere(x, q):
    n = len(x)
    a = [0] * q
    b = [0] * q
    spectrum = []
    for j in range(1, n + 1):
        a[x[j - 1]] += 1
        b[x[n - j]] += 1
        spectrum.append(tuple(a))
        spectrum.append(tuple(b))
    return len(set(spectrum))


def exact_empirical(q, n):
    counts = Counter(sphere(x, q) for x in product(range(q), repeat=n))
    return {v: Fraction(c, q**n) for v, c in counts.items()}


def multinomial(j, parts):
    out = factorial(j)
    den = 1
    for x in parts:
        den *= factorial(x)
    return out // den


def compositions(total, q):
    if q == 1:
        yield (total,)
    else:
        for x in range(total + 1):
            for tail in compositions(total - x, q - 1):
                yield (x,) + tail


def return_probs(q, m):
    u = [Fraction(1)]
    for j in range(1, m + 1):
        u.append(Fraction(sum(multinomial(j,p)**2 for p in compositions(j,q)), q**(2*j)))
    return u


def conv(a, b, m):
    out = [Fraction(0)] * (m+1)
    for i, ai in enumerate(a[:m+1]):
        if ai:
            for j, bj in enumerate(b[:m+1-i]):
                if bj:
                    out[i+j] += ai*bj
    return out


def renewal_tables(q, m):
    u = return_probs(q, m)
    f = [Fraction(0)] * (m+1)
    for j in range(1,m+1):
        f[j] = u[j] - sum(f[i]*u[j-i] for i in range(1,j))
    h = [1-sum(f[1:j+1]) for j in range(m+1)]
    powers = [[Fraction(1)]+[Fraction(0)]*m]
    for r in range(1,m+1):
        powers.append(conv(powers[-1],f,m))
    return u,f,h,powers


def theoretical(q,n):
    m=n//2
    u,f,h,pow_f = renewal_tables(q,m)
    result=defaultdict(Fraction)
    if n%2:
        # P(Z_m=r)=[z^m]F(z)^r H(z)
        for r in range(m+1):
            prob=sum(pow_f[r][i]*h[m-i] for i in range(m+1))
            result[2*n-1-2*r]+=prob
    else:
        # I_m=1 iff the walk completes its (r+1)-st return exactly at m
        for r in range(m):
            pz=sum(pow_f[r][i]*h[m-1-i] for i in range(m))
            hit=pow_f[r+1][m]
            result[2*n-1-2*r-1]+=hit
            result[2*n-1-2*r]+=(pz-hit)
    return {v:p for v,p in result.items() if p}


def check():
    trials=0
    for q,maxn in [(2,14),(3,9),(4,7)]:
        for n in range(1,maxn+1):
            a=exact_empirical(q,n)
            b=theoretical(q,n)
            assert a==b, (q,n,a,b)
            trials+=q**n
            m=n//2
            u=return_probs(q,m)
            mean=sum(Fraction(x)*p for x,p in b.items())
            theo=(2*n-1-2*sum(u[1:])) if n%2 else (2*n-1-2*sum(u[1:m])-u[m])
            assert mean==theo, (q,n,mean,theo)
    for q in range(2,8):
        for m in range(0,14):
            u,f,h,powers=renewal_tables(q,m)
            assert all(v>=0 for v in f)
            assert all(v>=0 for v in h)
            assert sum(sum(powers[r][i]*h[m-i] for i in range(m+1)) for r in range(m+1))==1
    print(f'PASS exhaustive {trials} input words, q=2 through n=14; q=3 through n=9; q=4 through n=7')
    print('PASS independent renewal normalization for q=2..7, m=0..13; exact means and distributions')

if __name__=='__main__':
    check()
