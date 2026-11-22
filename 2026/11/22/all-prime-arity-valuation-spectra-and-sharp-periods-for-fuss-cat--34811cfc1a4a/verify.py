"""Exact checks of arity-index valuations of generalized Catalan numbers.

No external dependencies. Finite tests support, but do not replace, the proof.
"""
from collections import Counter
from fractions import Fraction as Q
from math import comb


def vp(n, p):
    assert n > 0
    j = 0
    while n % p == 0:
        n //= p
        j += 1
    return j


def digits(m, p):
    assert m > 0
    out = []
    while m:
        out.append(m % p)
        m //= p
    return out


def coefficients_distribution(m, p, max_degree):
    """Exact probability masses through degree max_degree, via carry states."""
    lo = [Q(1)] + [Q(0)] * max_degree
    hi = [Q(0)] * (max_degree + 1)
    for d in digits(m, p):
        a = [Q(0)] * (max_degree + 1)
        b = [Q(0)] * (max_degree + 1)
        for j in range(max_degree + 1):
            a[j] += lo[j] * Q(p-d,p) + hi[j]*Q(p-d-1,p)
            if j:
                b[j] += lo[j-1]*Q(d,p) + hi[j-1]*Q(d+1,p)
        lo, hi = a, b
    out = lo[:]
    for j in range(max_degree + 1):
        for i in range(j+1):
            out[j] += hi[i] * Q(p-1,p**(j-i+1))
    return out


def arity_val(n, t, p):
    z = comb((t+1)*n,n) // (t*n+1)
    return vp(z,p)


def reduced_column(n,p):
    return n // p**vp(n,p) if n%p==0 else n-1


def check():
    assertions = 0
    cases = 0
    for p in (2,3,5,7):
        for n in range(2,28):
            m = reduced_column(n,p)
            L = len(digits(m,p))
            vals = coefficients_distribution(m,p,8)
            assert vals[0] == Q(1, p**L) * __import__('math').prod(p-d for d in digits(m,p)); assertions += 1
            # Independent finite exact calculations of the normalized valuation.
            for t in range(0,40):
                a=arity_val(n,t,p)
                if n%p==0:
                    b=vp(comb((t+1)*m,m),p)
                else:
                    b=vp(comb((t+1)*n,n-1),p)
                assert a==b,(p,n,t,a,b)
                assertions+=1
            for k in (1,2,3,4):
                period=p**(L+k-1)
                if period>1500: continue
                masses = coefficients_distribution(m,p,k-1)
                hist=Counter()
                for t in range(period):
                    v=min(k,arity_val(n,t,p))
                    hist[v]+=1
                    assertions+=1
                for j in range(k):
                    assert hist[j] == period*masses[j], (p,n,k,j,hist[j],period*masses[j]);assertions+=1
                assert hist[k] == period*(1-sum(masses)), (p,n,k,hist[k]); assertions+=1
                if period>1:
                    half=period//p
                    assert any(min(k,arity_val(n,t,p)) != min(k,arity_val(n,t+half,p)) for t in range(period)),(p,n,k)
                    assertions+=1
                cases+=1
    # Direct mean via exact transfer-polynomial differentiation at z=1, including infinite geometric tail.
    for p in (2,3,5,7):
        for m in range(1,101):
            digits_m=digits(m,p)
            lo=[Q(1)];hi=[Q(0)]
            # Polynomial list, no truncation.
            for d in digits_m:
                a=[Q(0)]*(len(lo)+1);b=[Q(0)]*(len(lo)+1)
                for j in range(len(lo)):
                    a[j]+=lo[j]*Q(p-d,p)+hi[j]*Q(p-d-1,p)
                    b[j+1]+=lo[j]*Q(d,p)+hi[j]*Q(d+1,p)
                lo,hi=a,b
            total=sum(lo)+sum(hi)
            assert total==1; assertions+=1
            mean=sum(j*v for j,v in enumerate(lo)) + sum((j+Q(1,p-1))*v for j,v in enumerate(hi))
            assert mean==Q(sum(digits_m),p-1),(p,m,mean);assertions+=1
    print(f'VERIFY_OK assertions={assertions} full_period_histograms={cases} primes=2,3,5,7 mean_cases=400')


if __name__ == '__main__':
    check()
