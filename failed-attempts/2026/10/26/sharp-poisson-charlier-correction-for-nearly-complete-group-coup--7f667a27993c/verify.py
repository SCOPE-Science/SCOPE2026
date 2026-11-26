"""Exact rational checks for nearly complete group coupon drawings.

Only Python's standard library is required. Checks supplement the written proof.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb, exp, factorial


def factorial_moments(n, r, t):
    moments = [Fraction(1)]
    for j in range(1, r + 1):
        moments.append(moments[-1] * Fraction((r-j+1)**t, (n-j+1)**(t-1)))
    return moments


def exact_distribution(n, r, t):
    mu = factorial_moments(n, r, t)
    return [sum(((-1)**(j-k)) * comb(j,k) * mu[j] / factorial(j)
                for j in range(k,r+1)) for k in range(r+1)]


def brute_distribution(n, r, t):
    choices = list(combinations(range(n), r))
    totals = [0]*(r+1)
    for choice in product(choices, repeat=t):
        common=set(choice[0])
        for subset in choice[1:]:
            common.intersection_update(subset)
        totals[len(common)]+=1
    return [Fraction(v,len(choices)**t) for v in totals]


def signed_error_and_tv(n,r,t):
    p=exact_distribution(n,r,t)
    lam=n*(r/n)**t
    delta=t/r-(t-1)/n
    probs=[exp(-lam)*lam**k/factorial(k) for k in range(r+1)]
    extra=[]
    for k in range(r+1,r+100):
        extra.append(exp(-lam)*lam**k/factorial(k))
    char=lambda k: (k-lam)**2-k
    l1=sum(abs(float(p[k])-probs[k]*(1-delta*char(k)/2)) for k in range(r+1))
    l1+=sum(abs(v*(1-delta*char(r+1+j)/2)) for j,v in enumerate(extra))
    tv=(sum(abs(float(p[k])-probs[k]) for k in range(r+1))+sum(extra))/2
    T4=lambda z:z**4+6*z**3+7*z**2+z
    bound=(4+5*t+t*t/2)*exp(2*lam)*T4(2*lam)/(r*r)
    assert l1<=bound+1e-12
    assert abs(sum(p)-1)<Fraction(1,10**100)
    return lam, r*tv, l1*r*r, bound


for n,r,t in [(5,2,3),(6,3,2)]:
    assert exact_distribution(n,r,t)==brute_distribution(n,r,t)
    print('Exact enumeration matches:',n,r,t)

for n,r,t in [(100,10,2),(400,20,2),(1600,40,2),(64,16,3),(216,36,3)]:
    lam,scaled_tv,scaled_residual,bound=signed_error_and_tv(n,r,t)
    print(f'n={n} r={r} t={t} lambda={lam:.6g} '
          f'r*TV={scaled_tv:.10f} r^2*L1remainder={scaled_residual:.9f} '
          f'validated_bound={bound:.4g}')
print('All rational enumeration and bound checks passed.')
