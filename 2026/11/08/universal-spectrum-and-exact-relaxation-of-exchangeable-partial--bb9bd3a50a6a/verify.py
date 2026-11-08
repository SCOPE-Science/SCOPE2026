#!/usr/bin/env python3
"""Finite exact checks for exchangeable subset-reshuffling kernels.

Standard library only. Exact rational convolution moments are compared with
Young-tableau Fourier predictions; these checks do not replace the proof.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations
from math import comb, factorial

CHECKS = 0

def check(cond, tag):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(tag)


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None:
        maximum = n
    for j in range(min(n, maximum), 0, -1):
        for rest in partitions(n-j, j):
            yield (j,) + rest


def contains(outer, inner):
    return all(i < len(outer) and outer[i] >= a for i,a in enumerate(inner))


@lru_cache(None)
def skew_tableaux(outer, inner=()):
    if not contains(outer, inner):
        return 0
    if outer == inner:
        return 1
    total = 0
    for i, a in enumerate(outer):
        if i + 1 < len(outer) and outer[i+1] == a:
            continue
        if a <= (inner[i] if i < len(inner) else 0):
            continue
        reduced = list(outer)
        reduced[i] -= 1
        if reduced[i] == 0:
            reduced.pop(i)
        total += skew_tableaux(tuple(reduced), inner)
    return total


def theoretical(n, w):
    predicted=[]
    for lam in partitions(n):
        dim=skew_tableaux(lam)
        eigen=sum((w[k] * F(skew_tableaux(lam,(k,)) if k else dim,dim)
                   for k in range(n+1)),F(0))
        predicted.extend([eigen]*(dim*dim))
        check(F(0)<=eigen<=1, ('nonnegative spectrum', n,lam,eigen))
        if lam != (n,):
            leading=F(n-sum(k*w[k] for k in range(n+1))-w[0],n-1)
            check(eigen<=leading, ('gap',n,lam,eigen,leading))
        for k in range(1,n+1):
            check((n-1)*skew_tableaux(lam,(k,)) <= (n-k)*dim if lam!=(n,) else True,
                  ('tableau bound',n,lam,k))
    check(len(predicted)==factorial(n), ('multiplicities',n))
    return predicted


def group_probabilities(n,w):
    group=list(permutations(range(n)))
    pr={}
    for g in group:
        s=sum(g[i]!=i for i in range(n))
        pr[g]=sum((w[k]*F(comb(n-s,k-s),comb(n,k)*factorial(k))
                   for k in range(s,n+1)),F(0))
    check(sum(pr.values())==1,('stochasticity',n))
    return group,pr


def compose(g,h):
    return tuple(g[i] for i in h)


def direct_moments(group,pr,two_only=False):
    n=len(group[0]); m=factorial(n)
    first=m*pr[tuple(range(n))]
    second=m*sum((p*p for p in pr.values()),F(0))
    if two_only:
        return first,second
    third=m*sum((pr[g]*pr[h]*pr[compose(g,h)]
                  for g in group for h in group),F(0))
    return first,second,third


def run():
    for n in range(2,7):
        samples=[]
        for k in [0,1,2,max(2,n-1),n]:
            w=[F(0)]*(n+1);w[k]=F(1)
            samples.append((f'K={k}',w))
        for p in [F(1,2),F(1,3)]:
            samples.append((f'Bernoulli {p}',[F(comb(n,k))*p**k*(1-p)**(n-k)
                                                 for k in range(n+1)]))
        # Non-binomial heterogeneous subset-size law.
        w=[F(k+1,(n+1)*(n+2)//2) for k in range(n+1)]
        samples.append(('weighted',w))
        for label,w in samples:
            check(sum(w)==1,(n,label,'weights'))
            vals=theoretical(n,w)
            group,pr=group_probabilities(n,w)
            two_only=n>=6
            moments=direct_moments(group,pr,two_only=two_only)
            for power,direct in enumerate(moments,1):
                check(sum((v**power for v in vals),F(0))==direct,
                      (n,label,power,'trace moments'))
            kmean=sum((k*w[k] for k in range(n+1)),F(0))
            standard=F(n-kmean-w[0],n-1)
            check(max(v for v in vals if v!=1)==standard if any(k>=2 and w[k] for k in range(n+1)) else True,
                  (n,label,'top eigen'))
    print('VERIFICATION_OK',CHECKS,'exact rational assertions')

if __name__=='__main__':
    run()
