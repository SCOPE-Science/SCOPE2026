"""Reproducible exact checks for birth-label/path-length covariance in recursive trees.

The finite checks supplement, but do not replace, the proof for all n.
Run: python verify_path_degree.py
"""
from fractions import Fraction
from itertools import product
from math import factorial, log, sqrt

checks = 0

def chk(v, msg):
    global checks
    if not v:
        raise AssertionError(msg)
    checks += 1

def harmonics(n):
    h = [Fraction(0)]
    h2 = [Fraction(0)]
    for k in range(1, n + 1):
        h.append(h[-1] + Fraction(1, k))
        h2.append(h2[-1] + Fraction(1, k*k))
    return h, h2

def predicted(n, i):
    h, h2 = harmonics(n)
    return (Fraction(n, i) - 1 - n * (h2[n-1] - h2[i-1])
            + h[n-1] - h[i-1])

def local(n, i, j):
    h, _ = harmonics(n)
    return Fraction(n, j*(j-1)) * (1 + h[i-1] - h[j-1])

# Exact enumeration of all recursive trees. Each parent vector is equally likely.
for n in range(3, 10):
    total = factorial(n-1)
    sum_L = 0
    sum_D = [0] * (n+1)
    sum_DL = [0] * (n+1)
    sum_I = [[0] * (n+1) for _ in range(n+1)]
    sum_IL = [[0] * (n+1) for _ in range(n+1)]
    for parents in product(*(range(1,j) for j in range(2,n+1))):
        depth = [0]*(n+1)
        degree = [0]*(n+1)
        for j,p in enumerate(parents, 2):
            depth[j] = depth[p] + 1
            degree[p] += 1
        length = sum(depth)
        sum_L += length
        for i in range(1,n+1):
            sum_D[i] += degree[i]
            sum_DL[i] += degree[i]*length
        for j,p in enumerate(parents,2):
            sum_I[p][j] += 1
            sum_IL[p][j] += length
    exp_L = Fraction(sum_L,total)
    for i in range(1,n+1):
        observed = Fraction(sum_DL[i],total) - Fraction(sum_D[i],total)*exp_L
        chk(observed==predicted(n,i), ('global',n,i,observed,predicted(n,i)))
        chk(sum(local(n,i,j) for j in range(i+1,n+1))==predicted(n,i),('sum',n,i))
        for j in range(i+1,n+1):
            observed_local = Fraction(sum_IL[i][j],total) - Fraction(sum_I[i][j],total)*exp_L
            chk(observed_local == local(n,i,j),('local',n,i,j,observed_local,local(n,i,j)))
    chk(sum(predicted(n,i) for i in range(1,n+1))==0,('total degree',n))

# Exact difference identity and one-crossing shape over a larger range.
for n in range(3, 151):
    cs = [predicted(n,i) for i in range(1,n+1)]
    chk(cs[0]<0,('root sign',n))
    chk(cs[n-2]>0 and cs[-1]==0,('terminal signs',n))
    chk(sum(cs)==0,('sum zero',n))
    for i in range(1,n):
        chk(cs[i]-cs[i-1]==Fraction(n-i*(i+1),i*i*(i+1)),('difference',n,i))
    first_positive = next(i for i,c in enumerate(cs,1) if c>0)
    chk(all(c<=0 for c in cs[:first_positive-1]),('neg side',n))
    chk(all(c>0 for c in cs[first_positive-1:-1]),('pos side',n))

# Asymptotic limit checks (numerical only: asymptotic claim is proved in text).
for n in [10**5, 10**6]:
    h = sum(1.0/k for k in range(1,n))
    # Compute tail from i to n-1 directly; avoid subtractive cancellation.
    for c in [0.6, 0.8, 1.0, 1.2, 1.5]:
        i = round(c*sqrt(n/log(n)))
        tail2 = sum(1.0/(k*k) for k in range(i,n))
        tail1 = sum(1.0/k for k in range(i,n))
        value = n/i - 1 - n*tail2 + tail1
        expected_limit = (1-c**(-2))/2
        # Loose diagnostic tolerance appropriate for finite n.
        chk(abs(value/log(n)-expected_limit)<0.15,('asymptotic diagnostic',n,c,value/log(n),expected_limit))

print(f'VERIFY_OK {checks} exact/diagnostic assertions')
