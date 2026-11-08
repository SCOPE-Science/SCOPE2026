"""Reproduce finite identities for the simple-chord count in a uniform chord diagram.

Uses Python standard library; run: python verify.py
The asymptotic assertions are illustrative, not replacements for the analytic proof.
"""
from collections import Counter
from fractions import Fraction
from math import comb, factorial, exp

checks = 0

def check(cond, message):
    global checks
    if not cond:
        raise AssertionError(message)
    checks += 1

def odd_fact(k):
    z = 1
    for j in range(1, k + 1):
        z *= 2 * j - 1
    return z

def all_pairings(mask):
    if not mask:
        yield ()
        return
    first = mask & -mask
    i = first.bit_length() - 1
    rest = mask ^ first
    while rest:
        last = rest & -rest
        j = last.bit_length() - 1
        rest ^= last
        for p in all_pairings(mask ^ first ^ last):
            yield ((i,j),) + p

def brute_histogram(n):
    n2 = 2*n
    h = Counter()
    for p in all_pairings((1 << n2) - 1):
        c = sum((j-i==1 or (i==0 and j==n2-1)) for i,j in p)
        h[c] += 1
    return h

def exact_factorial_moment(n,k):
    if k > n: return Fraction(0)
    N=2*n
    a=Fraction(1)
    for j in range(k):
        a*=Fraction(N-2*j, N-j-1)
    return a

def exact_distribution(n):
    a=[exact_factorial_moment(n,k) for k in range(n+1)]
    probs=[]
    for r in range(n+1):
        # From p.g.f. E[z^S] = sum E(S)_k (z-1)^k / k!
        probs.append(sum(((-1)**(k-r))*Fraction(comb(k,r), factorial(k))*a[k]
                         for k in range(r,n+1)))
    return probs

def cycle_matchings(n,k):
    N=2*n
    return N*comb(N-k,k)//(N-k)

for n in range(2,7):
    N=2*n
    hist=brute_histogram(n)
    p=exact_distribution(n)
    check(sum(hist.values()) == odd_fact(n), f'pairing count {n}')
    check(sum(p)==1, f'normalization {n}')
    for r in range(n+1):
        check(p[r] == Fraction(hist[r],odd_fact(n)), f'coefficient {n},{r}')
    for k in range(n+1):
        observed=sum(factorial(r)//factorial(r-k)*hist[r] for r in range(k,n+1))
        check(Fraction(observed,odd_fact(n)) == exact_factorial_moment(n,k), f'moment {n},{k}')
    for k in range(n+1):
        expected=Fraction(factorial(k)*cycle_matchings(n,k)*odd_fact(n-k),odd_fact(n))
        check(expected==exact_factorial_moment(n,k),f'cycle matching {n},{k}')

for n in range(2,41):
    a=[exact_factorial_moment(n,k) for k in range(n+1)]
    p=exact_distribution(n)
    check(sum(p)==1,f'norm {n}')
    check(all(x>=0 for x in p),f'positivity {n}')
    check(a[1] == Fraction(2*n,2*n-1), f'mean {n}')
    check(sum(r*p[r] for r in range(n+1))==a[1], f'from coeff mean {n}')
    check(a[2] + a[1]-a[1]**2 == 1-Fraction(1,(2*n-1)**2),f'variance {n}')
    check(all(a[k] <= Fraction(2*n,2*n-1) for k in range(n+1)), f'moment bound {n}')
    check(all((a[k+1] == a[k]*Fraction(2*n-2*k,2*n-k-1)) for k in range(n)),f'recurrence {n}')

# The first-order signed correction is a signed mass-zero perturbation.
Q=lambda r: -r*r+5*r-3
# Sum Q(r)/r! = 0 after multiplying by e^-1, from Poisson moments.
check(-2+5*1-3==0, 'coefficient normalization')
check(sum(Fraction(Q(r),factorial(r)) for r in range(1,5)) == Fraction(73,24), 'positive mass')
check([Q(r)>0 for r in range(8)]==[False,True,True,True,True,False,False,False], 'sign window')

# Numeric convergence sanity only. The proof of the limit is algebraic/analytic.
target=73/(96*exp(1))
for n in (40,80,120):
    p=exact_distribution(n)
    poisson=[exp(-1)/factorial(r) for r in range(n+1)]
    tv=sum(abs(float(p[r])-poisson[r]) for r in range(n+1))/2
    check(abs(n*tv-target) < 0.25/n, f'total variation convergence {n}')
    check(abs(n*(float(p[0])*exp(1)-1)+0.75)< 0.4/n, f'zero-chord correction {n}')

print(f'VERIFY_OK {checks} exact/reproducible assertions')
