"""Exact finite checks for sink counts in uniform acyclic orientations of bicliques.

No finite test is claimed to certify the asymptotic coefficient estimate.
"""
from fractions import Fraction
from math import factorial, comb, exp, log
from itertools import product

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def bell_poly_b(a, b):
    n = max(a,b)+1
    S = [[0]*(n+1) for _ in range(n+1)]
    S[0][0] = 1
    for i in range(1,n+1):
        for k in range(1,i+1):
            S[i][k] = S[i-1][k-1] + k*S[i-1][k]
    return sum(factorial(k)**2 * S[a+1][k+1] * S[b+1][k+1] for k in range(min(a,b)+1))


def sink_counts(a,b):
    total = bell_poly_b(a,b)
    E = [0]*(a+b+1)
    for r in range(a+1):
        for k in range(r+1):
            E[k] += comb(a,r)*bell_poly_b(a-r,b)*comb(r,k)*(-1)**(r-k)
    for r in range(b+1):
        for k in range(r+1):
            E[k] += comb(b,r)*bell_poly_b(a,b-r)*comb(r,k)*(-1)**(r-k)
    E[0] -= total
    return E


def brute_counts(a,b):
    counts = [0]*(a+b+1)
    num = 0
    for bits in product((0,1),repeat=a*b):
        # Direction bit 1 means A --> B. Directed cycle iff 2x2 alternating minor exists.
        if any(bits[i*b+j] == bits[k*b+l] != bits[i*b+l] == bits[k*b+j]
               for i in range(a) for k in range(i+1,a)
               for j in range(b) for l in range(j+1,b)):
            continue
        num += 1
        sinks_a = sum(all(bits[i*b+j] == 0 for j in range(b)) for i in range(a))
        sinks_b = sum(all(bits[i*b+j] == 1 for i in range(a)) for j in range(b))
        counts[sinks_a+sinks_b] += 1
    return num, counts

for a in range(1,5):
    for b in range(1,5):
        expected = sink_counts(a,b)
        check(sum(expected)==bell_poly_b(a,b),f'normalization {a,b}')
        check(expected[0]==0,f'no zero sinks {a,b}')
        check(all(x>=0 for x in expected),f'positivity {a,b}')
        total, actual = brute_counts(a,b)
        check(total==bell_poly_b(a,b),f'acyl count {a,b}')
        check(actual==expected,f'distribution {a,b} {actual} {expected}')
        for r in range(a+b+1):
            # Factorial-moment identity derived by marking named sinks in either part.
            factorial_moment = sum(comb(k,r)*expected[k] for k in range(len(expected)))
            predicted = (comb(a,r)*bell_poly_b(a-r,b) if r <= a else 0) + \
                        (comb(b,r)*bell_poly_b(a,b-r) if r <= b else 0)
            if r==0: predicted-=bell_poly_b(a,b)
            check(factorial_moment==predicted, f'factorial moments {a,b,r}')

rho=log(2)
for n in (5,10,20,30,40,50):
    cnt=sink_counts(n,n)
    tot=bell_poly_b(n,n)
    p=[c/tot for c in cnt]
    target=[0.]+[rho**k/factorial(k) for k in range(1,n*2+1)]
    tail=2-exp(rho)*sum(rho**k/factorial(k) for k in range(n*2+1)) # not used
    tv=.5*(sum(abs(x-y) for x,y in zip(p,target)) +
            (1.0-sum(target)))
    check(tv<1.0/n, f'asymptotic scale {n}: {tv}')
    print(f'n={n} TV={tv:.10f} n*TV={n*tv:.10f} mass1={p[1]:.10f}')

print(f'VERIFY_OK {checks} exact-enumerative and numerical cross-checks')
