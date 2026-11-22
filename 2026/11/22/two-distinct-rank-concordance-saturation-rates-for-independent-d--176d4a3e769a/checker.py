#!/usr/bin/env python3
"""Finite exact checks of the cyclic-occupation identity and rank algebra.

No finite experiment can establish the almost-sure asymptotic theorem.
"""
import itertools
import math
import random
from fractions import Fraction

checks = 0

# Steps +sqrt(2) (probability 2/3) or -1 (probability 1/3).
# If a positive and b negative steps have occurred, their sum is
# a*sqrt(2)-b, negative exactly when 2*a*a < b*b. Thus exact.
def count_negative(seq):
    a = b = total = 0
    for positive in seq:
        if positive: a += 1
        else: b += 1
        total += (2*a*a < b*b)
    return total

def weight(seq):
    return Fraction(2**sum(seq), 3**len(seq))

p = {}
A = [[Fraction(1)]]
for n in range(1, 10):
    actual = [Fraction(0) for _ in range(n+1)]
    neg = Fraction(0)
    for seq in itertools.product([0, 1], repeat=n):
        w = weight(seq)
        t = count_negative(seq)
        actual[t] += w
        if t == n: pass
        a = sum(seq)
        b = n-a
        if 2*a*a < b*b: neg += w
        checks += 1
    p[n] = neg
    pred = [Fraction(0) for _ in range(n+1)]
    # A_n(z) = 1/n sum_{k=1}^n ((1-p_k)+p_k*z^k) A_{n-k}(z)
    for k in range(1, n+1):
        for j, coef in enumerate(A[n-k]):
            pred[j] += (1-p[k])*coef / n
            pred[j+k] += p[k]*coef / n
            checks += 2
    assert actual == pred, ('cycle coefficients', n)
    assert sum(actual) == 1
    A.append(actual)
    checks += len(actual)+1

# Check both no-tie rank identities on every pair up to size five.
for n in range(2, 6):
    perms = list(itertools.permutations(range(1, n+1)))
    for x in perms:
        for y in perms:
            squared = sum((a-b)**2 for a,b in zip(x,y))
            rho = Fraction(1)-Fraction(6*squared, n*(n*n-1))
            mean = Fraction(n+1, 2)
            inner = sum((a-mean)*(b-mean) for a,b in zip(x,y))
            denom = sum((a-mean)**2 for a in x)
            assert rho == inner/denom
            discord = sum((x[i]-x[j])*(y[i]-y[j])<0 for i in range(n) for j in range(i+1,n))
            tau = Fraction(1)-Fraction(4*discord, n*(n-1))
            concord = n*(n-1)//2-discord
            assert tau == Fraction(concord-discord,n*(n-1)//2)
            checks += 2

# Check a deterministic non-monotone finite horizon with random increments.
rng = random.Random(2077)
for n in (8, 15, 40):
    for rep in range(30):
        stream = [rng.gauss(.85,1) for _ in range(n)]
        levels = list(itertools.accumulate(stream))
        ranks = [1+sum(w<z for w in levels) for z in levels]
        for i in range(n):
            net = sum(levels[j]<levels[i] for j in range(i+1,n))-sum(levels[j]>levels[i] for j in range(i))
            assert ranks[i]-i-1 == net
            checks += 1

# Values printed are for finite, rapidly convergent series only.
for a in (0.85, 1.0):
    terms = [0.5*math.erfc(a*math.sqrt(k/2)) for k in range(1,401)]
    c_rho = 24*sum((k+1)*v for k,v in enumerate(terms))
    c_tau = 8*sum(v*(1-v) for v in terms)
    assert c_rho>c_tau>0
    print('Gaussian a=',a,'C_rho=',format(c_rho,'.12f'),'C_tau=',format(c_tau,'.12f'))
    checks += 1
print('PASS',checks,'finite checks')
