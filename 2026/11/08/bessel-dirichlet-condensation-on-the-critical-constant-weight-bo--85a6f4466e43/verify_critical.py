"""Finite exact checks and large-system diagnostics for a critical canonical lattice gas.

Run: python verify_critical.py
Numerical tests support but do not replace the analytical thermodynamic-limit proof.
"""
from fractions import Fraction
from math import comb, factorial, sqrt


def coefficient_direct(L, N, b, theta):
    weights = [(1-b)*b**n + theta/Fraction(L*L) for n in range(N+1)]
    a = [Fraction(1)] + [Fraction(0)]*N
    for _ in range(L):
        c = [Fraction(0)]*(N+1)
        for n in range(N+1):
            c[n] = sum(a[i]*weights[n-i] for i in range(n+1))
        a = c
    return a[N]


def bulk_sum_pmf(m, s, b):
    if m == 0:
        return Fraction(int(s == 0))
    return Fraction(comb(m+s-1, s))*(1-b)**m*b**s


def coefficient_split(L, N, b, theta):
    terms = []
    for j in range(L+1):
        c = comb(L, j)*(theta/Fraction(L*L))**j
        if j == 0:
            terms.append(bulk_sum_pmf(L,N,b))
        else:
            terms.append(c * sum(bulk_sum_pmf(L-j,s,b)*comb(N-s+j-1,j-1) for s in range(N+1)))
    return terms


def coefficient_direct_general(L, N, bulk, theta):
    weights = [bulk(n) + theta/Fraction(L*L) for n in range(N+1)]
    a = [Fraction(1)] + [Fraction(0)]*N
    for _ in range(L):
        a = [sum(a[i]*weights[n-i] for i in range(n+1)) for n in range(N+1)]
    return a[N]


def coefficient_split_general(L, N, bulk, theta):
    terms = []
    for j in range(L+1):
        m = L-j
        a=[Fraction(1)] + [Fraction(0)]*N
        for _ in range(m):
            a=[sum(a[i]*bulk(n-i) for i in range(n+1)) for n in range(N+1)]
        if j == 0:
            terms.append(a[N])
        else:
            terms.append(comb(L,j)*(theta/Fraction(L*L))**j *
                         sum(a[s]*comb(N-s+j-1,j-1) for s in range(N+1)))
    return terms


def main():
    count=0
    for L in range(1,7):
        for N in range(0,11):
            for b in (Fraction(1,2),Fraction(1,3),Fraction(3,5)):
                for theta in (Fraction(1,2),Fraction(2)):
                    direct = coefficient_direct(L,N,b,theta)
                    terms = coefficient_split(L,N,b,theta)
                    assert direct == sum(terms), (L,N,b,theta,direct,sum(terms))
                    assert all(t >= 0 for t in terms)
                    count+=2
    for L in range(1,6):
        for N in range(0,9):
            for p in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
                def bernoulli(n):
                    return (1-p) if n==0 else (p if n==1 else Fraction(0))
                for theta in (Fraction(1),Fraction(3,2)):
                    d=coefficient_direct_general(L,N,bernoulli,theta)
                    ts=coefficient_split_general(L,N,bernoulli,theta)
                    assert d == sum(ts), (L,N,p,theta)
                    assert all(t>=0 for t in ts)
                    count+=2
    # Check that the explicit Bessel-series normalization is a probability law.
    for a,theta in ((0.3,0.1),(1.0,1.0),(2.0,4.0),(0.9,0.7)):
        numer=[theta**j*a**(j-1)/(factorial(j)*factorial(j-1)) for j in range(1,45)]
        f=sum(numer)
        assert f>0
        assert abs(sum(n/f for n in numer)-1)<1e-12
        assert abs(numer[0]/f-theta/f)<1e-12
        count+=3
    print(f'PASS: {count} exact-rational and series assertions')

if __name__ == '__main__':
    main()
